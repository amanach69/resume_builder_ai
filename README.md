# 📄 Professional Resume Reviewer and Builder  

> 🎯 **Transform your resume intelligently with AI-powered customization**

This smart tool helps job seekers customize their resumes automatically using advanced AI. Perfect for professionals targeting AI and ML positions, it analyzes job descriptions and optimizes resumes in seconds.

---

## ✨ Features  

🤖 **Intelligent Job Analysis**
- Extracts key requirements from job URLs
- Understands context and priorities
- Supports multiple job boards

📝 **Smart Resume Review**
- Deep analysis of your current resume
- Gap identification with job requirements
- Skill alignment checking

✨ **AI-Powered Customization**
- Automatic resume tailoring
- Keyword optimization
- Format preservation

📊 **Comprehensive Feedback**
- Before-after comparison
- Improvement suggestions
- Alignment scoring

---

## 🎯 Why Choose This Tool?  

- ⚡ **Lightning Fast:** Generate tailored resumes in minutes
- 🎯 **AI/ML Focused:** Optimized for tech roles
- 📈 **Data-Driven:** Uses advanced LLMs for accuracy
- 🔄 **Iterative:** Continuous improvement through feedback

---

## 🛠️ Technology Stack  

### Core Technologies
- 🐍 Python 3.9+
- 🌟 Streamlit
- 🔗 LangChain

### AI Models
- 🤖 **OpenAI:** `gpt-4o`, `gpt-4.5-turbo`, `gpt-4-turbo`, `gpt-3.5-turbo`
- 🧠 **Groq:** `gemma2-9b-it`, `llama3-groq-70b-8192-tool-use-preview`, and more

---

## Installation

### Option 1: Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ayushach007/resume_builder_ai
   ```
2. Navigate to the project directory:
   ```bash
   cd resume_builder_ai`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Docker Installation 🐳

If you have Docker installed, you can run the application in a container:

1. Build the Docker image:
   ```bash
   docker build -t resume-builder-app .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 resume-builder-app
   ```

## Usage

### Local Usage
1. Start the application:
   ```bash
   streamlit run Data_Analysis_App📊.py
   ```
2. Access the app at `http://localhost:8501` in your web browser.

### Docker Usage
- The application will automatically start when you run the container
- Access the app at `http://localhost:8501` in your web browser
- To stop the container, use `docker stop <container_id>`

## 📌 Limitations  

- 🎯 Best suited for AI/ML roles
- 📊 Results quality depends on input data
- 💰 Premium models (OpenAI) offer better results but at a cost

---

## 🔜 Roadmap  

- [ ] Multi-language support
- [ ] Additional resume templates
- [ ] Custom LLM fine-tuning
- [ ] ATS score prediction
- [ ] Interview preparation suggestions

---

## 🤝 Contributing  

We welcome contributions! Here's how:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch
3. 💻 Make your changes
4. 🔍 Test thoroughly
5. 📤 Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License  

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ by Ayush Acharya
</div>