import json
import logging

from sqlmodel import Session, select

from data.models import Therapist
from config import engine


def update_therapist_schedule(therapist_id: str, schedule: dict):
    print(f"Updating therapist schedule, {therapist_id=}, {schedule=}")
    with Session(engine) as session:
        statement = select(Therapist).where(Therapist.id == therapist_id)
        results = session.exec(statement)
        therapist = results.one()

        therapist.schedule = json.dumps(schedule)
        session.add(therapist)
        session.commit()
        session.refresh(therapist)

def get_current_therapist_schedule(therapist_id: str):
    print(f"Retrieving therapist schedule, {therapist_id=}")
    with Session(engine) as session:
        statement = select(Therapist).where(Therapist.id == therapist_id)
        results = session.exec(statement)
        therapist = results.one()
        if not therapist:
            logging.warning(f"Therapist with {therapist_id=} does not exist")
            return None
        return json.loads(therapist.schedule) if therapist.schedule else None