from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini/gemini-1.5-flash",
                               verbose=True,
                               temperature=0.5,
                               google_api_key=os.getenv("GOOGLE_API_KEY"))

test_agent = Agent(
      role="Test Agent",
      goal="Test LLM integration",
      llm=llm,
      verbose=True,
          backstory= (
        "Driven by curiorsity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world. "
    )
)

test_task = Task(description="Write a short poem about flowers.", 
                 agent=test_agent,
                 expected_output= 'A 4 paragraph article on advancements formatted as markdown.',

                 )

crew = Crew(
      agents=[test_agent],
      tasks=[test_task],
      verbose=True,
      process=Process.sequential
)

result = crew.kickoff()
print(result)