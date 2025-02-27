from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.sql import func
from database import Base
from enum import Enum as PyEnum


class EventStatus(str, PyEnum):
    SCHEDULED = "scheduled"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELED = "canceled"
    #RESCHEDULED = "rescheduled"
    
class Event(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    max_attendees = Column(Integer, nullable=False)
    status = Column(Enum(EventStatus), default=EventStatus.SCHEDULED)


class Attendee(Base):
    __tablename__ = "attendees"
    attendee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)
    check_in_status = Column(Boolean, default=False)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)