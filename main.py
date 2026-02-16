from dotenv import load_dotenv
from orchestrator import run_stock_analysis

load_dotenv()


if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    result = run_stock_analysis(ticker)

    print("\n===== FINAL INVESTMENT REPORT =====\n")
    print(result)
