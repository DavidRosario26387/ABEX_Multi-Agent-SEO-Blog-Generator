import time
import streamlit as st
from utils import research_hr_trends, generate_outline, generate_blog, seo_optimization, review_content
from agents import agent_executor

def run_blog_pipeline(status_area=None):
    steps = [
        "Fetching HR Trends...",
        "Generating Blog Outline...",
        "Generating Blog Content...",
        "Optimizing Blog for SEO...",
        "Reviewing and Proofreading Content..."
    ]

    status_log = []
    
    def update_status():
        status_area.markdown("\n".join(status_log))

    # Step 1: Fetch HR Trends
    status_log.append(f"🟡 {steps[0]}")
    update_status()
    hr_trends = agent_executor.run("Fetch trending HR topics for 2025.")
    status_log[-1] = f"🟢 {steps[0]}"
    update_status()

    # Step 2: Generate Blog Outline
    status_log.append(f"🟡 {steps[1]}")
    update_status()
    outline = generate_outline(hr_trends)
    status_log[-1] = f"🟢 {steps[1]}"
    update_status()

    # Step 3: Generate Blog Content
    status_log.append(f"🟡 {steps[2]}")
    update_status()
    blog_content = generate_blog(outline)
    status_log[-1] = f"🟢 {steps[2]}"
    update_status()

    # Step 4: Optimize for SEO
    status_log.append(f"🟡 {steps[3]}")
    update_status()
    seo_optimized_content = seo_optimization(blog_content)
    status_log[-1] = f"🟢 {steps[3]}"
    update_status()

    # Step 5: Review Content
    status_log.append(f"🟡 {steps[4]}")
    update_status()
    reviewed_content = review_content(seo_optimized_content)
    status_log[-1] = f"🟢 {steps[4]}"
    update_status()

    return reviewed_content
