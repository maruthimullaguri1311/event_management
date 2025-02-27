import pytest
from crud import create_event, create_attendee, check_in_attendee
from models import Event, Attendee
from schemas import EventCreate, AttendeeCreate

def test_check_in_attendee(db):
    
    event_data = EventCreate(
        name="Test Event",
        description="Test Description",
        start_time="2023-10-01T10:00:00",
        end_time="2023-10-01T12:00:00",
        location="Test Location",
        max_attendees=10,
    )
    event = create_event(db, event_data)

    
    attendee_data = AttendeeCreate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        event_id=event.event_id,
    )
    attendee = create_attendee(db, attendee_data)

   
    checked_in_attendee = check_in_attendee(db, attendee.attendee_id)
    assert checked_in_attendee.check_in_status is True