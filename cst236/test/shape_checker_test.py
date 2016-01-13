"""
Test for source.shape_checker

name: Zaid Rashid
lab 1 CST 236
"""
from source.shape_checker import get_object_shape__type, get_triangle_type, get_object_shape_type_2
from unittest import TestCase


class TestGetTriangleType(TestCase):
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')


class TestGetObjectType(TestCase):
    def test_get_square_type_square(self):
        result = get_object_shape__type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_square_type_rectangle(self):
        result = get_object_shape__type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_square_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_rectangle_type_2(self):
        result = get_object_shape_type_2(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_rhombus_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 35, 145, 35, 145)
        self.assertEqual(result, 'rhombus')

    def test_get_disconnected_type_2(self):
        result = get_object_shape_type_2(1, 1, 1, 1, 0, 90, 90, 90)
        self.assertEqual(result, 'disconnected')
