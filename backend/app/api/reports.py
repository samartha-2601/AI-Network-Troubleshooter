import json
import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.models.analysis import AnalysisReport

from sqlalchemy.orm import Session

from fastapi import Depends

from app.db.dependencies import get_db

from app.services.pdf_report import (
    generate_pdf_report
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/{report_id}")
def download_report(
    report_id: int,
    db: Session = Depends(get_db)
):

    report = (
        db.query(AnalysisReport)
        .filter(
            AnalysisReport.id == report_id
        )
        .first()
    )

    if not report:

        return {
            "error": "Report not found"
        }

    pdf_path = (
        f"reports/report_{report.id}.pdf"
    )

    generate_pdf_report(
        report.filename,
        json.loads(
            report.analysis_json
        ),
        report.ai_report,
        pdf_path
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=
        f"report_{report.id}.pdf"
    )