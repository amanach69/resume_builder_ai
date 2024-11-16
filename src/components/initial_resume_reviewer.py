from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import streamlit as st

@st.cache_resource()
def review_resume(_llm, model: str, resume: str, job_description: dict) -> dict:
    """Review the resume against the job description.

    Args:
        _llm: The LLM model.
        resume (str): The resume content.
        job_description (dict): The extracted job description.

    Returns:
        dict: The parsed review output.
    """
    resume_review_prompt = ChatPromptTemplate.from_template(
        '''
        You are an experienced HR professional and resume reviewer specializing in aligning resumes with specific job descriptions. Your objective is to perform a comprehensive and detailed analysis of the provided resume in the context of the given job description. Your analysis will be used to enhance the resume to better fit the job requirements.

        **Instructions:**

        - Thoroughly read and understand both the resume and the job description.
        - Critically evaluate the resume's content, structure, and relevance to the job description.
        - Identify strengths, weaknesses, and areas for improvement with specific references to the resume and job description.

        **Provided Documents:**

        - **Resume:**
        {resume}

        - **Job Description:**
        {job_description}

        **Analysis Requirements:**

        1. **Overall Alignment:**
           - Assess the overall fit of the resume to the job description.
           - Indicate **Yes/No** on whether the resume matches the job requirements, and provide a justification.

        2. **Strengths:**
           - List specific sections or points in the resume that effectively showcase relevant skills, experiences, or qualifications.
           - Highlight any achievements or credentials that strongly align with the job description.

        3. **Weaknesses and Unnecessary Information:**
           - Identify areas where the resume lacks critical information or includes irrelevant details.
           - Point out any outdated or unnecessary inputs that do not contribute to the candidate's suitability.

        4. **Detailed Areas for Improvement:**
           - Provide actionable suggestions to enhance the resume's content and presentation.
           - Recommend ways to emphasize relevant skills and experiences that match the job description.
           - Suggest removal or modification of irrelevant or unnecessary information.

        5. **Missing Skills and Qualifications:**
           - List the specific skills, qualifications, or experiences mentioned in the job description that are missing from the resume.
           - Advise on how and where these can be incorporated if applicable.

        6. **Additional Relevant Skills:**
           - Identify any skills or experiences in the resume that, while not mentioned in the job description, could be advantageous for the role.
           - Explain how these additional skills can be leveraged.

        7. **Relation to Job Description:**
           - Analyze how each section of the resume relates to the specific requirements of the job.
           - Provide insights on alignment with the company's values, culture, or industry trends if applicable.

        8. **Formatting and Presentation:**
           - Comment on the resume's layout, formatting, and readability.
           - Suggest improvements for professional appearance and easy navigation for hiring managers.

        9. **Final Recommendation:**
           - Provide a comprehensive summary of the resume's suitability.
           - Assign a score on a scale of **1-10** reflecting the overall quality and fit.
           - Include a brief narrative highlighting key findings and recommendations.

        **Output Format:**

        Present your analysis in a structured JSON format as follows:

        ```json
        {{
            "OverallAlignment": {{
                "Match": "Yes/No",
                "Justification": "..."
            }},
            "Strengths": ["..."],
            "Weaknesses": ["..."],
            "AreasForImprovement": ["..."],
            "MissingSkills": ["..."],
            "AdditionalSkills": ["..."],
            "RelationToJobDescription": ["..."],
            "FormattingAndPresentation": ["..."],
            "FinalRecommendation": {{
                "Score": "...",
                "Summary": "..."
            }}
        }}
        ```

        Ensure that the JSON is properly formatted and all strings are enclosed in double quotes. Do not include any extraneous information outside of this JSON structure.
        '''
    )
    resume_review_chain = resume_review_prompt | _llm
    parser = JsonOutputParser()
    return parser.parse(resume_review_chain.invoke({'resume': resume, 'job_description': job_description}).content)