from typing import List

from google.genai import types
from pydantic import BaseModel, Field

from gemini_client import MODEL_NAME, get_client


class QuizQuestion(BaseModel):
    question: str
    options: List[str] = Field(min_length=4, max_length=4)
    correct_answer: str
    explanation: str


class QuizResponse(BaseModel):
    questions: List[QuizQuestion]


def generate_quiz(passage: str, question_count: int = 3) -> dict:
    """Generate validated MCQs using Gemini structured output."""
    question_count = max(1, min(question_count, 10))

    prompt = f"""
Create exactly {question_count} multiple-choice questions from the educational text below.

Rules:
- Exactly 4 options per question.
- Only one option is correct.
- correct_answer must exactly equal one of the option strings.
- Include a short explanation.
- Test understanding rather than random tiny details.
- Return only the requested structured JSON.

Educational text:
{passage}
"""

    client = get_client()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
            max_output_tokens=4000,
            response_mime_type="application/json",
            response_schema=QuizResponse,
        ),
    )

    if getattr(response, "parsed", None):
        parsed = response.parsed
        data = (
            parsed.model_dump()
            if isinstance(parsed, QuizResponse)
            else QuizResponse.model_validate(parsed).model_dump()
        )
    else:
        data = QuizResponse.model_validate_json(response.text).model_dump()

    if len(data["questions"]) != question_count:
        raise RuntimeError(
            f"Gemini returned {len(data['questions'])} questions instead of {question_count}."
        )

    for question in data["questions"]:
        if question["correct_answer"] not in question["options"]:
            raise RuntimeError("Quiz validation failed: correct answer is not an option.")

    return data
