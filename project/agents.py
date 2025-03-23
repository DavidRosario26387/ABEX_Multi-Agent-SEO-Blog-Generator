from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from utils import research_hr_trends, generate_outline, generate_blog, seo_optimization, review_content
import os
from dotenv import load_dotenv

# Load API Keys
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)

# Define Tools
tools = [
    Tool(
        name="HR Trends Research", 
        func=research_hr_trends,
        description="Fetches the latest trending HR topics for 2025."
    ),
    Tool(
        name="Content Planning", 
        func=generate_outline,
        description="Creates a detailed blog outline."
    ),
    Tool(
        name="Content Generation", 
        func=generate_blog,
        description="Generates a blog post based on the outline."
    ),
    Tool(
        name="SEO Optimization", 
        func=seo_optimization,
        description="Optimizes the blog content for SEO."
    ),
    Tool(
        name="Review", 
        func=review_content,
        description="Proofreads and enhances the blog content for readability."
    )
]

# Ensure at least one tool is provided
if not tools:
    raise ValueError("No tools provided to the agent!")

# Initialize the Agent
agent_executor = initialize_agent(
    tools=tools,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm=llm,
    verbose=True
)
