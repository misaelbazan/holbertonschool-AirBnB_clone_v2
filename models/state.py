#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        from models import storage
        cities = []
        for city in storage.all("City").values():
            if city.state.id == self.id:
                cities.append(city)
        return cities