import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.analyzers.pcap_analyzer import (
    analyze_pcap
)

from app.ai.diagnostics import (
    generate_diagnostic_report
)

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

    # Run packet analysis
    analysis_results = analyze_pcap(
        file_path
    )

    # Generate AI diagnostics
    ai_report = generate_diagnostic_report(
        analysis_results
    )

    return {

        "filename": file.filename,

        "analysis": analysis_results,

        "ai_diagnostic_report": ai_report
    }