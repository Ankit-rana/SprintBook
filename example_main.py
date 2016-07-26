from flask import Flask
#from base.user_data_handler import UserDataHandler


app = Flask(__name__)


@app.route('/')
def getBook():
   return "Sprint book recieved"


if __name__ == "__main__":
    app.run(debug=True)



