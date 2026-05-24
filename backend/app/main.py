from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.pcap import router as pcap_router

app = FastAPI(
    title="AI Network Troubleshooter",
    version="1.0.0"
)

app.include_router(auth_router)

app.include_router(pcap_router)

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