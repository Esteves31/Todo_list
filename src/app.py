import bcrypt
from flask import Flask, request, jsonify

from src.externals.bcrypthashservice import BcryptHashService
from src.usecases.signup import SignUp

from test.usecases.inmemoryuserrepository import InMemoryUserRepository

def create_app():
    app = Flask(__name__)
    salt = bcrypt.gensalt()
    hash_service = BcryptHashService(salt)
    user_repo = InMemoryUserRepository()

    @app.route("/api/users", methods = ['POST'])
    def signup():
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        signup_usecase = SignUp(user_repo, hash_service)
        try:
            signup_usecase.perform(name, email, password)
        except Exception as error:
            return jsonify({
                "error": str(error)
            }), 400
        result = { 
            "name": name, 
            "email": email
        }
        return jsonify(result), 201

    return app