import unittest


class Calculator():
    
    def __init__(self):
        pass
    
    def add(self, number1, number2):
        return number1 + number2

    def divide(self, number1, number2):
        if number2 == 0
            return None
        return number1 / number2

class CalculatorTesting(unittest.Testcase):

    calc = Calculator()

    def test_add(self):
        real_value = self.calc.add(4,6)
        expected_value = 10
        self.assertEqual(real_value, expected_value)

    def test_divide(self):
        real_value = self.calc.divide(12,2)
        expected_value = 6
        self.assertEqual(real_value, expected_value)

        real_value = self.calc.divide(12, 0)
        expected_value = None
        self.assertEqual(real_value, expected_value)