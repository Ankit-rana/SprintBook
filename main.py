from flask import Flask
from flask_restful import Api
from base.user_data_handler import UserDataHandler


app = Flask(__name__)
api = Api(app)

api.add_resource(UserDataHandler, '/user/<username>')

if __name__ == "__main__":
    app.run(debug=True)



