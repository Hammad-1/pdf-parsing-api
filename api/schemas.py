from pydantic import BaseModel

class ExtractedData(BaseModel):
    property_name: str
    address: str
    total_rentable_sqft: str
