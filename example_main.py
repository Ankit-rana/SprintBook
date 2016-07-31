from flask import Flask,request
from user_data_handler import UserDataHandler


app = Flask(__name__)

@app.route('/')
def welcome_book():
   return "Welcome to Sprint book"

@app.route('/user/<user>',methods = ['GET','POST'])
def book_interface(user):
   print user
   handler = UserDataHandler()
   if request.method == 'GET':
      return handler.get(user)
   elif request.method == 'POST':
      bookname = request.args.get('name','')
      description = request.args.get('description','')
      return handler.put(user,bookname,description)


if __name__ == "__main__":
    app.run(debug=True)



