import logging
import os

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from auth.auth import auth_bp
from auth.models import setup_db
from routes.period import sales_period_bp
from routes.total import total_sales_bp

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

jwt = JWTManager(app)


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """ Response invalid token """
    logging.error(f"Invalid JWT token: {error}")
    return jsonify({'message': 'Invalid token.'}), 401


setup_db(app)

app.register_blueprint(sales_period_bp, url_prefix='/sales_period')
app.register_blueprint(total_sales_bp, url_prefix='/total_sales')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
