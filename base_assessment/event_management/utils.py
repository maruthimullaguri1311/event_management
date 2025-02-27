import csv
from io import StringIO
from typing import List
from sqlalchemy.orm import Session
from crud import check_in_attendee

def process_csv_for_bulk_check_in(db: Session, csv_data: str):
    
    
    reader = csv.DictReader(StringIO(csv_data))
    for row in reader:
        attendee_id = int(row["attendee_id"])
       
        check_in_attendee(db, attendee_id)