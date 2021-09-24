from sqlmodel import Session, select

from data.models import Therapist
from config import engine
from datetime import datetime, time, timedelta
from typing import List
from fastapi_chameleon.engine import response
from starlette import status

from starlette.requests import Request
import fastapi

from infrastructure import cookie_auth
from command.schedule import get_current_therapist_schedule

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

router = fastapi.APIRouter()


def generate_events(schedule: dict, start: datetime, end: datetime, time_zone: str) -> List[str]:
    day = timedelta(hours=24)
    events = []
    week_hours = schedule["week"]
    if time_zone != schedule["timezone"]:
        # TODO: Implement timezone conversion
        return []
    session_duration = timedelta(hours=1)
    while start < end:
        weekday = start.strftime("%A").lower()
        activated = week_hours[weekday]["activated"]
        hours: List[str] = week_hours[weekday]["hours"]

        if activated:
            for available_hours in hours:
                hours_added = timedelta(hours=int(available_hours.split(":")[0]))
                minutes_added = timedelta(minutes=int(available_hours.split(":")[1]))
                start_event = start + hours_added + minutes_added
                end_event = start_event + session_duration
                event = {
                    "title": "Sesión Disponible",
                    "start": start_event.strftime(DATETIME_FORMAT),
                    "end": end_event.strftime(DATETIME_FORMAT)
                }
                events.append(event)
        start += day
    
    return events


@router.get('/events')
def get_user_open_events(start: str, end: str, user_id: str, timeZone: str, user_type: str, request: Request):
    logged_in = cookie_auth.get_email_via_auth_cookie(request)
    if not logged_in:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {}

    start = datetime.strptime(start, DATETIME_FORMAT)
    end = datetime.strptime(end, DATETIME_FORMAT)
    schedule = None
    if user_type == "therapist":
        # First get the therapist email through id
        with Session(engine) as session:
            statement = select(Therapist).where(Therapist.id == user_id)
            results = session.exec(statement)
            therapist = results.first()


        schedule = get_current_therapist_schedule(therapist.email)

    return generate_events(schedule, start, end, timeZone)
