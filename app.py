import os
from flask import Flask
from flask_jwt_extended import JWTManager
from models import setup_db
from auth import auth_bp
from views import sales_bp

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

jwt = JWTManager(app)

setup_db(app)

app.register_blueprint(sales_bp, url_prefix='/sales')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
