from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, SprintBook 
from flask import jsonify

engine = create_engine('sqlite:///sprintbooks.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class UserDataHandler():
    '''This class is maintained to put data in sprintbook table or get the data from the database for a particular user'''
    def get(self,username):
        book = None
        try:
            book = session.query(SprintBook).filter_by(user=username).one()
        except Exception as exc:
            return exc
        return jsonify(Book=book.serialize)
    def put(self,username,bookname,description):
        book = SprintBook(user=username,name=bookname,description=description)
        session.add(book)
        session.commit()
        return "Updated a SprintBook: %s" % bookname
