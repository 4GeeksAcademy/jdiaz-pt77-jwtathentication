"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required, create_access_token
import hashlib


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def handle_create_user():
    body = request.get_json()
    user_email = body["email"]
    user_password = hashlib.sha256(body['password'].encode("utf-8")).hexdigest()
    user = User(email = user_email, password = user_password)
    db.session.add(user)
    db.session.commit()
    return jsonify("User created")

@api.route('/login', methods=['POST'])
def handle_log_in():
    body = request.get_json()
    user_email = body["email"]
    user_password = hashlib.sha256(body['password'].encode("utf-8")).hexdigest()
    user = User.query.filter_by(email = user_email, password = user_password).first()
    if user and user.password == user_password:
        access_token = create_access_token(identity = user.email)
        return jsonify(access_token = access_token, user = user.serialize())
    else:
        return jsonify("user does not exist")
@api.route('user', methods=['Get'])
@jwt_required()
def handle_get_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(email= user.email, name = user.name)