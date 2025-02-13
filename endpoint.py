# pip install python-multipart python-docx PyMuPDF
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Optional
import fitz  # PyMuPDF
import docx

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str
    email: str
    extra: Optional[str] = None

def extract_text_from_pdf(content: bytes) -> str:
    pdf_document = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_word(content: bytes) -> str:
    doc = docx.Document(content)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def extract_text_from_txt(content: bytes) -> str:
    return content.decode("utf-8")

def index_text(content: str) -> dict:
    words = content.split()
    index = {}
    for position, word in enumerate(words):
        word = word.lower()
        if word in index:
            index[word].append(position)
        else:
            index[word] = [position]
    return index

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/plain"]:
        return {"error": "File type not supported"}
    
    content = await file.read()
    if file.content_type == "application/pdf":
        content_str = extract_text_from_pdf(content)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        content_str = extract_text_from_word(content)
    elif file.content_type == "text/plain":
        content_str = extract_text_from_txt(content)
    
    index = index_text(content_str)
    
    return {
        "filename": file.filename, 
        "content_type": file.content_type,
        "content": content_str,
        "index": index
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")