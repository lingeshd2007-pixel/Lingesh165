# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a complete FastAPI web application for students. It provides:

1. Ask a Question
2. Explain a Concept
3. Generate MCQ Quiz
4. Summarize Text
5. Recommend a Learning Path

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    ├── __init__.py
    └── test_health.py
```

## 1. Requirements

Install Python 3.10 or newer.

Check:

```bash
python --version
```

Windows may also use:

```bash
py --version
```

## 2. Open in VS Code

Open the **EduGenie** folder itself in VS Code.

## 3. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Create `.env`

Copy `.env.example` to a new file named:

```text
.env
```

Then put your Gemini API key in it:

```text
GEMINI_API_KEY=YOUR_REAL_KEY
GEMINI_MODEL=gemini-3.8-flash
ENABLE_LOCAL_EXPLAIN=false
```

Never commit `.env` to GitHub.

## 6. Run the project

From the folder containing `main.py`:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## 7. Test the API

Health:

```text
http://127.0.0.1:8000/health
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Automated tests:

```bash
pytest
```

## 8. Try the five features

### Q&A

```text
What is the difference between RAM and ROM?
```

### Explain

```text
Explain the Pythagoras theorem in simple language.
```

### Quiz

```text
Photosynthesis is the process by which green plants use sunlight,
water and carbon dioxide to produce food and oxygen.
```

### Summary

Paste a longer study paragraph.

### Learning path

```text
Python programming
```

Select Beginner, Intermediate, or Advanced.

## Troubleshooting

### API key error

If the app says `GEMINI_API_KEY is missing`, check that `.env` is in the same folder as `main.py`.

### Model error

Change `GEMINI_MODEL` in `.env` to a Gemini model available to your Google AI Studio/API project.

### Port already in use

```bash
uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001
```

### Python package error

Make sure `.venv` is active:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Optional local explanation model

The simplest setup is Gemini-only. If you specifically want the optional local LaMini fallback, install:

```bash
pip install transformers torch sentencepiece
```

Then set:

```text
ENABLE_LOCAL_EXPLAIN=true
LOCAL_EXPLAIN_MODEL=MBZUAI/LaMini-Flan-T5-783M
```

The local model can require substantial RAM/disk and is not necessary for the normal project.

## Architecture

```text
Browser
   |
   v
FastAPI (main.py)
   |
   +--> Q&A ----------------------+
   +--> Explanation --------------|
   +--> Quiz ---------------------|--> Gemini API
   +--> Summary ------------------|
   +--> Learning Path ------------+
   |
   v
HTML/CSS/JavaScript
```
