import datetime
import logging

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User

logging.basicConfig(level=logging.INFO)

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint user registration.
    Accepts user credentials (Username - Password)
    Hashes the password, and saves the new user to the database.
    """
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    logging.info(f"New user registered: {data['username']}")
    return jsonify({'message': 'User successfully registered'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
        Endpoint user login.
        Accepts user credentials (Username - Password)
        Checks if the user exists and if the password is correct, then generates an access token.
    """
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        logging.warning('Login attempt with incomplete credentials')
        return make_response('Verification failed', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        logging.warning(f"Login attempt for nonexistent user: {auth.username}")
        return make_response('Verification failed', 401, {'WWW-Authenticate': 'Basic realm="User not found"'})

    if check_password_hash(user.password, auth.password):
        token = create_access_token(identity=auth.username, expires_delta=datetime.timedelta(hours=48))
        logging.info(f"User logged in: {auth.username}")
        return jsonify({'token': token})

    logging.warning(f"Failed login attempt for user: {auth.username} due to incorrect password")
    return make_response('Verification failed', 401, {'WWW-Authenticate': 'Basic realm="Incorrect password"'})
