from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser

import streamlit as st

@st.cache_resource()
def extract_job_description(_llm, url: str) -> dict:
    """Extract job description from the provided URL.

    Args:
        _llm: The LLM model.
        url (str): The URL of the job description.

    Returns:
        dict: The extracted job description.
    """
    website_loader = WebBaseLoader(web_path=url)
    job_description = website_loader.load()
    
    job_description_prompt = ChatPromptTemplate.from_template(
        '''
        You are a highly skilled job description analyst. Your task is to extract structured and detailed information from the provided job description.
        
        The job description is as follows:
        {job_description}
        
        Please extract and organize the following details:
        1. **Job Title:** Clearly state the title of the job.
        2. **Detailed Job Description:** Provide a concise summary of the role, including its purpose and objectives.
        3. **Key Responsibilities:** List the primary responsibilities and duties associated with the role.
        4. **Required Qualifications:** Highlight the educational background, certifications, or mandatory requirements.
        5. **Preferred Tools and Technologies:** List the software, tools, or technologies mentioned or implied in the job description.
        6. **Experience Requirements:** Specify the years and types of experience required.
        
        Output this information in a JSON format.
        '''
    )
    job_description_extractor_chain = job_description_prompt | _llm
    parser = JsonOutputParser()
    return parser.parse(job_description_extractor_chain.invoke({'job_description': job_description[0].page_content}).content)