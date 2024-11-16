from langchain_core.prompts import ChatPromptTemplate
import streamlit as st


def build_resume(_llm, resume: str, job_description: dict, review: dict) -> str:
    """Build an improved resume based on the review and job description.

    Args:
        _llm: The LLM model.
        resume (str): The resume content.
        job_description (dict): The extracted job description.
        review (dict): The parsed review output.

    Returns:
        str: The improved resume.
    """
    resume_builder_prompt = ChatPromptTemplate.from_template(
        '''
        You are a highly skilled resume writer specializing in transforming resumes into powerful tools that align perfectly with specific job descriptions in the fields of AI, ML, GenAI, Data Science, Data Engineering, and Data Analysis.

        **Objective:** 
        Thoroughly analyze the given resume, identify key contributions, achievements, and skills, and significantly enhance them using advanced vocabulary, business and technical terminologies, and industry-specific keywords. Use abbreviations and acronyms where appropriate to appeal to high-level executives like CEOs, CSOs, and CTOs who prefer concise and impactful resumes.

        **Constraints:**
        - Do not add new information or fabricate experiences.
        - Focus on rephrasing and enhancing existing content.
        - Paraphrase project descriptions and work experiences to make them stand out.
        - Incorporate business and technical terms, including short forms and industry-specific jargon.

        **Resources:**
        - **Pre-filled Resume:**  
        {resume}
        - **Job Description:**  
        {job_description}
        - **Expert Review and Suggestions:**  
        {review}

        **Instructions:**
        Analyze the weaknesses, areas for improvement, and final summary provided by the expert, and enhance the resume accordingly. Focus on the following aspects:
        
        ### **1. Combine Points for Conciseness:**
        - Merge multiple related points into fewer, more comprehensive statements to avoid redundancy.
        - Ensure all key information is retained while improving readability and impact.
        
        **Examples on combining multiple points:**

        ### Example 1: Data Analysis
        **Before:**
        - Analyzed sales data to identify trends and patterns.
        - Created detailed reports to present findings to management.
        - Recommended strategies to improve sales performance.

        **After:**
        - Analyzed sales data, generated detailed reports, and recommended strategies to enhance sales performance.

        ### Example 2: Machine Learning
        **Before:**
        - Developed a machine learning model to predict customer churn.
        - Tuned hyperparameters to improve model accuracy.
        - Deployed the model in a production environment.

        **After:**
        - Engineered and deployed a predictive ML model for customer churn with optimized hyperparameters.

        ### Example 3: Data Engineering
        **Before:**
        - Built a data pipeline to automate data collection and processing.
        - Ensured data accuracy and integrity throughout the pipeline.
        - Integrated various data sources into a unified system.

        **After:**
        - Developed an automated data pipeline ensuring accuracy and integrity, integrating multiple data sources.

        ### Example 4: Natural Language Processing (NLP)
        **Before:**
        - Created a chatbot using natural language processing techniques.
        - Improved the chatbot's response accuracy through continuous training.
        - Deployed the chatbot on the company's website to assist customers.

        **After:**
        - Architected and deployed an NLP-based chatbot, continuously enhancing response accuracy.

        ### Example 5: Data Visualization
        **Before:**
        - Designed interactive dashboards using Tableau.
        - Visualized key performance indicators for stakeholders.
        - Provided actionable insights to drive business decisions.

        **After:**
        - Developed Tableau dashboards visualizing KPIs, delivering actionable insights for strategic decisions.

        ### Example 6: Cloud Computing
        **Before:**
        - Migrated on-premises applications to AWS cloud.
        - Ensured high availability and scalability of applications.
        - Monitored and optimized cloud resources for cost efficiency.

        **After:**
        - Migrated applications to AWS, ensuring high availability, scalability, and cost-efficient resource optimization.

        ### Example 7: Project Management
        **Before:**
        - Led a team of data scientists and engineers to develop a new analytics platform.
        - Managed project timelines and deliverables.
        - Coordinated with stakeholders to ensure project alignment with business goals.

        **After:**
        - Led a cross-functional team to develop an analytics platform, managing timelines and stakeholder coordination.

        ### **2. Enrich Descriptions with Advanced Vocabulary:**
        - Rewrite projects and experiences using impactful, action-oriented language.
        - Use industry-specific jargon and acronyms where appropriate to demonstrate expertise (e.g., AI, ML, NLP, IoT, Big Data).
        - Emphasize key accomplishments and technical contributions with strong verbs (e.g., "implemented", "optimized", "engineered").
        - Replace simple words with business terminology for relevance and professionalism (e.g., "managed" to "oversaw", "led" to "orchestrated").

        **Examples:**
        - Before: "Developed a machine learning model to predict customer churn."
        - After: "Engineered a predictive ML model to forecast customer churn, enhancing retention strategies."

        - Before: "Worked on data preprocessing and feature engineering."
        - After: "Executed advanced data preprocessing and feature engineering to optimize model performance."

        - Before: "Built a chatbot using NLP techniques."
        - After: "Architected an intelligent chatbot leveraging NLP techniques to enhance customer interaction."

        - Before: "Analyzed large datasets to find trends."
        - After: "Conducted comprehensive analysis of large datasets to uncover actionable trends and insights."

        ### **3. Highlight Business and Technical Skills:**
        - Ensure high-priority skills are prominently featured.
        - Align terms with what high-level executives expect to see (e.g., "strategic planning", "cross-functional collaboration").

        **Examples:**
        - Before: "Skilled in Python and SQL."
        - After: "Proficient in Python and SQL, with expertise in data manipulation and analysis."

        - Before: "Experience with cloud platforms."
        - After: "Experienced in deploying scalable solutions on cloud platforms such as AWS and Azure."

        - Before: "Knowledge of machine learning algorithms."
        - After: "In-depth knowledge of machine learning algorithms, including supervised and unsupervised learning techniques."

        - Before: "Familiar with data visualization tools."
        - After: "Adept at using data visualization tools like Tableau and Power BI to present complex data insights."

        ### **4. Paraphrase for Impact:**
        - Reword existing content to be more compelling without adding new information (e.g., "Developed a new system" to "Pioneered an innovative system", "Managed a team" to "Led a high-performing team").
        - Enhance clarity and persuasiveness through advanced phrasing (e.g., "Improved efficiency" to "Drove operational efficiency enhancements", "Handled customer inquiries" to "Managed high-volume customer inquiries").

        **Examples:**
        - Before: "Improved model accuracy by tuning hyperparameters."
        - After: "Enhanced model accuracy through meticulous hyperparameter tuning."

        - Before: "Led a team of data scientists."
        - After: "Orchestrated a high-performing team of data scientists to deliver cutting-edge solutions."

        - Before: "Developed a data pipeline."
        - After: "Engineered a robust data pipeline to streamline data processing and integration."

        - Before: "Worked on data cleaning and transformation."
        - After: "Executed comprehensive data cleaning and transformation to ensure data integrity and quality."
        
        - Before: "Developed software using Python. Implemented machine learning algorithms. Achieved 20% performance improvement."
        - After: "Developed software using Python, implemented ML algorithms, and achieved a 20% performance improvement."

        - Before: "Built a data pipeline. Automated data collection. Improved data accuracy."
        - After: "Built and automated a data pipeline, significantly improving data accuracy."

        - Before: "Created dashboards using Power BI. Provided insights to stakeholders. Improved decision-making."
        - After: "Created Power BI dashboards to provide actionable insights to stakeholders, enhancing decision-making."

        - Before: "Developed a recommendation system. Used collaborative filtering. Improved user engagement."
        - After: "Developed a recommendation system using collaborative filtering, resulting in improved user engagement."
        
        
        ### **6. Align with Job Description:**
        - Map skills and experiences directly to job requirements.
        - Incorporate relevant keywords from the job description.

        **Examples:**
        - If the job description emphasizes "experience with NLP," ensure relevant NLP projects and skills are highlighted.
        - If the job description requires "cloud deployment experience," emphasize projects involving AWS, Azure, or GCP.

        - Before: "Worked on various machine learning projects."
        - After: "Executed multiple machine learning projects, including NLP and computer vision, aligning with job requirements."

        - Before: "Experience in data engineering."
        - After: "Proven experience in data engineering, including ETL processes and data pipeline development, as required by the job description."

        ### **7. Optimize Readability and Professionalism:**
        - Use consistent formatting for better readability (e.g., bullet points, bolding, italics).
        - Break down complex sentences; include bullet points where appropriate.
        - Emphasize impactful words through proper formatting (e.g., bold, italics) to draw attention to key achievements and skills.

        **Examples:**
        - Before: "Led a team of developers, designers, and analysts to create a new software platform."
        - After: "Led a team of developers, designers, and analysts to create a new software platform."

        - Before: "Developed a machine learning model to predict customer churn."
        - After: "Engineered a predictive ML model to forecast customer churn, enhancing retention strategies."

        - Before: "Built a data pipeline to automate data collection and processing."
        - After: "Engineered a robust data pipeline to automate data collection and processing, ensuring data accuracy and efficiency."

        - Before: "Created dashboards to visualize data insights."
        - After: "Developed interactive dashboards to visualize data insights, facilitating informed decision-making."

        ### **8. Remove Redundancies and Irrelevant Information:**
        - Remove redundant or irrelevant information that does not add value to the resume.
        - Ensure the resume is concise, impactful, and tailored to the job description.

        **Examples:**
        - Remove outdated skills or experiences that are not relevant to the current job application.
        - Focus on recent and relevant experiences that align with the job description.

        - Before: "Worked on various projects using different technologies."
        - After: "Focused on recent projects utilizing cutting-edge technologies relevant to the job description."

        - Before: "Experience with outdated programming languages."
        - After: "Highlighted experience with modern programming languages and tools relevant to the job description."

        **Final Review:**
        - Ensure the resume is concise, impactful, and tailored to the job description.
        - Repeat the enhancement process until the resume stands out among others.
        
        ### Ensure NO PREAMBLE AND NO POSTAMBLE
        
        Give the output in structured plain text format so that it can be easily converted into a PDF or Word document.
        '''
    )
    resume_builder_chain = resume_builder_prompt | _llm
    return resume_builder_chain.invoke({'resume': resume, 'job_description': job_description, 'review': review}).content