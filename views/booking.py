from datetime import datetime, timedelta
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from sqlmodel import Session, select

from data.models import Therapist
from config import engine
from sqlalchemy.exc import NoResultFound
# import locale
# locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

router = fastapi.APIRouter()


@router.get('/agenda')
@template()
def calendar(request: Request):
    return {

    }


@router.get('/agenda_sesion/therapist/{therapist_id}/date_time/{date_str}/time_zone/{time_zone}')
@template()
def book_session(therapist_id: str, date_str: str, time_zone: str, request: Request):
    time_zone = time_zone.replace("*", "/")
    try:
        with Session(engine) as session:
            statement = select(Therapist).where(Therapist.id == therapist_id)
            results = session.exec(statement)
            therapist = results.one()
            therapist_name = therapist.name
    except NoResultFound as no_result:
        # TODO: add log
        therapist_name = None

    date: datetime = datetime.strptime(date_str, DATETIME_FORMAT)
    hour_range = f"{date.strftime('%I:%M %p')} - {(date + timedelta(hours=1)).strftime('%I:%M %p')}"
    readable_date = date.strftime("%d/%m/%Y")
    return {
        "therapist_name": therapist_name,
        "hour_range": hour_range,
        "readable_date": readable_date,
        "therapist_id": therapist_id,
        "date_str": date_str,
        "time_zone": time_zone
    }


@router.post('/agenda_sesion/confirmacion')
def confirmation(request: Request):
    time_zone = time_zone.replace("*", "/")
    try:
        with Session(engine) as session:
            statement = select(Therapist).where(Therapist.id == therapist_id)
            results = session.exec(statement)
            therapist = results.one()
            therapist_name = therapist.name
    except NoResultFound as no_result:
        # TODO: add log
        therapist_name = None

    date: datetime = datetime.strptime(date, DATETIME_FORMAT)
    hour_range = f"{date.strftime('%I:%M %p')} - {(date + timedelta(hours=1)).strftime('%I:%M %p')}"
    readable_date = date.strftime("%d/%m/%Y")
    return {
        "therapist_name": therapist_name,
        "hour_range": hour_range,
        "date": readable_date,
        "time_zone": time_zone
    }
