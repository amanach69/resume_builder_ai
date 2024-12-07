from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

@st.cache_resource()
def compare_resumes(_llm, model: str, old_resume: str, new_resume: str, job_description: dict) -> str:
    """Compare the old and new resumes and provide feedback.

    Args:
        _llm: The LLM model.
        old_resume (str): The old resume content.
        new_resume (str): The new resume content.
        job_description (dict): The extracted job description.

    Returns:
        str: The comparison and feedback output.
    """
    old_and_new_resume_review_prompt = ChatPromptTemplate.from_template(
        '''
        You are a professional resume reviewer tasked with comparing two resumes: an old version and an improved version. Your goal is to evaluate how the new resume has changed and assess its alignment with the provided job description.

        The old resume is as follows:
        {old_resume}

        The new resume is as follows:
        {new_resume}

        The job description is as follows:
        {job_description}

        Perform the following analysis:

        1. **Detailed Comparison of Resumes:**
           - **Changes Made:** Identify and explain the specific changes between the old and new resumes, highlighting additions, removals, and modifications.
           - **Impact on Alignment:** Explain how these changes have improved or affected the resume's alignment with the job description.

        2. **Alignment with Job Description:**
           - **Matched Requirements:** List the specific job requirements that are addressed in the new resume. Reference the exact sections or bullet points where these matches occur.
           - **Partial Matches:** Identify any requirements that are partially met and suggest how they could be fully addressed.
           - **Missing Requirements:** Highlight the job requirements not covered in the new resume and provide suggestions on how to include them.

        3. **Strengths of New Resume:**
           - Point out the strong aspects of the new resume, especially those that closely match the key requirements of the job description.
           - Explain how these strengths make the candidate a suitable fit for the position.

        4. **Weaknesses and Areas for Improvement:**
           - Identify sections where the new resume lacks information or could be further enhanced.
           - Provide actionable recommendations to improve these areas for better alignment with the job description.

        5. **Recommendations for Improvement:**
           - Offer specific advice on how to adjust or add content to the new resume to better meet the job requirements.
           - Suggest ways to highlight relevant experiences, skills, or achievements more effectively.

        6. **Overall Evaluation:**
           - **Likelihood of Getting the Job:** Estimate the likelihood (as a percentage from 0% to 100%) that the candidate will get the job with this resume, based on its alignment with the job description.
           - **Summary:** Provide a comprehensive summary of your findings, emphasizing key improvements and remaining areas for enhancement.

        Present your analysis in a clear and structured manner, using headings and bullet points to make it easy to understand which parts of the resume match the job description and what areas need improvement.
        
        ## NO PREAMBLE AND POSTAMBLE

        '''
    )
    old_and_new_resume_review_chain = old_and_new_resume_review_prompt | _llm
    return old_and_new_resume_review_chain.invoke({'old_resume': old_resume, 'new_resume': new_resume, 'job_description': job_description}).content