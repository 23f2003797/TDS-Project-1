import requests
import os

AI_PIPE_API_KEY = os.getenv("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDM3OTdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.ooPeiUm12TyB4g4y9f38z51oKLvYtqRBLKCCHk6f5Gc")
AI_PIPE_URL = "https://api.aipipe.ai/v1/chat/completions"

def generate_answer(question: str):
    headers = {
        "Authorization": f"Bearer {AI_PIPE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",  # Or another model AI Pipe supports
        "messages": [
            {"role": "system", "content": "You are a helpful virtual TA for the IITM TDS course."},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(AI_PIPE_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error from AI Pipe: {response.text}", []

    result = response.json()
    answer = result["choices"][0]["message"]["content"]

    # Dummy links for now — replace with your logic
    links = []
    return answer.strip(), links
