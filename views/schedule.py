from command.schedule import get_current_therapist_schedule, update_therapist_schedule
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import json
router = fastapi.APIRouter()


@router.get('/horario-de-disponibilidad')
@template()
def availability(request: Request):
    # When the user system is mature, use request to get user id
    schedule = get_current_therapist_schedule(therapist_id="1")
    if not schedule:
        schedule = {
        "timezone": None,
        "monday": {
            "activated": False,
            "available_hours": []
        },
        "tuesday": {
            "activated": False,
            "available_hours": []
        },
        "wednesday": {
            "activated": False,
            "available_hours": []
        },
        "thursday": {
            "activated": False,
            "available_hours": []
        },
        "friday": {
            "activated": False,
            "available_hours": []
        },
        "saturday": {
            "activated": False,
            "available_hours": []
        },
        "sunday": {
            "activated": False,
            "available_hours": []
        }
    }
    return schedule

@router.post('/horario-de-disponibilidad')
@template()
async def availability(request: Request):
    form = await request.form()
    monday = form.get('monday')
    tuesday = form.get('tuesday')
    wednesday = form.get('wednesday')
    thursday = form.get('thursday')
    friday = form.get('friday')
    saturday = form.get('saturday')
    sunday = form.get('sunday')
    monday_hours = []
    tuesday_hours = []
    wednesday_hours = []
    thursday_hours = []
    friday_hours = []
    saturday_hours = []
    sunday_hours = []
    for hour_id, hour in form.items():
        if "monday_hour" in hour_id:
            monday_hours.append(hour)
        if "tuesday_hour" in hour_id:
            tuesday_hours.append(hour)
        if "wednesday_hour" in hour_id:
            wednesday_hours.append(hour)
        if "thursday_hour" in hour_id:
            thursday_hours.append(hour)
        if "friday_hour" in hour_id:
            friday_hours.append(hour)
        if "saturday_hour" in hour_id:
            saturday_hours.append(hour)
        if "sunday_hour" in hour_id:
            sunday_hours.append(hour)
    timezone = form.get("time-zone-selector")
    schedule = {
        "timezone": timezone,
        "monday": {
            "activated": True if monday else False,
            "available_hours": monday_hours
        },
        "tuesday": {
            "activated": True if tuesday else False,
            "available_hours": tuesday_hours
        },
        "wednesday": {
            "activated": True if wednesday else False,
            "available_hours": wednesday_hours
        },
        "thursday": {
            "activated": True if thursday else False,
            "available_hours": thursday_hours
        },
        "friday": {
            "activated": True if friday else False,
            "available_hours": friday_hours
        },
        "saturday": {
            "activated": True if saturday else False,
            "available_hours": saturday_hours
        },
        "sunday": {
            "activated": True if sunday else False,
            "available_hours": sunday_hours
        }
    }
    update_therapist_schedule(therapist_id="1", schedule=schedule)
    return schedule
