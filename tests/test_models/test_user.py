#!/usr/bin/python3
"""Unittest module for Class User"""

from datetime import datetime
import unittest
import pep8
import models
import time
from models.user import User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    def test_pep8_conformance(self):
        """Test that models/user.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violation found")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        doc = models.user.__doc__
        self.assertIsNot(doc, None, "user.py not documented")
        self.assertTrue(len(doc) > 5, 'user.py not properly documented')

    def test_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User Class not documented")
        self.assertTrue(len(User.__doc__) > 5,
                        "User Class not documented")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        self.assertIsNot(User.__init__.__doc__, None,
                         "User __init__ method not documented")
        self.assertTrue(len(User.__init__.__doc__) > 5,
                        "User __init__ method not documented")
        self.assertIsNot(User.to_dict.__doc__, None,
                         "User to_dict method not documented")
        self.assertTrue(len(User.to_dict.__doc__) > 5,
                        "User to_dict method not documented")


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_instantiation(self):
        """Test that object is of type"""
        model = User()
        self.assertIs(type(model), User)

    def test_instance_attributes(self):
        """Test that object has expected attributes"""
        model = User()
        model.name = 'test'
        types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            'name': str
            }
        self.assertEqual(model.name, "test")

        for key, typ in types.items():
            with self.subTest(key=key, typ=typ):
                self.assertIn(key, model.__dict__)
                self.assertIs(type(model.__dict__[key]), typ)

    def test_attributes(self):
        """Test that two User instances have different datetime objects
        and attributes
        """
        start = datetime.utcnow()
        model = User()
        stop = datetime.utcnow()
        self.assertTrue(start <= model.created_at <= stop)
        time.sleep(1)
        start = datetime.utcnow()
        model_2 = User()
        stop = datetime.utcnow()
        self.assertTrue(start <= model_2.created_at <= stop)
        self.assertNotEqual(model.created_at, model_2.created_at)
        self.assertNotEqual(model.updated_at, model_2.updated_at)
        self.assertNotEqual(model.id, model_2.id)

        def test_to_dict_values(self):
            """test that values in dict returned from to_dict are correct"""
            formats = "%Y-%m-%dT%H:%M:%S.%f"
            model = User()
            test = model.to_dict()
            self.assertEqual(test["__class__"], "User")
            self.assertEqual(type(test["created_at"]), str)
            self.assertEqual(type(test["updated_at"]), str)
            self.assertEqual(test["created_at"],
                             model.created_at.strftime(t_format))
            self.assertEqual(test["updated_at"],
                             model.created_at.strftime(t_format))


if __name__ == '__main__':
    unittest.main()
