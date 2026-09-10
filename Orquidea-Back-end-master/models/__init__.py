from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from models.base import Base
from models.produto1 import Produto


db_path = "database/"
db_url = f"sqlite:///{db_path}/db.sqlite3"

if not os.path.exists(db_path):
    os.makedirs(db_path)

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(db_url):
    create_database(db_url)

Base.metadata.create_all(engine)