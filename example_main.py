from flask import Flask
from base.user_data_handler import UserDataHandler


app = Flask(__name__)


@app.route('/')
def Sprint():
   print "Sprint"


if __name__ == "__main__":
    app.run(debug=True)



