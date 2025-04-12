from fastapi import APIRouter, File, UploadFile, HTTPException
from services.parser import parse_pdf
from api.schemas import ExtractedData

router = APIRouter()

@router.post("/parse-pdf", response_model=ExtractedData)
async def parse_pdf_endpoint(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a PDF.")
    
    contents = await file.read()
    extracted = parse_pdf(contents)
    
    return extracted
