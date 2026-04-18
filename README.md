# 🚀 Resume Sentinel

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.30-orange)](https://www.crewai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Supabase](https://img.shields.io/badge/Supabase-Primary_DB-purple)](https://supabase.com/)

## 🔍 AI-Powered Resume Analysis & Job Matching Platform

**Resume Sentinel** is an intelligent web application that analyzes resumes against job descriptions using a multi-agent AI system built with **CrewAI**. Upload a resume (PDF/DOCX/TXT) and JD to get:

- **Match Score (0-100%)**
- **Skills Gap Analysis**
- **Critical Interview Questions**
- **Structured Skills Extraction**

Perfect for recruiters, hiring managers, and hackathons! Built for [Alphalogic Hackathon](https://github.com) 🏆

## ✨ Features

- **📄 Multi-Format Upload**: PDF, DOCX, TXT extraction
- **🤖 4-Agent AI Pipeline**:
  1. **Parser Agent**: Extracts skills & experience
  2. **Normalizer Agent**: Standardizes terminology  
  3. **Matcher Agent**: Computes match score
  4. **Inquisitor Agent**: Generates interview questions
- **☁️ Dual Database**: Supabase (primary) + PostgreSQL (fallback)
- **🔐 User Authentication**: Register/Login with Supabase sync
- **📊 Dashboard**: Saved profiles & analysis reports
- **⚡ Fast Inference**: Groq API + Mixtral-8x7B model
- **🚀 Production-Ready**: CORS, error handling, JSON APIs

## 🎯 Live Demo
```
http://localhost:5000
```

## 📸 Screenshots

![Logo](Alphalogic.png)

*(Add UI screenshots: Home, Analysis result, Dashboard)*

## 🚀 Quick Start (2 minutes)

1. **Clone & Install**
```bash
pip install flask crewai langchain-groq supabase pdfplumber python-docx flask-login flask-cors python-dotenv psycopg2-binary
```

2. **Environment Setup** (`.env`)
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
GROQ_API_KEY=gsk_...
DB_HOST=localhost  # Optional PostgreSQL
DB_NAME=resume_db_schema
DB_USER=postgres
DB_PASSWORD=yourpass
SENTINEL_SECRET_KEY=your-secret
```

3. **Run**
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000)

**Default Login**: `admin@sentinel.ai` / `admin123`

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐
│   Flask Web UI  │───▶│   File Extractor │
│ (Templates+JS)  │    │ (PDF/DOCX/TXT)   │
└─────────────────┘    └──────────────────┘
                              │
                              ▼
┌─────────────────┐    ┌──────────────────┐
│  Supabase DB    │◄──▶│ PostgreSQL DB    │
│ (Profiles/Reports)   │ (Fallback)     │
└─────────────────┘    └──────────────────┘
                              ▲
                              │
                    ┌──────────────────┐
                    │  CrewAI Pipeline │
                    │ Parser → Normalizer
                    │ Matcher → Inquisitor
                    └──────────┬─────────┘
                               │
                        ┌──────────────┐
                        │ Groq API     │
                        │ (Mixtral)    │
                        └──────────────┘
```

## 🔌 API Endpoints

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/` | GET | - | Home page |
| `/analyze` | POST | ✅ | Run AI analysis |
| `/profiles` | GET/POST | ✅ | Manage profiles |
| `/reports` | GET | ✅ | View reports |
| `/signin` | GET/POST | - | Login |
| `/register` | POST | - | Register |
| `/status` | GET | - | DB status |

**Analyze Request**:
```json
{
  "resume_file": (file),
  "jd": "Job description text...",
  "candidate_name": "John Doe"
}
```

## 🛠️ Local Development

### Prerequisites
- Python 3.8+
- PostgreSQL (optional)
- Supabase account (free tier)

### Full Setup
```bash
# 1. Database (Supabase - Recommended)
# Create project → Get URL/Key → Add to .env

# 2. PostgreSQL (Optional)
docker run -p 5432:5432 -e POSTGRES_PASSWORD=root -d postgres:15

# 3. Dependencies
pip install -r requirements.txt  # Create this!

# 4. Run
python app.py
```

### Agents Deep Dive
Each agent uses **CrewAI** + **Grok Mixtral**:

```python
# Example from orchestrator.py
task1 = Task(description="Extract skills...", agent=parser_agent)
# Sequential execution: Parser → Normalizer → Matcher → Inquisitor
```

## 🔧 Configuration

| Env Var | Required | Default | Purpose |
|---------|----------|---------|---------|
| `GROQ_API_KEY` | ✅ | - | AI inference |
| `SUPABASE_URL` | ✅ | - | Primary DB |
| `SUPABASE_KEY` | ✅ | - | DB access |
| `SENTINEL_SECRET_KEY` | ✅ | dev-key | Session security |

## 📁 Project Structure

```
Hacathon2/
├── app.py              # Flask app + routes + DB
├── orchestrator.py     # CrewAI pipeline
├── agents/             # 4 AI agents
│   ├── parser_agent.py
│   ├── normalizer_agent.py
│   ├── matcher_agent.py
│   └── inquisitor_agent.py
├── templates/          # HTML UI
│   ├── index.html
│   ├── signin.html
│   └── sigout.html
├── Alphalogic.png      # Logo
└── README.md           # You're reading it!
```

## 🚀 Deployment

**Vercel/Render**: Flask + Gunicorn
```bash
pip install gunicorn
gunicorn app:app
```

**Docker**: Coming soon!

## 🤝 Contributing

1. Fork repo
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit (`git commit -am 'Add amazing feature'`)
4. Push & PR

## 📄 License

MIT License - Use freely! 🎉

## 👥 Credits

Built for **Alphalogic Hackathon** by [Your Team]. Special thanks to:
- [CrewAI](https://crewai.com)
- [Groq](https://groq.com)
- [Supabase](https://supabase.com)

---

⭐ **Star us on GitHub** | 💬 [Issues](https://github.com/issues) | 📧 [Contact](mailto:hello@resumesentinel.ai)

