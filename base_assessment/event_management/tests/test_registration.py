import pytest
from crud import create_event, create_attendee
from models import Event, Attendee
from schemas import EventCreate, AttendeeCreate

def test_registration_limit(db):
    
    event_data = EventCreate(
        name="Test Event",
        description="Test Description",
        start_time="2023-10-01T10:00:00",
        end_time="2023-10-01T12:00:00",
        location="Test Location",
        max_attendees=1,
    )
    event = create_event(db, event_data)

    
    attendee1_data = AttendeeCreate(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        event_id=event.event_id,
    )
    attendee1 = create_attendee(db, attendee1_data)
    assert attendee1 is not None

    
    attendee2_data = AttendeeCreate(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        event_id=event.event_id,
    )
    with pytest.raises(Exception):  # Expect an exception
        create_attendee(db, attendee2_data)