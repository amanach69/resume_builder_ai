# Professional Resume Reviewer and Builder  

**A smart and efficient app for freshers applying to AI and ML jobs.**  
This tool automates resume review and customization, saving time by tailoring resumes to job descriptions in just a few steps.  

---

## 🚀 Features  

- **Job Description Extraction:**  
  Provide a job posting link, and the app fetches relevant details using a powerful LLM chain.  

- **Resume Analysis:**  
  Upload your resume, and the app evaluates it against the job description to identify alignment gaps.  

- **Resume Customization:**  
  Automatically generates a modified resume tailored to the job description and feedback from the analysis phase.  

- **Detailed Review:**
  Compares the original and modified resumes, offering feedback on changes, relevance, and job suitability.  

---

## 🌟 Why Use This App?  

- **Saves Time:** No more manually rewriting resumes for every job application.  
- **Focused on AI/ML Roles:** Optimized for fields like Data Science, Data Analysis, and Data Engineering.  
- **Comprehensive Feedback:** Step-by-step insights into how your resume aligns with the job requirements.  
- **Automated and Smart:** Uses cutting-edge LLMs for accurate and efficient results.  

---

## 🛠️ Tech Stack  

- **Languages & Frameworks:**  
  Python, Streamlit, LangChain  

- **APIs & Libraries:**  
  Groq API, OpenAI API  

- **Core Models:**  
  - **OpenAI Models:** `gpt-4o`, `gpt-4.5-turbo`, `gpt-4-turbo`, `gpt-3.5-turbo`  
  - **Groq Models:** `gemma2-9b-it`, `llama3-groq-70b-8192-tool-use-preview`, `llama-3.1-8b-instant`, `llama3-8b-8192`, `llava-v1.5-7b-4096-preview`  

- **Deployment:**  
  Streamlit platform  

---

## 🖥️ How to Use  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/<your-username>/<repo-name>.git  
cd <repo-name>  
```  

### Step 2: Create a Virtual Environment  

#### Using `conda`:  
```bash  
conda create -n resume_builder python=3.9  
conda activate resume_builder  
```  

#### Using `pip` with `venv`:  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  

### Step 3: Install Requirements  
```bash  
pip install -r requirements.txt  
```  

### Step 4: Set Up API Keys  
Add your **Groq API** and **OpenAI API** keys in a `.env` file:  
```  
GROQ_API_KEY=your_groq_api_key_here  
OPENAI_API_KEY=your_openai_api_key_here  
```  

### Step 5: Run the App  
```bash  
streamlit run app.py  
```  

This point fits well in the **Limitations** section since it highlights a trade-off between cost and performance. Here's the updated section:

---

## 📌 Limitations  

- Optimized for AI/ML job roles. Performance may vary for other fields.  
- LLM results depend on the quality and clarity of job descriptions and resumes provided.  
- **Model Performance vs. Cost:** Based on usage, OpenAI models generally produce better results compared to open-source models. However, using OpenAI models incurs costs, making them less ideal for users seeking a completely free solution.

---

## 💡 Future Improvements  

- Extend support to other fields beyond AI and ML.  
- Add more resume templates and customization options.  
- Improve accuracy by fine-tuning LLMs. 

---

## 👥 Contributing  

Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch.  
3. Submit a pull request.  

---

## 📄 License  

This project is licensed under the ['GNU'](LICENSE)