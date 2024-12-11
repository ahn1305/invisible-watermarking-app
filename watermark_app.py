import cv2
import numpy as np
from scipy.fftpack import dct, idct
import pytesseract
import streamlit as st
from PIL import Image
from io import BytesIO

# Function to apply 2D DCT
def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

# Function to apply 2D inverse DCT
def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

# Function to embed a watermark into an image
def embed_watermark(image, watermark, alpha=0.1):
    image = np.float32(image) / 255.0
    watermark = np.float32(watermark) / 255.0
    image_dct = dct2(image)
    (w_h, w_w) = watermark.shape
    image_dct[:w_h, :w_w] += alpha * watermark
    watermarked_image = idct2(image_dct)
    watermarked_image = np.uint8(np.clip(watermarked_image * 255, 0, 255))
    return watermarked_image

# Function to generate a watermark image with text
def generate_watermark(text, size):
    watermark = np.zeros(size, dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(watermark, text, (10, size[1] // 2), font, 1, (255), 2, cv2.LINE_AA)
    return watermark

# Function to extract a watermark from a watermarked image
def extract_watermark(original_image, watermarked_image, alpha=0.1):
    original_image = np.float32(original_image) / 255.0
    watermarked_image = np.float32(watermarked_image) / 255.0
    original_dct = dct2(original_image)
    watermarked_dct = dct2(watermarked_image)
    watermark_dct = (watermarked_dct - original_dct) / alpha
    extracted_watermark = np.uint8(np.clip(watermark_dct * 255, 0, 255))
    return extracted_watermark

# Streamlit application
st.title('Invisible Watermarking Application')

st.sidebar.title('Options')
option = st.sidebar.selectbox('Select an option:', ('Embed Watermark', 'Extract Watermark'))

if option == 'Embed Watermark':
    st.header('Embed Watermark')
    uploaded_image = st.file_uploader('Upload a color image', type=['jpg', 'jpeg', 'png'])
    unique_id = st.text_input('Enter a unique identifier:')
    
    if uploaded_image is not None and unique_id:
        # Read the image as a color image (RGB)
        image = Image.open(uploaded_image).convert('RGB')
        image = np.array(image)
        
        # Create the watermark with the unique identifier (keep RGB channels the same size as the image)
        watermark = generate_watermark(unique_id, (image.shape[0], image.shape[1]))
        
        # Convert watermark to 3 channels to match the color image
        watermark_color = np.stack([watermark] * 3, axis=-1)
        
        # Embed the watermark into the image
        watermarked_image = np.zeros_like(image)
        for i in range(3):  # Process each channel (RGB)
            watermarked_image[..., i] = embed_watermark(image[..., i], watermark_color[..., i])

        # Show the watermarked image
        st.image(watermarked_image, caption='Watermarked Image', use_column_width=True)
        result = Image.fromarray(watermarked_image)
        st.success('Watermark embedded successfully!')

        # Save the watermarked image to an in-memory file
        buffer = BytesIO()
        result.save(buffer, format="PNG")  # Save as PNG format
        buffer.seek(0)

        # Allow user to download the watermarked image
        st.download_button(
            label="Download watermarked image",
            data=buffer,
            file_name="watermarked_image.png",
            mime="image/png"
        )

elif option == 'Extract Watermark':
    st.header('Extract Watermark')
    original_image_upload = st.file_uploader('Upload the original color image', type=['jpg', 'jpeg', 'png'])
    watermarked_image_upload = st.file_uploader('Upload the watermarked color image', type=['jpg', 'jpeg', 'png'])

    if original_image_upload is not None and watermarked_image_upload is not None:
        try:
            # Read the images as color images (RGB)
            original_image = Image.open(original_image_upload).convert('RGB')
            original_image = np.array(original_image)

            watermarked_image = Image.open(watermarked_image_upload).convert('RGB')
            watermarked_image = np.array(watermarked_image)
            
            # Check for shape mismatch
            if original_image.shape != watermarked_image.shape:
                raise ValueError(f"Image dimension mismatch: Original image has dimensions {original_image.shape}, "
                                 f"but the watermarked image has dimensions {watermarked_image.shape}.")

            # Extract the watermark for each color channel
            extracted_watermark = np.zeros_like(original_image)
            for i in range(3):  # Process each channel (RGB)
                extracted_watermark[..., i] = extract_watermark(original_image[..., i], watermarked_image[..., i])

            # Show the extracted watermark
            st.image(extracted_watermark, caption='Extracted Watermark', use_column_width=True)
            st.success('Watermark extracted successfully!')

            # Use OCR to read the extracted text from the watermark
            extracted_text = pytesseract.image_to_string(extracted_watermark)
            st.write(f'Extracted Unique ID: {extracted_text.strip()}')

        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
