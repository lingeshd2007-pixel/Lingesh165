from gemini_client import generate_text


def get_learning_recommendations(topic: str, level: str = "Beginner") -> str:
    prompt = f"""
Create a personalized learning path for the topic: {topic}

Learner level: {level}

Structure:
1. Goal
2. Stage 1 - Foundations
3. Stage 2 - Core concepts
4. Stage 3 - Intermediate practice
5. Stage 4 - Advanced concepts
6. Practice/project ideas
7. Suggested resource types
8. A realistic 4-week or 8-week timeline

For every stage, include what to learn and what the learner should be able to do afterward.
Keep it practical for a student.
Do not invent specific URLs.
"""
    return generate_text(prompt, temperature=0.4, max_output_tokens=3000)
