from os import environ
from datetime import datetime

from sqlmodel import create_engine, select, Session

from dotenv import load_dotenv
from models import Therapist, Patient, Event, EventHistory

load_dotenv(override=True)

DATABASE = environ.get("DATABASE")
HOST = environ.get("HOST")
PASSWORD = environ.get("PASSWORD")
PORT = environ.get("PORT")
USER = environ.get("USER")
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL, echo=True)


def create_test_data():
    therapist = Therapist(
        name="Viridiana",
        schedule="some json",
        email="viri@gmail.com",
        password="123",
        created_date=str(datetime.now()),
    )
    patient = Patient(
        name="Carmen",
        age=25,
        schedule="some other json",
        email="carmen@gmail.com",
        password="123",
        created_date=str(datetime.now()),
        therapist=therapist
    )

    interview_session = Event(
        start_date=str(datetime.now()),
        end_date=str(datetime.now()),
        frequency=0, # Single event
        price_per_session=400,
        created_date=str(datetime.now()),
        therapist=therapist,
        patient=patient
    )
    
    with Session(engine) as session:
        session.add(interview_session)
        session.commit()
create_test_data()