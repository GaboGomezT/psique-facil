from os import environ

from sqlmodel import create_engine

from dotenv import load_dotenv
from deta import Deta  # Import Deta


load_dotenv(override=True)

DATABASE = environ.get("DATABASE")
HOST = environ.get("HOST")
PASSWORD = environ.get("PASSWORD")
PORT = environ.get("PORT")
USER = environ.get("USER")
DETA_PROJECT_KEY = environ.get("DETA_PROJECT_KEY")
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)

deta = Deta(DETA_PROJECT_KEY)
email_db = deta.Base("psique_facil_emails")