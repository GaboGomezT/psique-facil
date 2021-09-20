from datetime import datetime, time, timedelta
from typing import List
from command.schedule import get_current_therapist_schedule
import fastapi

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

router = fastapi.APIRouter()


def generate_events(schedule: dict, start: datetime, end: datetime) -> List[str]:
    day = timedelta(hours=24)
    events = []
    week_hours = schedule["week"]
    session_duration = timedelta(hours=1)
    while start < end:
        weekday = start.strftime("%A").lower()
        activated = week_hours[weekday]["activated"]
        hours = week_hours[weekday]["hours"]

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
                print(event)
        start += day
    
    return events


@router.get('/events')
def get_user_open_events(start: str, end: str, user_id: str, timeZone: str, user_type: str):
    # TODO: Use cookies to get user_id to protect this API, or find another way to protect it.
    print(f"{start=}, {end=}, {user_id=}, {timeZone=}")
    start = datetime.strptime(start, DATETIME_FORMAT)
    end = datetime.strptime(end, DATETIME_FORMAT)
    print(f"{start=}, {end=}, {user_id=}, {timeZone=}")
    schedule = None
    if user_type == "therapist":
        schedule = get_current_therapist_schedule(user_id)

    return generate_events(schedule, start, end)
