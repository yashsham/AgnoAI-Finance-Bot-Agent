from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent =Agent(
    model=Gemini(id="gemini-2.0-flash"),
    description="you are the assistant please answers like a professional of the field which is ask by the user.",
    tools=[DuckDuckGoTools()],
    markdown=True,)


agent.print_response("can you tell me according to reviews who pornstar girl with name is famous.")

