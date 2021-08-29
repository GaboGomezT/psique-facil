import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
router = fastapi.APIRouter()


@router.get('/agenda')
@template()
def calendar(request: Request):
    return {
        
    }
