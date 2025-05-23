import openai

openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDM3OTdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.ooPeiUm12TyB4g4y9f38z51oKLvYtqRBLKCCHk6f5Gc"

def generate_answer(question: str):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    links = []  # Extract relevant links based on the answer
    return answer, links
