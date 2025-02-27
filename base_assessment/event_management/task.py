from datetime import datetime
from sqlalchemy.orm import Session
from models import Event

def update_event_status(db: Session):
    now = datetime.now()
    events_to_update = db.query(Event).filter(Event.end_time <= now, Event.status != "completed").all()
    for event in events_to_update:
        event.status = "completed"
    db.commit()