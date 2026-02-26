import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import read_data_tool

# Load environment variables
load_dotenv()

# Validate API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# Initialize LLM (deterministic for financial analysis)
llm = LLM(
    model="gpt-4o-mini",
    api_key=api_key,
    temperature=0
)

# ---------------------------------------------------------
# Financial Analyst Agent
# ---------------------------------------------------------

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze uploaded financial documents and provide structured, "
        "data-backed insights strictly based on document content and the user's query: {query}"
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a CFA-certified financial analyst with experience in corporate financial reporting. "
        "You focus on factual accuracy, financial ratios, profitability trends, and risk indicators. "
        "You avoid speculation and do not fabricate information. "
        "All analysis must be grounded in the provided financial document."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# ---------------------------------------------------------
# Financial Document Verifier Agent
# ---------------------------------------------------------

verifier = Agent(
    role="Financial Document Compliance Officer",
    goal=(
        "Verify whether the uploaded file is a legitimate financial document "
        "containing financial statements, revenue data, balance sheets, "
        "cash flow reports, or investment disclosures."
    ),
    verbose=True,
    memory=False,
    backstory=(
        "You specialize in document compliance and validation. "
        "You carefully inspect documents to determine whether they contain financial reporting information. "
        "If the document is not financial in nature, clearly state the reason."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ---------------------------------------------------------
# Investment Advisor Agent
# ---------------------------------------------------------

investment_advisor = Agent(
    role="Investment Advisor",
    goal=(
        "Provide balanced and compliance-aware investment insights "
        "based strictly on the financial analysis results."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a licensed investment advisor. "
        "You provide diversified and risk-aware investment suggestions "
        "based only on verified financial data. "
        "You avoid speculative or high-risk unsupported recommendations."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ---------------------------------------------------------
# Risk Assessment Agent
# ---------------------------------------------------------

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal=(
        "Identify and evaluate financial risks mentioned in the document "
        "such as liquidity risk, leverage exposure, market volatility, "
        "operational risk, or macroeconomic risks."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial risk analyst. "
        "You assess downside exposure, financial stability, and risk concentration "
        "based only on documented financial data."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)