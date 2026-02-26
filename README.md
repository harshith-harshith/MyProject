# Financial Document Analyzer - Debug Assignment

## Project Overview
A refactored and debugged financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents built with CrewAI and FastAPI.

## Getting Started

### Install Required Libraries
```sh
pip install -r requirements.txt
```
# Environment Configuration

# Create a .env file in the root directory and add:

OPENAI_API_KEY=your_api_key_here

# Running the Application
uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

### Sample Document

You can test the system using financial documents such as Tesla’s quarterly financial reports.

## To test using a sample PDF:

1. Download a financial report (for example from Tesla’s investor relations page).

2. Upload the PDF using the /analyze API endpoint.

3. Provide an optional query for specific analysis (e.g., revenue growth, risk insights).

## API Documentation

# Endpoint

POST /analyze

# Request Parameters

- file → Financial PDF document (required)

- query → Optional analysis instruction

# Example Request

curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@financial_report.pdf" \
  -F "query=Analyze revenue trends and identify risks"

# Example Response
{
  "status": "success",
  "query": "Analyze revenue trends and identify risks",
  "analysis": "...structured financial analysis...",
  "file_processed": "financial_report.pdf"
}

# Final Features

- Upload financial documents (PDF format)

- Document validation before analysis

- AI-powered structured financial analysis

- Revenue and profitability insights

- Risk assessment based strictly on document content

- Balanced investment insights grounded in financial data