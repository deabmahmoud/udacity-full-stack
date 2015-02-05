import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    homepage_url = Column(String(255))

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    course_url = Column(String(255))
    course_number = Column(String(20))
    description = Column(String(250))
    perpetual = Column(Boolean, default=False)
    start_date = Column(Date)
    provider_id = Column(Integer, ForeignKey('provider.id'))
    provider = relationship(Provider)

    @property
    def serialize(self):
        """ JSON serializer method """
        return {
            'id': self.id,
            'name': self.name,
            'course_number': self.course_number,
            'description': self.description,
            'perpetual': self.perpetual,
            'start_date': self.start_date,
        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
