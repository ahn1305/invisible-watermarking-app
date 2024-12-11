### **Detailed Project README**

# **Invisible Watermarking Application**

A Python-based application powered by Streamlit that allows users to embed and extract invisible watermarks in images using the Discrete Cosine Transform (DCT). This project includes an intuitive web interface, making it accessible even to non-technical users.

---

## **What is Invisible Watermarking?**

Invisible watermarking is a technique used to embed imperceptible marks into digital media, such as images or videos, without affecting their visual quality. These watermarks are generally used to:

- Protect intellectual property.
- Authenticate ownership.
- Verify originality.
- Embed metadata for secure communication.

By leveraging the Discrete Cosine Transform (DCT), this project provides a robust way to embed watermarks directly into the frequency domain of images, ensuring minimal visible changes.

---

## **Why is This Application Needed?**

In the digital era, the authenticity and ownership of media assets are often challenged due to their ease of replication. This application is essential for:

1. **Digital Rights Management**: Embedding unique identifiers in images helps prove ownership in case of copyright disputes.
2. **Secure Image Distribution**: Organizations can use invisible watermarks to track the distribution of sensitive images.
3. **Brand Protection**: Watermarks ensure the visibility of branding, even when images are used without explicit permission.
4. **Steganography**: A method to hide information in images for secure communication.

---

## **Features**

1. **Embed Watermark**:
   - Embed a unique text (e.g., user ID, license number) into an image.
   - Download the watermarked image for secure sharing.

2. **Extract Watermark**:
   - Extract the embedded watermark from an image using its original version.
   - Retrieve text information using OCR (Optical Character Recognition).

3. **Streamlit Web Interface**:
   - User-friendly interface with drag-and-drop functionality for images.
   - Real-time preview of watermarked and extracted results.

---

## **Technologies Used**

- **Python**: Core language for development.
- **Streamlit**: Framework for creating the web interface.
- **OpenCV**: Image processing for watermark embedding and extraction.
- **NumPy**: Array manipulation for frequency-domain transformations.
- **SciPy**: Discrete Cosine Transform (DCT) operations.
- **Pillow**: Image handling and manipulation.
- **PyTesseract**: Optical Character Recognition (OCR) for watermark text extraction.

---

## **How to Use**

### **Prerequisites**

- Install Python (version 3.8 or higher).
- Basic familiarity with running Python scripts or Streamlit apps.

### **Step-by-Step Instructions**

#### **1. Clone the Repository**

```bash
git clone https://github.com/ahn1305/invisible-watermarking-app.git
cd invisible-watermarking-app
```

#### **2. Install Dependencies**

Use the following command to install all required Python libraries:

```bash
pip install -r requirements.txt
```

#### **3. Run the Application**

Start the application locally with Streamlit:

```bash
streamlit run watermark_app.py
```

This will open the application in your default web browser at `http://localhost:8501`.

#### **4. Using the Application**

- **Embed Watermark**:
  1. Select the "Embed Watermark" option from the sidebar.
  2. Upload an image and enter a unique identifier.
  3. Preview and download the watermarked image.

- **Extract Watermark**:
  1. Select the "Extract Watermark" option from the sidebar.
  2. Upload the original and watermarked images.
  3. View the extracted watermark and retrieve the embedded text.

---

## **Folder Structure**

```plaintext
watermarking-app/
├── watermark_app.py      # Main application script
├── requirements.txt      # Dependencies list
├── README.md             # Project overview and instructions
├── LICENSE               # Open-source license
├── .gitignore            # Files and folders to ignore in Git
└── Dockerfile            # Optional: For containerizing the application
```

---

## **Sample Workflow**

### **Embedding a Watermark**
1. Upload an image (`example.jpg`).
2. Enter a unique identifier (e.g., "1234ABCD").
3. Download the generated image (`watermarked_example.png`).

### **Extracting a Watermark**
1. Upload the original image (`example.jpg`).
2. Upload the watermarked image (`watermarked_example.png`).
3. View the extracted watermark and retrieve the text ("1234ABCD").

---

## **Additional Information**

### **Limitations**
1. Requires both the original and watermarked images for extraction.
2. Accuracy of watermark extraction may be impacted by image resizing, cropping, or compression.

### **Future Enhancements**
1. Add support for batch processing of images.
2. Implement advanced error correction for extracted watermarks.
3. Enable secure encryption of watermarks before embedding.
4. shareable link with tracking

### **Contributing**
Contributions are welcome! If you encounter bugs or have feature requests, please open an issue or submit a pull request.
To know more, read [ContributionGuide](ContributionGuide.md)

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contact Information**

- **Author**: [Ashwin B]
- **Email**: ahnashwin1305@gmail.com

Let us know how you use this application! Feedback and suggestions are always welcome. 😊