from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.record import Record

router = APIRouter()


@router.get("/dashboard/summary")
def get_summary(db: Session = Depends(get_db)):

    total_income = db.query(func.sum(Record.amount))\
        .filter(Record.type == "income").scalar() or 0

    total_expense = db.query(func.sum(Record.amount))\
        .filter(Record.type == "expense").scalar() or 0

    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }
