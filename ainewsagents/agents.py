from crewai import Agent, LLM
from tools import tool
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
my_llm = LLM(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini/gemini-1.5-flash",
    verbose=True,
    temperature=0.5
    )


news_researcher = Agent(
    role = "Senior researcher",
    goal= "Uncover ground breaking technologies in {topic}",
    verbose= True,
    memory= True,
    backstory= (
        "Driven by curiorsity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world. "
    ),
    tools= [tool],
    llm=my_llm,
    allow_delegation=True
)

news_writer = Agent(
    role = "Senior Writer",
    goal= "Narrate compelling tech stories about {topic}",
    verbose= True,
    memory= True,
    backstory= (
      "With a flair for simplifying complex topics, you craft"
      "engaging narratives that captivate and educate, bringing new"
      "discoveries to light in an accessible manner."
    ),
    tools= [tool],
    llm=my_llm,
    allow_delegation=False
)