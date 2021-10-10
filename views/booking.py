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

frequencies = {
    0: "Única",
    1: "Semanal",
    2: "Quincenal",
    3: "Cada tres semanas",
    4: "Mensual"
}

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
@template()
async def confirmation(request: Request):
    form = await request.form()
    therapist_id = form.get("therapist_id")
    date_str = form.get("date_str")
    time_zone = form.get("time_zone")
    session_frequency = form.get("session_frequency")

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
    # TODO: Implement final validation to check if hour is available.
    return {
        "therapist_name": therapist_name,
        "hour_range": hour_range,
        "readable_date": readable_date,
        "time_zone": time_zone,
        "session_frequency": frequencies[int(session_frequency)],
        "link": "https://us04web.zoom.us/j/73860720314?pwd=WEZuNjg2bnpkYVdiVUMvYitwRkNSZz09"
    }
