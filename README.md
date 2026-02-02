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

2. Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=gsk-your-actual-groq-api-key-here
   ```
   
   Get your free Groq API key at: https://console.groq.com/keys
   
   **Important**: Never commit your `.env` file to version control!

### 4. Run the Pipeline

```bash
python main.py
```

## Project Structure

- `main.py` - Entry point
- `ade_pipeline.py` - Orchestrates OCR and AI extraction
- `ocr.py` - Tesseract OCR wrapper
- `agent.py` - Groq-powered extraction agent (using Llama 3.3 70B)
- `schema.py` - Pydantic data models
- `.env` - Your environment variables (not tracked in git)
- `.env.example` - Template for environment variables

## How It Works

1. **OCR**: Extracts raw text from invoice image using Tesseract
2. **Agent**: Uses Groq's Llama 3.3 70B model to understand and structure the data
3. **Output**: Returns validated structured data (invoice number, date, vendor, amount, etc.)

- ⚡ **Ultra-fast inference** - Responses in milliseconds
- 🆓 **Free tier** - Generous free usage limits
- 🤖 **Powerful models** - Access to Llama 3.3 70B and other top models
