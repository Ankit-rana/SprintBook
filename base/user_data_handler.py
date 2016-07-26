from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.models import Base, SprintBook 

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class UserDataHandler():
'''This class is maintained to put data in sprintbook table or get the data from the database for a particular user'''
    def get(self,username):
        book = None
        try:
            book = session.query(SprintBook).filter_by(name=username).one()
        except :
            exc = "error : connection unsucessfull"
            return exc
        return book

    def put(self,username,bookname,description):
        book = session.query(SprintBook).filter_by(name = username).one()
        if not bookname:
           book.user = username
        if not username:
           book.name = bookname
        if not description:
           book.description = description
        session.add(SprintBook)
        session.commit()
        return "Updated a SprintBook: %s" % bookname
