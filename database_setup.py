import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Job(Base):

    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    role = Column(String(10), nullable=False)
    description = Column(String(250))
    img = Column(String(250))
    author = Column(String(80), nullable=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id
            }


class Ability(Base):
    __tablename__ = 'ability'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    Cast = Column(String(250))
    description = Column(String(250))
    level = Column(Integer)
    job_id = Column(Integer, ForeignKey('job.id'))
    job = relationship(Job)
    author = Column(String(80), nullable=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'level': self.level,
            'Cast': self.Cast,
            }

engine = create_engine('sqlite:///ff14jobs.db')

Base.metadata.create_all(engine)
