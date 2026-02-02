# ocr.py
import pytesseract
from PIL import Image
import os
import platform

if platform.system() == 'Windows':
    possible_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        os.path.expanduser(r'~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break
    else:
        pass

def extract_text(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except pytesseract.TesseractNotFoundError:
        error_msg = """
        Tesseract is not found. Please install it:
        
        1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
        2. Install it (note the installation path)
        3. If installed in a custom location, add this line at the top of ocr.py:
           
           pytesseract.pytesseract.tesseract_cmd = r'C:\\path\\to\\tesseract.exe'
        """
        raise Exception(error_msg)