from groq import Groq
from schema import InvoiceData
from dotenv import load_dotenv
import os
import json

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an agentic document extraction system.

You receive noisy OCR text.
Your job is to:
- understand document intent
- correct OCR errors if obvious
- extract structured information
- return valid JSON ONLY

Return a JSON object with these fields:
- invoice_number
- invoice_date
- vendor_name
- total_amount
- currency

If a field does not exist, return null.
Never hallucinate values.
Return ONLY the JSON object, no other text.
"""


def extract_structured_data(ocr_text: str) -> InvoiceData:
    user_prompt = f"""
OCR TEXT:
----------------
{ocr_text}
----------------

Extract the information according to the schema and return ONLY valid JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        max_tokens=1000
    )

    json_output = response.choices[0].message.content
    
    json_output = json_output.strip()
    if json_output.startswith("```json"):
        json_output = json_output[7:]
    if json_output.startswith("```"):
        json_output = json_output[3:]
    if json_output.endswith("```"):
        json_output = json_output[:-3]
    json_output = json_output.strip()

    return InvoiceData.model_validate_json(json_output)
