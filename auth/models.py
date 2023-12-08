from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app):
    """ Configuration of the database to store user information """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User(db.Model):
    """ User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
