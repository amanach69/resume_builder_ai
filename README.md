# Professional Resume Reviewer and Builder

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-GNU-green.svg)](LICENSE)

> **A smart AI-powered resume customization tool for AI/ML job seekers**

This intelligent application leverages state-of-the-art Language Models to analyze job descriptions, review resumes, and automatically generate tailored versions that align perfectly with specific job requirements. Built specifically for AI, ML, and Data Science roles, it streamlines the job application process and increases your chances of landing interviews.

## 📸 App Preview

Get a quick look at the **Resume Builder App** in action! Below are screenshots of the app's user interface and an example of the generated email response:

1. **App UI**

   ![App UI Screenshot](notebook/resources/Screenshot%202024-12-31%20190553.png)

2. **Modified Sample Resume**

   ![Modified Resume Screenshot](notebook/resources/Screenshot%202024-12-31%20191735.png)

3. **Comparison and Feedback On New Resume**

   ![Feedback Screenshot](notebook/resources/Screenshot%202024-12-31%20191818.png)

## 📋 Table of Contents

- [Features](#-features)
- [Why Use This App?](#-why-use-this-app)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Configuration](#-configuration)
- [Limitations](#-limitations)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Contact](#-contact)

## 🚀 Features

- **Smart Job Description Analysis:**

  - Automatic extraction from job posting URLs
  - Identification of key requirements and skills
  - Understanding of company culture and values

- **Comprehensive Resume Analysis:**

  - Deep evaluation against job requirements
  - Gap identification in skills and experience
  - Keyword optimization suggestions

- **Intelligent Resume Customization:**

  - Automated content restructuring
  - Skills and experience prioritization
  - Achievement highlighting based on job relevance

- **Detailed Review & Feedback:**
  - Side-by-side comparison
  - Improvement suggestions
  - ATS optimization tips

## 🌟 Why Use This App?

- **Time Efficiency:** Reduce resume tailoring time from hours to minutes
- **AI/ML Focus:** Specialized for tech roles in Data Science, ML Engineering, and Analytics
- **Smart Analysis:** Leverages multiple LLMs for comprehensive evaluation
- **ATS Optimization:** Ensures your resume passes Applicant Tracking Systems
- **Professional Guidance:** Provides expert-level feedback on improvements

## 🛠️ Tech Stack

### Core Technologies

- **Frontend:** Streamlit
- **Backend:** Python 3.9+
- **AI Framework:** LangChain

### AI Models

- **OpenAI:**
  - GPT-4
  - GPT-4-turbo
  - GPT-4.5-turbo
  - GPT-3.5-turbo
- **Groq:**
  - Gemma-2-9b
  - LLaMA-3-70b
  - LLaMA-3-8b
  - LLaMA-3.1-8b-instant
  - LLaVA-v1.5-7b

## 🛠️ Installation

### Streamlit Deployment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/resume-builder.git
   cd resume-builder
   ```

2. **Set Up Virtual Environment**

   Using Conda:

   ```bash
   conda create -n resume_builder python=3.9
   conda activate resume_builder
   ```

   Using venv:

   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Unix/MacOS:
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Launch the Application**

   ```bash
   streamlit run app.py
   ```

### Docker Deployment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/resume-builder.git
   cd resume-builder
   ```

2. **Build the Docker Image**

   ```bash
   docker build -t resume-builder:latest .
   ```

3. **Run the Docker Container**

   ```bash
   docker run -d -p 8501:8501 --name resume_builder_app resume-builder:latest
   ```

4. **Access the Application**

   Open your web browser and navigate to `http://localhost:8501` to access the Resume Builder application.

## 🔧 Configuration

### API Keys

- Get your Groq API key from [Groq Console](https://console.groq.com)
- Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com)

## ❗ Limitations

- **Domain Specificity:** Optimized for AI/ML roles; may need adjustments for other fields
- **Language Support:** Currently supports English resumes only
- **API Costs:** OpenAI models provide better results but incur usage costs
- **Processing Time:** Complex resumes may take longer to analyze

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**

   ```bash
   # Check if environment variables are set
   echo %GROQ_API_KEY%  # Windows
   echo $GROQ_API_KEY   # Unix/MacOS
   ```

2. **Dependencies Issues**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

## 📄 License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
