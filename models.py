from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship

def _get_date():
   return datetime.datetime.now()

Base = declarative_base()


class SprintBook(Base):
   __tablename__ = 'sprintbook'
   __table_args__ = { 'sqlite_autoincrement' : True }
   id = Column(Integer, primary_key = True )
   name = Column(String(40)) 
   user = Column(String(21))
   description = Column(String(80))
   @property
   def serialize(self):
      return {
         'user' : self.user, 
         'bookname' : self.name,
         'description' : self.description,
         'sprints' : [sprint.serialize for sprint in self.sprints]
      }
   sprints = relationship('sprint',lazy="dynamic")
   

class Sprint(Base):
   __tablename__ = 'sprint'
   __table_args__ = {'sqlite_autoincrement': True}
   id = Column(Integer, primary_key = True )
   name = Column(String(40))
   description = Column(String(100))
   start_date = Column(Date, default = _get_date)
   end_date = Column(Date, default=_get_date)
   sprintbook = Column(ForeignKey(SprintBook.id))
   def serialize(self):
       return {
           'sprintname': self.name,
           'description': self.description,
           'start': self.start_date,
           'end': self.end_date,
           'tickets': [ticket.serialize for ticket in self.tickets]
       }
   tickets = relationship('ticket',lazy="dynamic")


class Ticket(Base):
   __tablename__ = 'ticket'
   __table_args__ = {'sqlite_autoincrement': True}
   id = Column(Integer, primary_key = True)
   name = Column(String(40))
   sprint = Column(ForeignKey(Sprint.id))
   def serialize(self):
       return {
           'name': self.name
       }



engine = create_engine('sqlite:///sprintbooks.db')
Base.metadata.create_all(engine)

