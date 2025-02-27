# endpoints/attendees.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Attendee, Event
from schemas import AttendeeCreate, AttendeeResponse
from crud import create_attendee, get_attendee, check_in_attendee
from authentication import get_current_user
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/attendees/", response_model=AttendeeResponse)
def register_attendee(attendee: AttendeeCreate,
                      db: Session = Depends(get_db),
                      current_user: dict = Depends(get_current_user)):
    
    event = db.query(Event).filter(Event.event_id == attendee.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.max_attendees <= db.query(Attendee).filter(Attendee.event_id == attendee.event_id).count():
        raise HTTPException(status_code=400, detail="Event is full")

    
    return create_attendee(db, attendee)


@router.post("/attendees/{attendee_id}/check-in", response_model=AttendeeResponse)
def check_in_attendee_endpoint(attendee_id: int,
                               db: Session = Depends(get_db),
                               current_user: dict = Depends(get_current_user)):
    
    db_attendee = get_attendee(db, attendee_id)
    if not db_attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")

    
    db_attendee = check_in_attendee(db, attendee_id)
    return db_attendee