import fitz  
import re
from api.schemas import ExtractedData

def parse_pdf(file_bytes: bytes) -> ExtractedData:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    
    property_name = doc[0].get_text().split('\n')[0].strip()

    address_match = doc[0].get_text().split('\n')[1].strip()
    sqft_match = re.search(
    r"([\d,]+)\s*(RSF|SF|sqft|square feet|Rentable SF|Rentable Square Feet)", text, re.IGNORECASE
    )


    return ExtractedData(
        property_name=property_name or "Not found",
        address=address_match or "Not found",

        total_rentable_sqft=sqft_match.group(1) if sqft_match else "Not found"
    )


