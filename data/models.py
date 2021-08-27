from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship


class Therapist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    description: Optional[str] = None
    schedule: str
    email: str
    password: str
    created_date: str

    patients: List["Patient"] = Relationship(back_populates="therapist")
    events: List["Event"] = Relationship(back_populates="therapist")

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    age: int
    schedule: str
    email: str
    password: str
    therapist_id: Optional[int] = Field(default=None, foreign_key="therapist.id")
    created_date: str

    therapist: Optional[Therapist] = Relationship(back_populates="patients")
    events: List["Event"] = Relationship(back_populates="patient")

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str] = None
    start_date: str
    end_date: str
    frequency: int
    price_per_session: int
    therapist_id: Optional[int] = Field(default=None, foreign_key="therapist.id")
    patient_id: Optional[int] = Field(default=None, foreign_key="patient.id")
    is_active: bool = True
    created_date: str

    therapist: Optional[Therapist] = Relationship(back_populates="events")
    patient: Optional[Patient] = Relationship(back_populates="events")

class EventHistory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")
    description: Optional[str] = None
    date: str
    status: str
    paid: bool = False
    created_date: str

