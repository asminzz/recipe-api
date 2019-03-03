from django.test import TestCase
from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """test that two numbers are added"""
        self.assertEqual(add(2,3),5)

    def test_subtract_numbers(self):
        """test that two numbers are subtracted"""
        self.assertEqual(subtract(6,9),3)