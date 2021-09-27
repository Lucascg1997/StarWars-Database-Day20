import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name=Column(String, nullable= False)
    _password=Column(String, nullable=False)
    nickname=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    fav = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship("Vehicles")
    specie_id = Column(Integer, ForeignKey('species.id'))
    specie = relationship("Species")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=False)
    diameter=Column(Numeric, nullable=False)
    rotation_period=Column(Numeric, nullable=False)
    orbital_period=Column(Numeric, nullable=False)
    gravity=Column(Numeric, nullable=False)
    population=Column(Numeric, nullable=False)
    climate=Column(String, nullable=False)
    terrain=Column(String, nullable=False)
    surface_water=Column(Numeric, nullable=False)
    create=Column(String, nullable=True)
    edited=Column(String, nullable=True)
    description=Column(String, nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=True)
    model=Column(Numeric, nullable=True)
    manufacturer=Column(Numeric, nullable=True)
    cost_in_credits=Column(String, nullable=True)
    length=Column(String, nullable=True)
    max_atmospheric_speed=Column(String, nullable=True)
    crew=Column(Date, nullable=True)
    passengers=Column(String, nullable=True)
    cargo_capacity=Column(String, nullable=True)
    consumables=Column(String, nullable=True)
    vehicle_class=Column(String, nullable=True)
    pilots= Column(String, nullable=True)
    created=Column(String, nullable=True)
    edited= Column(String, nullable=True)



class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=False)
    classification=Column(String, nullable=False)
    average_height=Column(String, nullable=False)
    skin_colors=Column(String, nullable=False)
    hair_colors=Column(Numeric, nullable=False)
    eye_colors=Column(Numeric, nullable=False)
    average_lifespan=Column(String, nullable=False)
    homeworld=Column(Numeric, nullable=False)
    language=Column(Numeric, nullable=False)
    people=Column(Numeric, nullable=False)
    created=Column(Numeric, nullable=False)
    edited=Column(Numeric, nullable=False)

    


def get_all(): 
    user = User.query.all()   #Select * from customer
    return user


def get_by_id(id): #Select * from customer where id = id
    user = User.query.get(id).one_or_None()
    #customer = Customer.query.filter_by(id = id)
    return user


def get_by_nick(nick):
    user = User.query.filter_by(nick = nick).one_or_None() #Select * from customer where nick = nick
    return user

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')