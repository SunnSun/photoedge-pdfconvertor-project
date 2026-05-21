import os
import subprocess
from PIL import Image

def convert_jpg_to_pdf(input_path, output_path):
    try:
        image = Image.open(input_path).convert('RGB')
        image.save(output_path)
        return True
    except Exception as e:
        print(f"Error converting JPG: {e}")
        return False

def convert_office_to_pdf(input_path, output_dir):
    try:
        libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
        
        subprocess.run([
            libreoffice_path, '--headless', '--convert-to', 'pdf', 
            input_path, '--outdir', output_dir
        ], check=True)
        return True
    except Exception as e:
        print(f"Error converting Office file: {e}")
        return False