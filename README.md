# Job Scraper LLM Project 🚀

## Overview
The **Job Scraper LLM Project** is an AI-powered application that scrapes job listings from online sources and uses **Large Language Models (LLMs)** to analyze, structure, and match job descriptions with candidate skills.

This project demonstrates **LLM integration, modular Python architecture, and real-world automation use cases**.

---

## Key Features
- Automated Job Data Fetching
- Job Description Parsing & Cleaning
- LLM-Based Structuring of Job Data
- Skill & Experience Extraction
- Job Matching Logic
- Modular & Scalable Code Design

---

## Tech Stack
- **Python**
- **LLM APIs** (OpenAI / Gemini / HuggingFace)
- **BeautifulSoup / Requests**
- **Pandas**
- **Environment Variables (.env)**
- **REST APIs**

---

## Project Architecture

```
JOB_SCRAPER_LLM_PROJECT/
│
├── config/                 # Configuration files
│
├── llm/                    # LLM related processing
│   ├── jd_structurer.py    # Structures raw job description using LLM
│   ├── matcher.py          # Matches skills / job roles
│
├── scraper/                # Scraping & parsing logic
│   ├── fetcher.py          # Fetches job data from websites
│   ├── parser.py           # Cleans & processes HTML/text
│   ├── jd_parser.py        # Job description specific parsing
│
├── storage/                # Data storage / output handling
│
├── utils/                  # Helper / utility functions
│
├── main.py                 # Entry point of the application
├── requirements.txt        # Dependencies
└── README.md
```

---

## How to Run

### 1. Clone Repository
```
git clone https://github.com/RutikP/job-scraper-llm.git
cd job-scraper-llm
```

### 2. Create Virtual Environment (Optional but Recommended)
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Add API Key
Create a `.env` file in the root folder:

```
API_KEY=your_api_key_here
```

---

### 5. Run Application
```
python main.py
```

---

## Example Output
 
Total jobs found: 3

Processing job 1/3: Account Executive, Airbnb for Business
Processing job 2/3: Acquisition Lead, Experiences, Mexico City (12 month contract)
Processing job 3/3: Acquisition Manager, Experiences, Mexico City

===== JOB MATCH RESULTS (RANKED) =====

1. Account Executive, Airbnb for Business
   Match Score   : 85
   Is Match      : True
   Experience Fit: Partial match
   Matched Skills: ['Sales', 'CRM', 'Negotiation', 'Client Management']
   Missing Skills: []
   URL           : https://careers.airbnb.com/positions/7434393/

---

## Use Cases
- Automated Job Search Assistance  
- Resume Skill Gap Analysis  
- Job Market Research  
- Candidate–Job Matching Systems  

---

## Future Improvements
- Streamlit / Flask UI  
- Database Integration  
- Multi-Platform Scraping  
- Semantic Embedding Search  
- Notification System  

---

## Best Practices Followed
- Modular Architecture  
- Environment Variable Security  
- Clean Code & Separation of Concerns  
- Dependency Management  
- Scalable Folder Structure  

---

## Author
**Rutik Panchal**  
Applied Machine Learning Enthusiast  
Focused on building real-world AI & LLM systems.

---

## License
This project is for educational and demonstration purposes.

