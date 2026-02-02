from ocr import extract_text
from agent import extract_structured_data


def run_ade(image_path: str):
    print("📸 OCR: extracting text...")
    ocr_text = extract_text(image_path)

    print("🧠 Agent: reasoning & structuring...")
    structured_data = extract_structured_data(ocr_text)

    return structured_data