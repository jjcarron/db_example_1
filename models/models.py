from sqlalchemy import Column, Integer, String
from models.base import Extended_Base  # Importer la nouvelle classe de base

Base = Extended_Base
class BaseModel(Base):
    __tablename__ = 'base_model'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __init__(self, name):
        self.name = name

class AnotherBaseModel(Base):
    __tablename__ = 'another_base_model'
    id = Column(Integer, primary_key=True, index=True)
    attribute = Column(String, index=True)

    def __init__(self, attribute):
        self.attribute = attribute
