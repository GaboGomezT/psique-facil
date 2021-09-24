import json
import logging

from sqlmodel import Session, select

from data.models import Therapist
from config import engine


def update_therapist_schedule(therapist_email: str, schedule: dict):
    print(f"Updating therapist schedule, {therapist_email=}, {schedule=}")
    with Session(engine) as session:
        statement = select(Therapist).where(Therapist.email == therapist_email)
        results = session.exec(statement)
        therapist = results.first()

        therapist.schedule = json.dumps(schedule)
        session.add(therapist)
        session.commit()
        session.refresh(therapist)

def get_current_therapist_schedule(therapist_email: str):
    print(f"Retrieving therapist schedule, {therapist_email=}")
    with Session(engine) as session:
        statement = select(Therapist).where(Therapist.email == therapist_email)
        results = session.exec(statement)
        therapist = results.first()
        if not therapist:
            logging.warning(f"Therapist with {therapist_email=} does not exist")
            return None
        return json.loads(therapist.schedule) if therapist.schedule else None