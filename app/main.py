from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
from app.answer_engine import generate_answer
from app.discourse_scraper import extract_text_from_image

app = FastAPI()

class Query(BaseModel):
    question: str
    image: str = None

@app.post("/api/")
async def answer_query(query: Query):
    if query.image:
        image_data = base64.b64decode(query.image)
        extracted_text = extract_text_from_image(image_data)
        query.question += f" {extracted_text}"
    
    answer, links = generate_answer(query.question)
    return {"answer": answer, "links": links}
