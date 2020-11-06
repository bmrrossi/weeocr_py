from sqlalchemy import Column, Integer, String
from weeocr_py.db.base import Base

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    extension = Column(String(5))
    date = Column(String(20))
    
    def __init__(self, name=None, extension=None, date=None):
        self.name = name
        self.extension = extension
        self.date = date
