from flask import Flask,request
from base.user_data_handler import UserDataHandler


app = Flask(__name__)

@app.route('/')
def welcome_book():
   return "Welcome to Sprint book"

@app.route('/book/',method = ['GET','POST'])
def book_interface():
   if request.method == 'GET':
      user = request.args.get('user','')
      return UserDataHandler.get(user)
   elif request.method == 'POST':
      user = request.args.get('user','')
      bookname = request.args.get('name','')
      description = request.args.get('description','')
      return UserDataHandler.put(user,bookname,description)


if __name__ == "__main__":
    app.run(debug=True)



