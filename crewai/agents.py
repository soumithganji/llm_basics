from crewai import Agent 
from tools import yt_tool

# create a blog content researcher
blog_researcher = Agent(
    role='Blog researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from youtube channel',
    verbose= True,
    memory=True,
    backstory= (
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestions"
        ),
    tools=[yt_tool],
    allow_delegation=True
)

# create a blog writer agent 
blog_writer = Agent(
    role='Blog writer',
    goal='Narrate compelling tech stories about the ideo {topic} from the youtube channel',
    verbose= True,
    memory=True,
    backstory= (
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner"
        ),
    tools=[yt_tool],
    allow_delegation=False
)