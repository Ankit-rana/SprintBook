from flask import request
from flask_restful import Resource
from pymongo import MongoClient



class UserDataHandler(Resource):

    def __init__(self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client.sprintbook

    def get(self,username):
        data=None
        try:
            data = self.db.books.find_one({"user":username},{'_id':False})
        except :
            exc = "error : connection unsucessfull"
            print exc
            return exc
        return data

    def put(self,username):
        msg=request.form['data']
        print msg
        return {'user':username}
