from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate, RecordResponse

router = APIRouter()

# CREATE RECORD


@router.post("/records", response_model=RecordResponse)
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    db_record = Record(
        amount=record.amount,
        type=record.type,
        category=record.category,
        date=record.date,
        notes=record.notes,
        created_by=1  # temporary user id
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


# GET ALL RECORDS (WITH FILTERING)
@router.get("/records")
def get_records(
    type: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Record)

    if type:
        query = query.filter(Record.type == type)

    if category:
        query = query.filter(Record.category == category)

    if start_date:
        query = query.filter(Record.date >= start_date)

    if end_date:
        query = query.filter(Record.date <= end_date)

    return query.all()


# DELETE RECORD
@router.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        return {"error": "Record not found"}

    db.delete(record)
    db.commit()
    return {"message": "Record deleted successfully"}
