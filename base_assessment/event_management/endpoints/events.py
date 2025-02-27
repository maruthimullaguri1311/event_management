from fastapi import APIRouter, Depends, HTTPException,BackgroundTasks
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Event
from schemas import EventCreate, EventResponse, EventUpdate
from crud import create_event, get_event, update_event, delete_event
from authentication import get_current_user
from task import update_event_status
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events/", response_model=EventResponse)
def create_new_event(event: EventCreate,
                     background_tasks:BackgroundTasks,
                     db: Session = Depends(get_db),
                     
                    current_user: dict = Depends(get_current_user)):
        new_event = create_event(db, event)
   
        background_tasks.add_task(update_event_status, db)
        return new_event


@router.get("/events/{event_id}", response_model=EventResponse)
def read_event(event_id: int, 
               db: Session = Depends(get_db),
               current_user: dict = Depends(get_current_user)):
    
    db_event = get_event(db, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.put("/events/{event_id}", response_model=EventResponse)
def update_existing_event(event_id: int,
                          event: EventUpdate, 
                          background_tasks:BackgroundTasks,
                          db: Session = Depends(get_db),
                          current_user: dict = Depends(get_current_user)):
            updated_event = update_event(db, event_id, event)
    
            background_tasks.add_task(update_event_status, db)
            return updated_event
    

# Delete an event
@router.delete("/events/{event_id}")
def delete_existing_event(event_id: int, 
                          db: Session = Depends(get_db), 
                          current_user: dict = Depends(get_current_user)):
    delete_event(db, event_id)
    return {"message": "Event deleted successfully"}