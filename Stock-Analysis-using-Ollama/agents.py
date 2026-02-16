import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  # change to "mistral" if needed


def ask_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=360
        )

        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:
        return f"Error communicating with Ollama: {e}"


def researcher_agent(fundamentals: dict) -> str:
    prompt = f"""
You are a professional equity research analyst.

Analyze the following company fundamentals:

{fundamentals}

Provide:
- Business summary
- Financial strength
- Valuation view
- Growth outlook
"""
    return ask_llm(prompt)


def technical_agent(technical_data: dict) -> str:
    prompt = f"""
You are a technical market analyst.

Analyze the following indicators:

{technical_data}

Explain:
- Trend direction
- Momentum strength
- Risk signals
"""
    return ask_llm(prompt)


def advisor_agent(fundamental_analysis: str, technical_analysis: str) -> str:
    prompt = f"""
You are a senior investment strategist.

Based on:

Fundamental Analysis:
{fundamental_analysis}

Technical Analysis:
{technical_analysis}

Provide:
- Investment outlook
- Risk assessment
- Final recommendation (Buy/Hold/Sell)
- Short-term vs Long-term view
"""
    return ask_llm(prompt)
