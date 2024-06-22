from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class TableXXX(Base):
    __tablename__ = 'table_xxx'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class TableZZZ(Base):
    __tablename__ = 'table_zzz'
    id = Column(Integer, primary_key=True, index=True)
    xxx_fk = Column(Integer, ForeignKey('table_xxx.id'))
    xxx = relationship("TableXXX")
