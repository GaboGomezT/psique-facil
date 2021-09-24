from datetime import datetime
from sqlmodel import Session, select

from data.models import Therapist, Patient
from config import engine
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

def register_user(name: str, email:str, password: str, type: str,  default_price: float = None,  therapist_id: str = None):
    # first check if the user already exists
    if type == "therapist":
        with Session(engine) as session:
            statement = select(Therapist).where(Therapist.email == email)
            results = session.exec(statement)
            if results.first():
                return "Este correo ya existe"
            
            therapist = Therapist(
                name=name,
                email=email,
                password=crypto.hash(password, rounds=172_434),
                default_price=default_price,
                created_date=str(datetime.now()),
            )
            session.add(therapist)
            session.commit()
            return None
    elif type == "patient":
        with Session(engine) as session:
            statement = select(Patient).where(Patient.email == email)
            results = session.exec(statement)

            if results.first():
                return "Este correo ya existe"
            
            patient = Patient(
                name=name,
                email=email,
                password=crypto.hash(password, rounds=172_434),
                therapist_id=therapist_id,
                created_date=str(datetime.now()),
            )
            session.add(patient)
            session.commit()
            return None


def login_user(email:str, password: str, type: str):
    # first check if the user already exists
    existing_user = None
    if type == "therapist":
        with Session(engine) as session:
            statement = select(Therapist).where(Therapist.email == email)
            results = session.exec(statement)
            existing_user = results.first()
    elif type == "patient":
        with Session(engine) as session:
            statement = select(Patient).where(Patient.email == email)
            results = session.exec(statement)
            existing_user = results.first()
    if not existing_user:
        return "Este correo no existe"
    
    if not crypto.verify(password, existing_user.password):
        return "Wrong password"
    return None

