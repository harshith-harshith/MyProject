from crewai import Task
from agents import financial_analyst, verifier
from tools import read_data_tool


# ---------------------------------------------------------
# Document Verification Task
# ---------------------------------------------------------

verification = Task(
    description="""
    Verify whether the uploaded document located at {file_path} 
    is a legitimate financial document.

    Check for the presence of:
    - Revenue or income statements
    - Balance sheets
    - Cash flow statements
    - Investment disclosures
    - Financial ratios or metrics

    If the document does not appear financial in nature,
    clearly explain why.
    """,

    expected_output="""
    - Document Type Confirmation
    - Key Financial Indicators Detected (if any)
    - Final Decision: Valid Financial Document / Invalid Document
    """,

    agent=verifier,
    async_execution=False
)


# ---------------------------------------------------------
# Financial Analysis Task
# ---------------------------------------------------------

analyze_financial_document = Task(
    description="""
    Use read_data_tool to read the financial document located at {file_path}.

    Carefully analyze the document and answer the user query: {query}.

    Requirements:
    - Base all insights strictly on document content.
    - Do NOT fabricate information.
    - Avoid speculative or exaggerated claims.
    - Maintain a professional financial analysis tone.

    Focus on:
    - Revenue trends
    - Profitability metrics
    - Cost structure
    - Growth indicators
    - Liquidity & leverage indicators
    - Notable risks mentioned in the document
    """,

    expected_output="""
    Structured Financial Analysis Report:

    1. Executive Summary
    2. Revenue & Profitability Overview
    3. Key Financial Metrics (if available)
    4. Risk Assessment (document-based)
    5. Balanced Investment Insight
    """,

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False
)