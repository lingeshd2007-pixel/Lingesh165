from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage for quick revision.

Requirements:
- Preserve important facts and meaning.
- Use simple student-friendly language.
- Use a short heading and bullet points where useful.
- Remove repetition and unnecessary wording.
- Do not add information that is not present in the passage.

Passage:
{text}
"""
    return generate_text(prompt, temperature=0.2, max_output_tokens=1800)
