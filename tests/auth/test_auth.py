import unittest

from werkzeug.security import generate_password_hash

from app import app
from auth.models import db, User


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        """ Configure the application for testing """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()
            # Add a test user
            hashed_password = generate_password_hash('testpassword', method='pbkdf2:sha256')
            new_user = User(username='testuser', password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

    def tearDown(self):
        """Clean up after tests """
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_successful_registration(self):
        """ Test successful registration """
        response = self.client.post('/auth/register', json={
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User successfully registered', response.get_data(as_text=True))

    def test_duplicate_username(self):
        """ Test registration with a duplicate username """
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username already exists', response.get_data(as_text=True))

    def test_login_nonexistent_user(self):
        """ Test login with a nonexistent user """
        response = self.client.post('/auth/login', json={
            'username': 'nonexistent',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 401)

    def test_incorrect_password(self):
        """ Test login with incorrect password """
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
