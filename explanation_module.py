import os

from gemini_client import generate_text


def _local_explanation(concept: str) -> str:
    """Optional local LaMini explanation; used only when explicitly enabled."""
    from transformers import pipeline

    model_name = os.getenv(
        "LOCAL_EXPLAIN_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M",
    )
    generator = pipeline(
        "text2text-generation",
        model=model_name,
        max_new_tokens=300,
    )

    prompt = (
        "Explain the following concept in simple language for a student. "
        "Use a short definition, key points, and one example.\n\n"
        f"Concept: {concept}"
    )
    result = generator(prompt, do_sample=False)
    return result[0]["generated_text"].strip()


def explain_concept(concept: str) -> str:
    use_local = os.getenv("ENABLE_LOCAL_EXPLAIN", "false").lower() == "true"

    if use_local:
        try:
            return _local_explanation(concept)
        except Exception:
            # Gemini remains the reliable fallback.
            pass

    prompt = f"""
You are EduGenie's concept explanation tutor.

Explain this concept:
{concept}

Requirements:
1. Start with a one-sentence definition.
2. Explain it in very simple language.
3. Give 3-5 important points.
4. Give one practical or academic example.
5. Avoid unnecessary jargon.
"""
    return generate_text(prompt, temperature=0.3, max_output_tokens=1800)
