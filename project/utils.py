import requests
import config
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)

def research_hr_trends(query=None):
    """Fetches trending HR topics for 2025 using Serper API."""
    try:
        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": config.SERPER_API_KEY, "Content-Type": "application/json"}
        params = {"q": "Latest trending HR topics 2025", "num": 5}

        response = requests.post(url, json=params, headers=headers)
        data = response.json()

        if "organic" in data and data["organic"]:
            return [result["title"] for result in data["organic"]]  
        else:
            return ["HR Trends 2025: AI in Hiring", "Remote Work Policies", "Diversity & Inclusion"]

    except Exception as e:
        return [f"Error fetching HR trends: {e}"]

def generate_outline(topic):
    """Generates a structured blog outline."""
    prompt = f"Create a structured blog outline on the topic: '{topic}'."
    return llm.invoke(prompt).content.strip()

def generate_blog(outline):
    """Generates a blog post based on the outline."""
    prompt = f"Write a detailed blog based on this outline:\n\n{outline}\n\nLimit to 2000 words."
    return llm.invoke(prompt).content.strip()

def seo_optimization(content):
    """Optimizes the blog for SEO by integrating keywords."""
    prompt = f"Enhance this blog for SEO best practices by adding relevant keywords:\n\n{content}"
    return llm.invoke(prompt).content.strip()

def review_content(content):
    """Proofreads and enhances blog content."""
    prompt = f"Proofread and enhance this blog to make it publication-ready:\n\n{content}"
    return llm.invoke(prompt).content.strip()
