# ✝️ Welcome to my Doc & Image Processing tool 😊 ✝️

---

## 👋 Hello there, Welcome! 

Thank you for visiting my repo! 😊 This is a **Personal Project** designed for image manipulation and file processing. If you are looking for a quick and **ZERO ADS**😜 way to handle your documents locally, you are in the right place! ✝️✨

This tool is a **Locally Installed Web Application** powered by a **Flask** backend. It provides a highly interactive and friendly user interface directly in your web browser! 🌐 

---

## 🌟 Main Features

Our digital Guagua-harvesting machine comes with 5 powerful core features:
*   📸 **Photo Edge Allocating ("Photo edge cutting")**: Upload your document photos, and dynamically drag **4 blue corner circles** to define the boundaries. The system will automatically perform a perspective transformation to flatten your document into a perfect A4 ratio!
*   📝 **Word to PDF Converter**: Transform your `.docx` files into clean PDF format in just one click!
*   📊 **Powerpoint to PDF Converter**: Convert slides `.pptx` directly to PDF for easy presentation sharing!
*   📈 **Excel to PDF Converter**: Flatten spreadsheets `.xlsx` into readable PDF documents!
*   🖼️ **JPG to PDF Converter**: Turn any standard image into a standard PDF file!

---
## ‼️ New UPDATES 
*   📖 **PDF to Word Converter**
*   📃 **PDF to Excel Converter**
*   📰 **PDF to Powerpoint Converter**
*   🙇‍♂️😞Might have some bugs, while converting to office file... I am still working on it

## 🛠️ Prerequisites & Installation

To run this project locally and start accumulating your Guagua seeds, please follow these setup instructions carefully! ✝️

### 1️⃣ Crucial Prerequisite: LibreOffice && Poppler🏢
This project uses **LibreOffice** as its underlying robust rendering engine to perform perfect, professional Office-to-PDF transformations. **You must download and install it on your machine first!**

*   🌐 **Official Website Download Link**: [Download LibreOffice Official Directly](https://www.libreoffice.org/download/download-libreoffice/)   [Download Poppler Official Directly](https://github.com/oschwartz10612/poppler-windows/releases/)
*   *Note for Windows users:* Ensure LibreOffice is installed in the default path (`C:\Program Files\LibreOffice\program\soffice.exe`) Poppler is installed in the default path (`C:\Program Files\poppler-26.02.0`)so the Flask backend can call it seamlessly!

### 2️⃣ Python Library Dependencies 📦
Open your VS Code terminal (or any terminal) and execute the following command to install all the necessary import libraries:

```bash
pip install Flask opencv-python numpy Pillow pandas pdf2docx pdfplumber pdf2image python-pptx
```

### 3️⃣ Running the Web App 🚀
Simply run

```bash
python app.py
```
Then open your browser and navigate to http://127.0.0.1:5000 😊!

### 🎬 Product Demonstration
Here is a visual sneak peek of how our amazing system operates! 😊✝️

📸Main Page Interface
<img width="720" height="480" alt="螢幕擷取畫面 2026-05-21 232748" src="https://github.com/user-attachments/assets/61860cc4-8dc9-4ea5-bb39-2677ac9ad875" />

🔧Photo Edge Allocating Function
<img width="600" height="400" alt="demo1" src="https://github.com/user-attachments/assets/00d56d54-0c4e-4dbc-8706-d61a76c66595" />


💾Transforming Office Files to PDF
<img width="600" height="400" alt="demo2" src="https://github.com/user-attachments/assets/8899f0a4-8ec0-4da8-bc70-3347bbb48ff2" />

## ⚠️ Disclaimer & Educational Purpose

🎨 Important Notice: This project is created strictly for educational purposes and personal experimentation with OpenCV and Flask web workflows. It should not be deployed as a high-concurrency production system without further enterprise security configurations.


If this tool helped you save time or gave you inspiration, please drop a Star ⭐ on this repository!
