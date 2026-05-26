from app.db.database import engine
from app.db.database import Base

from app.models.user import User

import app.models.analysis

from app.models.pcap_file import PcapFile

def init_db():

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()