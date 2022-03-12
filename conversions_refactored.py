class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    if fromUnit == "Celsius" and toUnit == "Kelvin":
        return value + 273.15
    if fromUnit == "Celsius" and toUnit == "Fahrenheit":
        return ((value * (9.0 / 5.0)) + 32)
    if fromUnit == "Fahrenheit" and toUnit == "Celsius":
        return ((value - 32) * (5.0 / 9.0))
    if fromUnit == "Fahrenheit" and toUnit == "Kelvin":
        return (((value - 32) * (5.0 / 9.0)) + 273.15)
    if fromUnit == "Kelvin" and toUnit == "Celsius":
        return value - 273.15
    if fromUnit == "Kelvin" and toUnit == "Fahrenheit":
        return ((value - 273.15) * (9.0 / 5.0) + 32)
    if fromUnit == "Miles" and toUnit == "Yards":
        return value * 1760.00
    if fromUnit == "Miles" and toUnit == "Meters":
        return value * 1609.344
    if fromUnit == "Yards" and toUnit == "Miles":
        return value / 1760.00
    if fromUnit == "Yards" and toUnit == "Meters":
        return value / 1.094
    if fromUnit == "Meters" and toUnit == "Miles":
        return value / 1609.344
    if fromUnit == "Meters" and toUnit == "Yards":
        return value * 1.094
    raise ConversionNotPossible("Conversion from " + fromUnit + " to " + toUnit + " is not possible")
