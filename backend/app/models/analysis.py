from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.db.database import Base


class AnalysisReport(Base):

    __tablename__ = "analysis_reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    packet_count = Column(
        Integer,
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
    )

    analysis_json = Column(
        Text,
        nullable=False
    )

    ai_report = Column(
        Text,
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )