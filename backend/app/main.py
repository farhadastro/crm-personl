from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from .api.v1.api import api_router
from .db.session import engine, Base

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Consultancy CRM API")

# CORS middleware for Vercel frontend
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRM API"}
