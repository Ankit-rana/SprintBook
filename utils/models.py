from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date


def _get_date():
   return datetime.datetime.now()

Base = declarative_base()


class SprintBook(Base):
   __tablename__ = 'sprintbook'
   id = Column(Integer, primary_key = True )
   name = Column(String(40)) 
   user = Column(String(21))
   description = Column(String(80))
   

class Sprint(Base):
   __tablename__ = 'sprint'
   id = Column(Integer, primary_key = True )
   name = Column(String(40))
   description = Column(String(100))
   start_date = Column(Date, default = _get_date)
   end_date = Column(Date, default=_get_date)
   sprintbook = Column(ForeignKey(SprintBook.id))


class Ticket(Base):
   __tablename__ = 'ticket'
   id = Column(Integer, primary_key = True)
   name = Column(String(40))
   sprint = Column(ForeignKey(Sprint.id))


engine = create_engine('sqlite:///sprintbooks.db')
Base.metadata.create_all(engine)

