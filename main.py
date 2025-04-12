from fastapi import FastAPI
from api.urls import router

app = FastAPI(
    title="PDF OM Parser API",
    description="Extracts property name, address, and rentable square footage from real estate Offering Memorandums (PDFs)."
)

app.include_router(router, prefix="/api")
