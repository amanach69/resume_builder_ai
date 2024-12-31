from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, FireCrawlLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain_community.document_loaders import FireCrawlLoader


import streamlit as st
from typing import Literal

@st.cache_resource()
def extract_job_description(_llm, url: str, type: Literal['default', 'firecrawl'] = 'default', api_key: str = None) -> dict:
    """Extract job description from the provided URL using specified scraping method.

    Args:
        _llm: The LLM model.
        url (str): The URL of the job description.
        type (Literal['default', 'firecrawl']): The scraping method to use.
            'default': Uses WebBaseLoader (no API key required)
            'firecrawl': Uses FireCrawlLoader (requires API key)
        api_key (str, optional): API key required when using 'firecrawl' type.
            Not required for 'default' type.

    Returns:
        dict: The extracted job description containing structured information about the job.
            Including job title, description, responsibilities, qualifications,
            tools/technologies, and experience requirements.

    Raises:
        ValueError: If 'firecrawl' type is selected but no API key is provided.
    """
    try:
        job_description_prompt = ChatPromptTemplate.from_template(
            '''
            You are a highly skilled job description analyst. Your task is to extract structured and detailed information from the provided text extracted from the website.
            
            ### SCRAPED TEXT FROM THE WEBSITE:
            {page_data}

            Please extract and organize the following details in JSON format with these keys:
            "Job Title": The title of the job.
            "Detailed Job Description": A concise summary of the role, including its purpose and objectives.
            "Key Responsibilities": A list of the primary responsibilities and duties associated with the role.
            "Skills": A list highlighting the key skills, abilities, or competencies required for the role.
            "Required Qualifications": A list highlighting the educational background, certifications, or mandatory requirements.
            "Preferred Tools and Technologies": A list of the software, tools, or technologies mentioned or implied in the job description.
            "Experience Requirements": Specify the years and types of experience required.

            Please provide the data in valid JSON format without any additional text or preamble.
            
            ## NO PREAMBLE AND POSTAMBLE 
            '''
        )
        if type == 'default':
            website_loader = WebBaseLoader(web_path=url)
            page_data = website_loader.load()
            job_description_extractor_chain = job_description_prompt | _llm
            parser = JsonOutputParser()
            response = job_description_extractor_chain.invoke({'page_data': page_data[0].page_content}).content
            fixing_parser = OutputFixingParser.from_llm(llm=_llm, parser=parser)
            parsed_response = fixing_parser.parse(response)
            # st.expander("Extracted Job Description", expanded=True).write(parsed_response)
            return parsed_response
        
        elif type == 'firecrawl':
            if api_key is None:
                raise ValueError("API key is required for FireCrawlLoader.")
            
            firecrawl_loader = FireCrawlLoader(url=url, api_key=api_key)
            page_data = firecrawl_loader.load()
            job_description_extractor_chain = job_description_prompt | _llm | JsonOutputParser()
            response = job_description_extractor_chain.invoke({'page_data': page_data[0].page_content})
            # st.expander("Extracted Job Description", expanded=True).write(response
            return response
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None