import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
import json
router = fastapi.APIRouter()


@router.get('/')
@template()
def index(request: Request):
    return {
        "message": "hello world",
        "available_dates": json.dumps({
            "2021-08-14": False,
            "2021-08-15": False,
            "2021-08-16": True,
            "2021-08-17": True
        })

    }

@router.get('/iniciar_sesion')
@template()
def login(request: Request):
    return {}
