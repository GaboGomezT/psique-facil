import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import json
router = fastapi.APIRouter()


@router.get('/horario-de-disponibilidad')
@template()
def availability(request: Request):
    return {
        "available_dates": json.dumps({
            "2021-08-14": False,
            "2021-08-15": False,
            "2021-08-16": True,
            "2021-08-17": True
        })
        
    }

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
    sunday = form.get('wednesday')
    print(monday, tuesday, wednesday, thursday, friday, saturday, sunday)

    return {
        "available_dates": json.dumps({
            "2021-08-14": False,
            "2021-08-15": False,
            "2021-08-16": True,
            "2021-08-17": True
        })
        
    }
