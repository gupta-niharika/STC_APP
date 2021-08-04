from flask import Flask, jsonify
from flask_bcrypt import Bcrypt     
from database.db import initialize_db
from flask_restful import Api       
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from resources.errors import errors

app = Flask(__name__)
#app.config.from_envvar('ENV_FILE_LOCATION')     
    # set ENV_FILE_LOCATION=./.env   <- set the file path with this
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False          #token wont expire at all now
app.config['JWT_SECRET_KEY'] = 'BhakkBC'
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

#atlas connected with IP 0.0.0.0 /  
#python driver version = 3.4+       
app.config['MONGODB_HOST'] = 'mongodb://admin:admin@cluster0-shard-00-00-iim6b.mongodb.net:27017,cluster0-shard-00-01-iim6b.mongodb.net:27017,cluster0-shard-00-02-iim6b.mongodb.net:27017/MSTC?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
# app.config['MONGODB_DB'] = not mentioned here
initialize_db(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run()