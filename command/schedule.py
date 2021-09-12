import json
import logging

from sqlmodel import Session, select

from data.models import Therapist
from config import engine


def update_schedule(therapist_id: str, schedule: dict):
    logging.info(f"Updating therapist schedule, {therapist_id=}, {schedule=}")
    with Session(engine) as session:
        statement = select(Therapist).where(Therapist.id == therapist_id)
        results = session.exec(statement)
        therapist = results.one()

        therapist.schedule = json.dumps(schedule)
        session.add(therapist)
        session.commit()
        session.refresh(therapist)
