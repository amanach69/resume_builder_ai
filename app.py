import streamlit as st

from src.components.job_description_extractor import extract_job_description
from src.components.initial_resume_reviewer import review_resume
from src.components.resume_modifier import build_resume
from src.components.resume_compare_and_review import compare_resumes
from src.utils.common import initialize_llm, upload_resume

from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")
load_dotenv()

def main():
    """Main function to run the Streamlit app."""
    
    try:
    
        st.title("**Resume Builder and Reviewer**")
        
        api_key = st.sidebar.text_input("Enter your API key", type='password')
        
        tool = st.sidebar.selectbox("Select the LLM tool", ['OpenAI', 'GROQ'])
        
        if tool.lower() == 'openai':
            model = st.sidebar.selectbox("Select the model", ['gpt-4o', 'gpt-4.5-turbo', 'gpt-4-turbo', 'gpt-3.5-turbo'])
        else:
            model = st.sidebar.selectbox("Select the model", ['gemma2-9b-it', 'llama3-groq-70b-8192-tool-use-preview', 'llama-3.1-70b-versatile', 'llama3-70b-8192'])
        
        _llm = initialize_llm(tool=tool, api_key=api_key, model=model)
        
        resume = upload_resume()
        
        if resume:
            url = st.text_input("Enter the URL of the job description", "https://www.example.com")
            job_description = extract_job_description(_llm, url)
        
            parsed_resume_review = review_resume(_llm, resume, job_description)
            
            if 'generate_new_resume' not in st.session_state:
                st.session_state.generate_new_resume = False
                
            if st.button("Generate New Resume"):
                st.session_state.generate_new_resume = True
                
            if st.session_state.generate_new_resume:
                # Generate PDF from improved_resume
                improved_resume = build_resume(_llm, resume, job_description, parsed_resume_review)
                
                st.code(improved_resume)
                
                if 'generate_feedback' not in st.session_state:
                    st.session_state.generate_feedback = False
                
                if st.button("Generate Feedback"):
                    st.session_state.generate_feedback = True
                    
                if st.session_state.generate_feedback:
                    old_and_new_resume_review_output = compare_resumes(_llm, resume, improved_resume, job_description)
                    st.write('Old and New Resume Review \n')
                    st.code(old_and_new_resume_review_output)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()