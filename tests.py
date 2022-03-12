import unittest
import conversions
import conversions_refactored

class Test_Conversions(unittest.TestCase):

    def test_CelsiusToKelvin(self):
        result = conversions.convertCelsiusToKelvin(300.00)
        self.assertAlmostEqual(result, 573.15)

    def test_CelsiusToFahrenheit(self):
        result = conversions.convertCelsiusToFahrenheit(300.00)
        self.assertAlmostEqual(result, 572.00)

    def test_FahrenheitToCelsius(self):
        result = conversions.convertFahrenheitToCelsius(572.00)
        self.assertAlmostEqual(result, 300.00)

    def test_FahrenheitToKelvin(self):
        result = conversions.convertFahrenheitToKelvin(572.00)
        self.assertAlmostEqual(result, 573.15)

    def test_KelvinToCelsius(self):
        result = conversions.convertKelvinToCelsius(573.15)
        self.assertAlmostEqual(result, 300.00)

    def test_KelvinToFahrenheit(self):
        result = conversions.convertKelvinToFahrenheit(573.15)
        self.assertAlmostEqual(result, 572.00)


class TestConversions(unittest.TestCase):

    def test_CelsiusToKelvin(self):
        result = round(conversions_refactored.convert("Celsius", "Kelvin", 300.00), 4)
        self.assertEqual(result, 573.1500)

    def test_CelsiusToFahrenheit(self):
        result = round(conversions_refactored.convert("Celsius", "Fahrenheit", 300.00), 4)
        self.assertEqual(result, 572.00)

    def test_FahrenheitToCelsius(self):
        result = round(conversions_refactored.convert("Fahrenheit", "Celsius", 572.00), 4)
        self.assertEqual(result, 300.0000)

    def test_FahrenheitToKelvin(self):
        result = round(conversions_refactored.convert("Fahrenheit", "Kelvin", 572.00), 4)
        self.assertEqual(result, 573.1500)

    def test_KelvinToCelsius(self):
        result = round(conversions_refactored.convert("Kelvin", "Celsius", 573.15), 4)
        self.assertEqual(result, 300.0000)

    def test_KelvinToFahrenheit(self):
        result = round(conversions_refactored.convert("Kelvin", "Fahrenheit", 573.15), 4)
        self.assertEqual(result, 572.0000)

    def test_MilesToMeters(self):
        result = round(conversions_refactored.convert("Miles", "Meters", 2.00), 4)
        self.assertEqual(result, 3218.6880)

    def test_MilesToYards(self):
        result = round(conversions_refactored.convert("Miles", "Yards", 2.00), 4)
        self.assertEqual(result, 3520.0000)

    def test_YardsToMiles(self):
        result = round(conversions_refactored.convert("Yards", "Miles", 3520.00), 4)
        self.assertEqual(result, 2.0000)

    def test_YardsToMeters(self):
        result = round(conversions_refactored.convert("Yards", "Meters", 2.00), 4)
        self.assertEqual(result, 1.8282)

    def test_MetersToMiles(self):
        result = round(conversions_refactored.convert("Meters", "Miles", 2.00), 4)
        self.assertEqual(result, 0.0012)

    def test_MetersToYards(self):
        result = round(conversions_refactored.convert("Meters", "Yards", 2.00), 4)
        self.assertEqual(result, 2.1880)

    def test_SameUnit(self):
        result = round(conversions_refactored.convert("Yards", "Yards", 2.00), 4)
        self.assertEqual(result, 2.0000)

    def test_ConversionNotPossible(self):
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, "Yards", "Kelvin", 2.00)

if __name__ == '__main__':
    unittest.main()
