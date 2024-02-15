#!/usr/bin/python3
"""Unittest module for Class Solution"""

from datetime import datetime
import unittest
import pep8
import models
import time
from models.solution import Solution


class TestSolutionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Solution class"""

    def test_pep8_conformance(self):
        """Test that models/solution.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/solution.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violation found")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        doc = models.solution.__doc__
        self.assertIsNot(doc, None, "solution.py not documented")
        self.assertTrue(len(doc) > 5, 'solution.py not properly documented')

    def test_class_docstring(self):
        """Test for the Solution class docstring"""
        self.assertIsNot(Solution.__doc__, None,
                         "Solution Class not documented")
        self.assertTrue(len(Solution.__doc__) > 5,
                        "Solution Class not documented")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in Solution methods"""
        self.assertIsNot(Solution.__init__.__doc__, None,
                         "Solution __init__ method not documented")
        self.assertTrue(len(Solution.__init__.__doc__) > 5,
                        "Solution __init__ method not documented")
        self.assertIsNot(Solution.to_dict.__doc__, None,
                         "Solution to_dict method not documented")
        self.assertTrue(len(Solution.to_dict.__doc__) > 5,
                        "Solution to_dict method not documented")


class TestSolution(unittest.TestCase):
    """Test the Solution class"""
    def test_instantiation(self):
        """Test that object is of type"""
        model = Solution()
        self.assertIs(type(model), Solution)

    def test_instance_attributes(self):
        """Test that object has expected attributes"""
        model = Solution()
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
        """Test that two Solution instances have different datetime objects
        and attributes
        """
        start = datetime.utcnow()
        model = Solution()
        stop = datetime.utcnow()
        self.assertTrue(start <= model.created_at <= stop)
        time.sleep(1)
        start = datetime.utcnow()
        model_2 = Solution()
        stop = datetime.utcnow()
        self.assertTrue(start <= model_2.created_at <= stop)
        self.assertNotEqual(model.created_at, model_2.created_at)
        self.assertNotEqual(model.updated_at, model_2.updated_at)
        self.assertNotEqual(model.id, model_2.id)

        def test_to_dict_values(self):
            """test that values in dict returned from to_dict are correct"""
            formats = "%Y-%m-%dT%H:%M:%S.%f"
            model = Solution()
            test = model.to_dict()
            self.assertEqual(test["__class__"], "Solution")
            self.assertEqual(type(test["created_at"]), str)
            self.assertEqual(type(test["updated_at"]), str)
            self.assertEqual(test["created_at"],
                             model.created_at.strftime(t_format))
            self.assertEqual(test["updated_at"],
                             model.created_at.strftime(t_format))


if __name__ == '__main__':
    unittest.main()
