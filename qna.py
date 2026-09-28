from gemini_client import generate_text

SYSTEM_PROMPT = """
You are EduGenie, a friendly educational assistant.
Answer the student's question accurately and clearly.
Use simple language suitable for a college student.
If the question is ambiguous, state the assumption.
Do not invent facts.
Use short headings or bullet points when useful.
Keep the answer concise unless the student asks for detail.
"""


def answer_question(question: str) -> str:
    prompt = f"""{SYSTEM_PROMPT}

Student question:
{question}

Give the best educational answer."""
    return generate_text(prompt, temperature=0.3, max_output_tokens=1800)
