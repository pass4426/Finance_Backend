from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # income / expense
    category = Column(String, nullable=False)
    date = Column(Date)
    notes = Column(String)
    created_by = Column(Integer)