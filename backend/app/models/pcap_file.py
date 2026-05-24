from sqlalchemy import Column, Integer, String
from app.db.database import Base

class PcapFile(Base):

    __tablename__ = "pcap_files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    uploaded_by = Column(String, nullable=False)