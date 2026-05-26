from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.pcap import router as pcap_router

from app.api.reports import (
    router as reports_router
)

from app.api.history import router as history_router

app = FastAPI(
    title="AI Network Troubleshooter",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

app.include_router(pcap_router)

app.include_router(history_router)

app.include_router(
    reports_router
)

@app.get("/")
def root():

    return {
        "message": "AI Network Troubleshooter API Running"
    }

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }