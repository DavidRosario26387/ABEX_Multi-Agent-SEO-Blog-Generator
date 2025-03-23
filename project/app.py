# app.py
import streamlit as st
from blog_pipeline import run_blog_pipeline

# Streamlit UI Setup
st.set_page_config(page_title="Blog Generator", layout="centered")
st.title("Blog Generation Tool")
st.header("Generate a blog about HR trends for 2025")

st.write("Click below to generate the blog based on the latest HR trends for 2025:")

if st.button("Generate Blog"):
    status_area = st.empty()  # Placeholder for status updates
    final_blog = run_blog_pipeline(status_area)  # Pass the placeholder
    
    st.subheader("Final Generated Blog")
    st.write(final_blog)