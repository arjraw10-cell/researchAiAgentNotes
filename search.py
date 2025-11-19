from tavily import TavilyClient
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("Bruh put in ur tavily api key as an environment variable. In terminal on windows, just put it in the .env")

print(TAVILY_API_KEY)
tavily = 0

def web_search(query, max_results=5):
    """
    Returns structured internet search results.
    """
    result = tavily.search(
        query=query,
        max_results=max_results
    )

    return result["results"]
print(web_search("What is the biggest contributing factor to climate change?"))