import pytest
from sqlalchemy.orm import Session
from utils import process_csv_for_bulk_check_in
from models import Attendee
from database import SessionLocal

def test_process_csv_for_bulk_check_in():
    
    db = SessionLocal()
    attendees = [
        Attendee(attendee_id=1, first_name="John", last_name="Doe", email="john.doe@example.com", event_id=1),
        Attendee(attendee_id=2, first_name="Jane", last_name="Doe", email="jane.doe@example.com", event_id=1),
    ]
    db.add_all(attendees)
    db.commit()

    
    csv_data = """attendee_id
1
2
"""

   
    process_csv_for_bulk_check_in(csv_data)

   
    attendee1 = db.query(Attendee).filter(Attendee.attendee_id == 1).first()
    attendee2 = db.query(Attendee).filter(Attendee.attendee_id == 2).first()
    assert attendee1.check_in_status is True
    assert attendee2.check_in_status is True

    db.close()