from tools import fetch_fundamentals, technical_analysis
from agents import researcher_agent, technical_agent, advisor_agent


def run_stock_analysis(ticker: str):

    print("Fetching fundamentals...")
    fundamentals = fetch_fundamentals(ticker)

    print("Running technical analysis...")
    technicals = technical_analysis(ticker)

    print("AI analyzing fundamentals...")
    fundamental_report = researcher_agent(fundamentals)

    print("AI analyzing technical indicators...")
    technical_report = technical_agent(technicals)

    print("AI generating final recommendation...")
    final_report = advisor_agent(fundamental_report, technical_report)

    return final_report
