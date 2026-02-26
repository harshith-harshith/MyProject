import os
from crewai_tools import tool
from langchain_community.document_loaders import PyPDFLoader


# ---------------------------------------------------------
# Financial Document Reader Tool
# ---------------------------------------------------------

@tool
def read_data_tool(path: str) -> str:
    """
    Reads a financial PDF document and extracts text content.

    Args:
        path (str): Path to uploaded PDF file.

    Returns:
        str: Extracted document text.
    """

    if not os.path.exists(path):
        return f"Error: File not found at {path}"

    try:
        loader = PyPDFLoader(path)
        documents = loader.load()

        if not documents:
            return "Error: No readable content found in the document."

        full_text = "\n".join(doc.page_content for doc in documents)

        return full_text.strip()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"