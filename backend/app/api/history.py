from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from fastapi import Depends

from app.models.analysis import AnalysisReport

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_history(
    db: Session = Depends(get_db)
):

    reports = (
        db.query(AnalysisReport)
        .order_by(
            AnalysisReport.created_at.desc()
        )
        .all()
    )

    return reports