import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.analyzers.pcap_analyzer import analyze_pcap

router = APIRouter(
    prefix="/pcap",
    tags=["PCAP Analysis"]
)

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_pcap(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    # Save uploaded file
    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    # Analyze PCAP
    analysis_results = analyze_pcap(file_path)

    return {
        "filename": file.filename,
        "analysis": analysis_results
    }