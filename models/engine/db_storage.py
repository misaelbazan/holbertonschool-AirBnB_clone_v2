#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker, scoped_session
from os import getenv
from models import BaseModel
"""
"""


class DBStorage:
  """
  """
  __engine = None
  __session = None

  def __init__(self):
    hbnb_user = getenv("HBNB_MYSQL_USER")
    hbnb_pass = getenv("HBNB_MYSQL_PWD")
    hbnb_host = getenv("HBNB_MYSQL_HOST")
    hbnb_db = getenv("HBNB_MYSQL_DB")
    hbnb_env = getenv("HBNB_ENV")
    port = 3306
    self.__engine = create_engine(
      f"mysql+mysqldb://{hbnb_user}:{hbnb_pass}@{hbnb_host}:3306/{hbnb_db}", 
      pool_pre_ping=True)
    if hbnb_env = "test":
      base.metadata.drop_all(self.__engine)