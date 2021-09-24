from infrastructure.auth import login_user, register_user
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status

import json

from infrastructure import cookie_auth
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


@router.post('/iniciar_sesion')
@template()
async def login(request: Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")

    # Check if email and password are valid
    login_error = login_user(email, password, type="therapist")
    print(f"{login_error}")
    if login_error:
        return {
            "password": password,
            "email": email,
            "login_error": login_error,
            "is_logged_in": False
        }

    # Login user
    response = fastapi.responses.RedirectResponse(
        url='/mi_horario', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, email)

    return response


@router.get('/registrar')
@template()
def register_therapist(request: Request):
    is_logged_in = cookie_auth.get_email_via_auth_cookie(request)
    print("is_logged_in: ", is_logged_in)
    return {
        "is_logged_in": is_logged_in
    }


@router.post('/registrar')
@template()
async def register_therapist(request: Request):
    form = await request.form()
    name = form.get('name')
    password = form.get('password')
    email = form.get('email')
    default_price = float(form.get('default_price', 0))

    validation_error = None
    if not name or not name.strip():
        validation_error = "Se requiere tu nombre."
    elif not email or not email.strip():
        validation_error = "Se requiere un correo válido."
    elif not password or len(password) < 5:
        validation_error = "Tu contraseña es requerida y debe ser al menos 5 caracteres."
    elif default_price < 0:
        validation_error = "El costo por sesión no puede ser un número negativo."

    # Create the account
    registration_error = register_user(
        name, email, password, default_price, type="therapist")

    if validation_error or registration_error:
        return {
            "name": name,
            "password": password,
            "email": email,
            "validation_error": validation_error,
            "registration_error": registration_error,
            "is_logged_in": False
        }

    # Login user
    response = fastapi.responses.RedirectResponse(
        url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, email)

    return response
