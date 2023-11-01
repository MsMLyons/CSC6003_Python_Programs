import unittest
import lyonsm_module_1

class TestCalculations(unittest.TestCase):

    def test_calc_circumference(self):
        result = lyonsm_module_1.calc_circumference()
        self.assertEqual(result, None)

    def test_calc_area(self):
        result = lyonsm_module_1.calc_area()
        self.assertEqual(result, None)

    def test_calc_volume(self):
        result = lyonsm_module_1.calc_volume()
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()