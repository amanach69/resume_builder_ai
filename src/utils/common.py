from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
import tempfile
import os


@st.cache_resource()
def initialize_llm(tool: str = None, api_key: str = None, model: str = None):
    """Initialize the LLM model for the application.

    Args:
        api_key (str): The OpenAI API key.
        model (str): The model name.

    Returns:
        ChatGroq: The initialized LLM model.
    """
    if tool.lower() == 'openai':
        return ChatOpenAI(api_key=api_key, model=model)
    
    elif tool.lower() == 'groq':
        return ChatGroq(model=model, api_key=api_key)
    else:
        raise ValueError("Invalid tool specified. Please choose 'openai' or 'groq'.")

def upload_resume() -> str:
    """Upload and read the resume file."""
    uploaded_file = st.sidebar.file_uploader("Upload Resume", type=['pdf'])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(uploaded_file.getvalue())
            pdf_path = temp.name

        resume_loader = PyPDFLoader(file_path=pdf_path)
        return ' '.join([doc.page_content for doc in resume_loader.load()])
    else:
        st.info("Please upload a resume")
        return None