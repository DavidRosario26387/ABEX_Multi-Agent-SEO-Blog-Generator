# Multi-Agent Blog Generator using LangChain

### Overview
This project is a multi-agent blog generation system using the LangChain framework. It automates:
1. Researching a trend
2. Generating structured blog outlines
3. Creating blog content
4. Enhancing with SEO optimization
5. Proofreading for clarity and readability

### Key Highlights:

* LLMs (Llama 3-8B via Groq API) for AI-powered blog generation
* Serper API for real-time HR trend research
* LangChain agents for an autonomous workflow
* Streamlit UI for real-time progress tracking

### Tools & Frameworks Used
> python 3.10+ – Core language

> langChain – Multi-agent workflow execution

> Streamlit – UI for real-time progress updates

> Groq API (Llama 3-8B) – AI-powered blog content generation

> Serper API – Fetches HR trends from Google

> dotenv – Secure API key management

### Installation & Setup
1. Clone the Repository
```
git clone https://github.com/DavidRosario26387/ABEX_Multi-Agent-SEO-Blog-Generator.git
cd project
```
2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up API Keys
> Create a .env file in the project root and add:
```
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```
5. Run the Application
```
streamlit run app.py
```

> Project Structure
```
project/
│── app.py               
│── blog_pipeline.py      
│── agents.py            
│── utils.py             
│── config.py             
│── requirements.txt     
│── .env                
```
## Live Demo
Try the deployed project here: [Deployed model](https://davidrosario26387-abex-multi-agent-seo-blog-g-projectapp-b8hrsk.streamlit.app/)

## Project screenshots:
![1](https://github.com/user-attachments/assets/b439ba34-4726-47a4-8967-ad6567c7282e)
<hr>

![2](https://github.com/user-attachments/assets/10f7782a-9a0e-45d5-9c08-e4976993b993)
<hr>

![3](https://github.com/user-attachments/assets/529beb13-dc40-4e83-8210-4ab98a6e9a8c)
<hr>
<br><br>
This project was developed as part of the SDE Intern (Junior Python Developer) assessment for ABEX Excellence Private Limited.
