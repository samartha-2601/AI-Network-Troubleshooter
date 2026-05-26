import os
import json

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.analysis import AnalysisReport

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
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
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

    # Determine severity
    severity = "LOW"

    failed_connections = (
        analysis_results.get(
            "tcp_analysis",
            {}
        ).get(
            "possible_failed_connections",
            0
        )
    )

    if failed_connections > 1000:

        severity = "HIGH"

    elif failed_connections > 100:

        severity = "MEDIUM"

    # Save analysis to database
    report = AnalysisReport(

        filename=file.filename,

        packet_count=
            analysis_results.get(
                "packet_count",
                0
            ),

        severity=severity,

        analysis_json=
            json.dumps(
                analysis_results
            ),

        ai_report=
            ai_report,

        user_id=1
    )

    db.add(report)

    db.commit()

    return {

        "filename": file.filename,

        "analysis": analysis_results,

        "ai_diagnostic_report": ai_report
    }