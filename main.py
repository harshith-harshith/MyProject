from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import financial_analyst, verifier
from tasks import analyze_financial_document, verification

app = FastAPI(title="Financial Document Analyzer")


# ---------------------------------------------------------
# Crew Execution Logic
# ---------------------------------------------------------

def run_crew(query: str, file_path: str):
    """
    Executes Crew workflow for financial document analysis.
    """

    financial_crew = Crew(
        agents=[verifier, financial_analyst],
        tasks=[verification, analyze_financial_document],
        process=Process.sequential
    )

    result = financial_crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ---------------------------------------------------------
# Main Analysis Endpoint
# ---------------------------------------------------------

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document")
):

    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file_id}.pdf"

    try:
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query or query.strip() == "":
            query = "Analyze this financial document"

        # Run Crew in thread executor (avoid blocking async loop)
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            run_crew,
            query.strip(),
            file_path
        )

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass


# ---------------------------------------------------------
# Local Run
# ---------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)