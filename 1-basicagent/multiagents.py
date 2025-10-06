from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

yfinance_toolkit = YFinanceTools()

web_agent=Agent(
    name="Web_Agent",
    role="Search the web for information",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    #show_tool_calls=True,
    markdown=True,
)


finance_agent=Agent(
    name="Finance_Agent",
    role="Get financial data",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[yfinance_toolkit],
    instructions="Use tables to display data",
    #show_tool_calls=True,
    markdown=True,
)



for agent in [web_agent, finance_agent]:
    result = agent.run("analyse companies like tesla,nvidia,apple and tell me which one is the best for long time buy ratings also show 3 years max profits")
    print(result)
