# Professional Resume Reviewer and Builder

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-GNU-green.svg)](LICENSE)

> **A smart AI-powered resume customization tool for AI/ML job seekers**

This intelligent application leverages state-of-the-art Language Models to analyze job descriptions, review resumes, and automatically generate tailored versions that align perfectly with specific job requirements. Built specifically for AI, ML, and Data Science roles, it streamlines the job application process and increases your chances of landing interviews.

![Demo](assets/demo.gif)
_Note: Add a demo.gif to the assets folder to show the app in action_

## 📋 Table of Contents

- [Features](#-features)
- [Why Use This App?](#-why-use-this-app)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Configuration](#-configuration)
- [Limitations](#-limitations)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
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
  - GPT-3.5-turbo
- **Groq:**
  - Gemma-2-9b
  - LLaMA-3-70b
  - LLaVA-v1.5

### Deployment

- Streamlit Cloud Platform
- Docker support (coming soon)

## 💻 Installation

### Prerequisites

- Python 3.9 or higher
- Git
- Pip or Conda package manager

### Step-by-Step Setup

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

## 🔧 Configuration

### API Keys

- Get your Groq API key from [Groq Console](https://console.groq.com)
- Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com)

### Model Selection

You can configure which models to use in `config.yaml`:

```yaml
models:
  primary: gpt-4-turbo
  fallback: gemma-2-9b
```

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

3. **Memory Errors**
   - Reduce batch size in config.yaml
   - Use lighter models for analysis

## 👥 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Project Link: [https://github.com/<your-username>/resume-builder](https://github.com/<your-username>/resume-builder)

For support or queries, please [open an issue](https://github.com/<your-username>/resume-builder/issues) or contact the maintainers.
