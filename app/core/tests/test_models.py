from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@astromeen.com'
        password = 'testpassword'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """Test the email for a new user is normalized"""

        email = 'test@ASTROMEEN.COM'

        user = get_user_model().objects.create_user(email,'abcd')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test for an invalid email"""

        with self.assertRaise(ValueError):
            user = get_user_model().objects.create_user(None, 'test123')