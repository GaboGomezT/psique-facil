import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(request: Request):
    return {
        "message": "hello world"
    }
