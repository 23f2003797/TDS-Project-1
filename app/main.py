from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.qa_engine import answer_question
import base64
import io
from PIL import Image
import pytesseract

app = FastAPI()

class QuestionInput(BaseModel):
    question: str
    image: str | None = None

@app.post("/api/")
async def get_answer(input_data: QuestionInput):
    extracted_text = ""
    if input_data.image:
        image_data = base64.b64decode(input_data.image)
        image = Image.open(io.BytesIO(image_data))
        extracted_text = pytesseract.image_to_string(image)
    
    final_question = input_data.question + "\n" + extracted_text
    answer, links = answer_question(final_question)
    return {"answer": answer, "links": links}
