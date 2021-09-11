import fastapi
from pytz import common_timezones
router = fastapi.APIRouter()


@router.get('/timezones')
def index():
    return {
        "timezones": common_timezones,
    }
