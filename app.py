from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import PyPDF2
from transformers import pipeline

app = FastAPI()

class Query(BaseModel):
    question: str

# Load the open-source LLM (e.g., GPT-Neo)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Store the uploaded document
document_text = ""

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global document_text
    if file.content_type == "application/pdf":
        pdf_reader = PyPDF2.PdfFileReader(file.file)
        document_text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            document_text += page.extract_text()
        return {"message": "PDF document uploaded successfully"}
    else:
        return {"error": "Invalid file format. Please upload a PDF document."}

@app.post("/query")
async def query_document(query: Query):
    if not document_text:
        return {"error": "No document uploaded"}

    # Split the document into chunks
    chunks = [document_text[i:i+1000] for i in range(0, len(document_text), 1000)]

    # Perform semantic search to retrieve the top 3 relevant chunks
    relevant_chunks = []
    for chunk in chunks:
        if query.question.lower() in chunk.lower():
            relevant_chunks.append(chunk)
        if len(relevant_chunks) >= 3:
            break

    if not relevant_chunks:
        return {"answer": "I don't know the answer"}

    # Generate a response using the open-source LLM
    response = generator(query.question, max_length=50, num_return_sequences=1)
    return {"answer": response[0]['generated_text']}
