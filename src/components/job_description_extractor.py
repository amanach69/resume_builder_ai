from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

import streamlit as st

@st.cache_resource()
def extract_job_description(_llm, model: str, url: str) -> dict:
    """Extract job description from the provided URL.

    Args:
        _llm: The LLM model.
        model (str): The model name.
        url (str): The URL of the job description.

    Returns:
        dict: The extracted job description.
    """
    website_loader = WebBaseLoader(web_path=url)
    page_data = website_loader.load()
    
    job_description_prompt = ChatPromptTemplate.from_template(
        '''
        You are a highly skilled job description analyst. Your task is to extract structured and detailed information from the provided text extracted from the website.
        
        ### SCRAPED TEXT FROM THE WEBSITE:
        {page_data}

        Please extract and organize the following details in JSON format with these keys:
        "Job Title": The title of the job.
        "Detailed Job Description": A concise summary of the role, including its purpose and objectives.
        "Key Responsibilities": A list of the primary responsibilities and duties associated with the role.
        "Required Qualifications": A list highlighting the educational background, certifications, or mandatory requirements.
        "Preferred Tools and Technologies": A list of the software, tools, or technologies mentioned or implied in the job description.
        "Experience Requirements": Specify the years and types of experience required.

        Please provide the data in valid JSON format without any additional text or preamble.
        '''
    )
    job_description_extractor_chain = job_description_prompt | _llm
    parser = JsonOutputParser()
    response = job_description_extractor_chain.invoke({'page_data': page_data[0].page_content}).content
    fixing_parser = OutputFixingParser.from_llm(llm=_llm, parser=parser)
    parsed_response = fixing_parser.parse(response)
    return parsed_response