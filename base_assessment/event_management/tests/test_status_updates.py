import pytest
from datetime import datetime, timedelta
from crud import create_event, update_event_status
from models import Event
from schemas import EventCreate

def test_automatic_status_update(db):
    
    past_time = datetime.now() - timedelta(hours=1)
    event_data = EventCreate(
        name="Test Event",
        description="Test Description",
        start_time=past_time - timedelta(hours=2),
        end_time=past_time,
        location="Test Location",
        max_attendees=10,
    )
    event = create_event(db, event_data)

    
    update_event_status(db)

    
    updated_event = db.query(Event).filter(Event.event_id == event.event_id).first()
    assert updated_event.status == "completed"