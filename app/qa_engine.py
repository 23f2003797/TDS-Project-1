from app.utils import load_data, get_relevant_chunks, generate_answer

# Preload data and embeddings
course_data = load_data("data/course_content.json")
discourse_data = load_data("data/discourse_posts.json")
all_docs = course_data + discourse_data

# Main answer generator
def answer_question(question: str):
    top_chunks = get_relevant_chunks(question, all_docs)
    answer = generate_answer(question, top_chunks)
    links = [chunk["link"] for chunk in top_chunks if "link" in chunk]
    return answer, [{"url": l, "text": "Relevant link"} for l in links[:2]]
