import math
import unittest


def area(r):
    '''
    Вычисляет площадь круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.

    Вычисление площади круга с радиусом 5
    import circle
    area_result = circle.area(5)
    print("Площадь круга:", area_result)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.

    Args:
        r (float): Радиус окружности.

    Returns:
        float: Длина окружности.

    Вычисление длины окружности с радиусом 7
    import circle
    perimeter_result = circle.perimeter(7)
    print("Длина окружности:", perimeter_result)
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_positive_int_values(self):
        res = area(5)
        self.assertAlmostEqual(78.53981633974483, res, places=6, msg="Failed for positive int value")

    def test_area_positive_float_values(self):
        res = area(5.0)
        self.assertAlmostEqual(78.53981633974483, res, places=6, msg="Failed for positive float value")

    def test_area_zero_values(self):
        res = area(0)
        self.assertEqual(0, res, "Failed for zero value")

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5.0)

    def test_area_string_value(self):
        with self.assertRaises(TypeError):
            area("5.0")

    def test_perimeter_positive_int_values(self):
        res = perimeter(7)
        self.assertAlmostEqual(43.982297150257104, res, places=6, msg="Failed for positive float value")

    def test_perimeter_positive_float_values(self):
        res = perimeter(7.0)
        self.assertAlmostEqual(43.982297150257104, res, places=6, msg="Failed for positive float value")

    def test_perimeter_zero_values(self):
        res = perimeter(0)
        self.assertEqual(0, res, "Failed for zero value")

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-7.0)

    def test_perimeter_string_value(self):
        with self.assertRaises(TypeError):
            perimeter("7.0")
