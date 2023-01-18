#!/usr/bin/python3
"""Unit test for rectangle class."""


import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import 


class TestRectangle(unittest.TestCase):
    """ class test for testing rectangle class """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ check if rectangle is instance of Base and Rect """
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def test_private_width(self):
        """ check if private var width is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_private_height(self):
        """ check if private var height is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__height

    def test_private_x(self):
        """ check if private var x is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__x

    def test_private_y(self):
        """ check if private var y is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__y
