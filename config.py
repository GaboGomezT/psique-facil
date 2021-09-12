from os import environ

from sqlmodel import create_engine

from dotenv import load_dotenv

load_dotenv(override=True)

DATABASE = environ.get("DATABASE")
HOST = environ.get("HOST")
PASSWORD = environ.get("PASSWORD")
PORT = environ.get("PORT")
USER = environ.get("USER")
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL, echo=True)
