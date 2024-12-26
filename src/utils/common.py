from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import streamlit as st
import pdfplumber
from docx import Document
from docx.shared import Pt, Inches

def initialize_llm(tool: str = None, api_key: str = None, model: str = None):
    """Initialize the LLM model for the application.

    Args:
        api_key (str): The api key for the LLM model.
        model (str): The model name.

    Returns:
        ChatOpenAI or ChatGroq: The LLM model object.
    """
    if tool.lower() == 'openai':
        return ChatOpenAI(api_key=api_key, model=model)
    
    elif tool.lower() == 'groq':
        return ChatGroq(model=model, api_key=api_key)
    else:
        raise ValueError("Invalid tool specified. Please choose 'openai' or 'groq'.")

def upload_resume() -> str:
    """Upload and read the resume file (PDF, DOCX, or TXT)."""
    uploaded_file = st.sidebar.file_uploader(
        "Upload Resume", 
        type=['pdf', 'docx', 'txt'], 
        accept_multiple_files=False
    )
    
    if not uploaded_file:
        st.info("Please upload a resume.")
        return None

    text = ""
    try:
        # PDF Handling
        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()
        # DOCX Handling
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text
        # TXT Handling
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode("utf-8")
        else:
            st.error("Unsupported file type.")
            return None
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

    return text