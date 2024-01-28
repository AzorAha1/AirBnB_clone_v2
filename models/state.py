#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from models.city import City
from sqlalchemy.orm import relationship
from models import hbnb_storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='State', cascade='all, delete-orphan',
            single_parent=True
            )

    @property
    def cities(self):
        """Returns City instances"""
        from models import storage
        from models.city import City
        # all_cities = storage.all(City)
        # return [city for city in all_cities.values()
        #         if city.state_id == self.id]
        listofcity = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                listofcity.append(city)
        return listofcity
