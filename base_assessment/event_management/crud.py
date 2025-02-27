
from sqlalchemy.orm import Session
from models import Event, Attendee,User
from schemas import EventCreate, EventUpdate, AttendeeCreate ,UserCreate # Import schemas
from passlib.context import CryptContext


pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')


def create_event(db: Session, event: EventCreate):  # Use EventCreate from schemas
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.event_id == event_id).first()

def update_event(db: Session, event_id: int, event: EventUpdate):  # Use EventUpdate from schemas
    db_event = get_event(db, event_id)
    if db_event:
        for key, value in event.model_dump(exclude_unset=True).items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event


def create_attendee(db: Session, attendee: AttendeeCreate):  # Use AttendeeCreate from schemas
    db_attendee = Attendee(**attendee.model_dump())
    db.add(db_attendee)
    db.commit()
    db.refresh(db_attendee)
    return db_attendee

def get_attendee(db: Session, attendee_id: int):
    return db.query(Attendee).filter(Attendee.attendee_id == attendee_id).first()

def check_in_attendee(db: Session, attendee_id: int):
    db_attendee = get_attendee(db, attendee_id)
    if db_attendee:
        db_attendee.check_in_status = True
        db.commit()
        db.refresh(db_attendee)
    return db_attendee
def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()