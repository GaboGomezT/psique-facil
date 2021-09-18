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
        empty_hours = """{\"activated\": false,\"hours\": []}"""
        schedule = {
            "timezone": None,
            "week": {
                "monday": empty_hours,
                "tuesday": empty_hours,
                "wednesday": empty_hours,
                "thursday": empty_hours,
                "friday": empty_hours,
                "saturday": empty_hours,
                "sunday": empty_hours
            }
        }
    else:
        days = ["monday", "tuesday", "wednesday",
                "thursday", "friday", "saturday", "sunday"]
        for d in days:
            schedule["week"][d] = json.dumps(schedule["week"][d])
    print(f"{schedule=}")
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
        "week": {
            "monday": {
                "activated": True if monday else False,
                "hours": monday_hours
            },
            "tuesday": {
                "activated": True if tuesday else False,
                "hours": tuesday_hours
            },
            "wednesday": {
                "activated": True if wednesday else False,
                "hours": wednesday_hours
            },
            "thursday": {
                "activated": True if thursday else False,
                "hours": thursday_hours
            },
            "friday": {
                "activated": True if friday else False,
                "hours": friday_hours
            },
            "saturday": {
                "activated": True if saturday else False,
                "hours": saturday_hours
            },
            "sunday": {
                "activated": True if sunday else False,
                "hours": sunday_hours
            }
        }
    }

    update_therapist_schedule(therapist_id="1", schedule=schedule)
    days = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]
    for d in days:
        schedule["week"][d] = json.dumps(schedule["week"][d])
    return schedule
