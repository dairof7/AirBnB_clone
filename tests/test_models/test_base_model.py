#!/usr/bin/python3
"""Unittest for basemodel file: class and methods"""

import pep8
import unittest
from models import base_model
from models.base_model import BaseModel


class Test_Base_Model_outputs(unittest.TestCase):
    """Test_Base_outputs test for Base class"""

    def test_unique_id(self):
        """test_unique_id [summary]

        [extended_summary]
        """
        list_ids = []
        instance1 = BaseModel()
        for i in range(1, 99000):
            list_ids.append(BaseModel().id)
        self.assertEqual(False, instance1.id in list_ids)


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        base_mod = "models/base_model.py"
        test_base_mod = "tests/test_models/test_base_model.py"
        result = style.check_files([base_mod, test_base_mod])
        self.assertEqual(result.total_errors, 0)


class TestDocsBaseModel(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
