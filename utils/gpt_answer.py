import requests

def generate_answer(question, context_notes, marks):
    prompt = f"""
You are a smart exam assistant. Use the notes below to answer the question in a simple format suitable for a {marks}-mark exam answer.

Notes:
{context_notes}

Question:
{question}

Answer:
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",   # <- model name (llama3, mistral, gemma etc.)
                "prompt": prompt,
                "stream": False      # disables streaming, returns full answer
            }
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        return f"Error generating answer locally: {e}"

