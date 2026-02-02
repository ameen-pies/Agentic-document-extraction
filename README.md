# Invoice Extraction Pipeline

Agentic Document Extraction (ADE) system that uses OCR and AI to extract structured data from invoices.

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

- **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac**: `brew install tesseract`
- **Linux**: `sudo apt-get install tesseract-ocr`

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

   **Important**: Never commit your `.env` file to version control!

### 4. Run the Pipeline

```bash
python main.py
```

## Project Structure

- `main.py` - Entry point
- `ade_pipeline.py` - Orchestrates OCR and AI extraction
- `ocr.py` - Tesseract OCR wrapper
- `agent.py` - OpenAI-powered extraction agent
- `schema.py` - Pydantic data models
- `.env` - Your environment variables (not tracked in git)
- `.env.example` - Template for environment variables

## How It Works

1. **OCR**: Extracts raw text from invoice image using Tesseract
2. **Agent**: Uses GPT-4o-mini to understand and structure the data
3. **Output**: Returns validated structured data (invoice number, date, vendor, amount, etc.)
