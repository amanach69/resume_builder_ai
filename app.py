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
    
        # title for the app
        st.markdown("<h1 style='text-align: center;'>📄 Resume Improvement Tool 📄</h1>", unsafe_allow_html=True)
        
        # select the LLM tool
        tool = st.sidebar.selectbox("Select the LLM tool", ['OpenAI', 'GROQ'])
        
        # select the model
        if tool.lower() == 'openai':
            model = st.sidebar.selectbox("Select the model", ['gpt-4o', 'gpt-4.5-turbo', 'gpt-4-turbo', 'gpt-3.5-turbo'])
        else:
            model = st.sidebar.selectbox("Select the model", ['gemma2-9b-it', 'llama3-groq-70b-8192-tool-use-preview', 'llama-3.1-8b-instant', 'llama3-8b-8192', 'llava-v1.5-7b-4096-preview'])
        
        # input for the API key
        api_key = st.sidebar.text_input("Enter your API key", type='password')
        
        # check if the API key is provided
        if api_key:
            
            # initialize the LLM model
            _llm = initialize_llm(tool=tool, api_key=api_key, model=model)
            
            # upload the resume
            resume = upload_resume()
            
            # check if the resume is uploaded
            if resume:
                # input for the job description URL
                url = st.text_input("Enter the URL of the job description", "https://www.example.com")
                
                if 'generate_new_resume' not in st.session_state:
                    st.session_state.generate_new_resume = False
                    
                if st.button("Generate New Resume"):
                    st.session_state.generate_new_resume = not st.session_state.generate_new_resume
                    
                if st.session_state.generate_new_resume:
                    
                    # extract the job description
                    job_description = extract_job_description(_llm, model, url)
                    
                    # convert the job description to string
                    job_description_str = str(job_description)

                    # review the resume
                    parsed_resume_review = review_resume(_llm, model, resume, job_description_str)
                    
                    improved_resume = build_resume(_llm, model, resume, job_description_str, parsed_resume_review)
                    
                    st.code(improved_resume)
                    
                    if 'generate_feedback' not in st.session_state:
                        st.session_state.generate_feedback = False
                    
                    if st.button("Generate Feedback"):
                        st.session_state.generate_feedback = not st.session_state.generate_feedback
                        
                    if st.session_state.generate_feedback:
                        old_and_new_resume_review_output = compare_resumes(_llm, model, resume, improved_resume, job_description_str)
                        st.write('Old and New Resume Review \n')
                        st.code(old_and_new_resume_review_output)
        else:
            st.info(":warning: Please enter your API key to proceed.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()