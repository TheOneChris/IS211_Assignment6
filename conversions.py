"Conversion for Celcius to Kelvins"
def convertCelsiusToKelvin(celsius):
    con_kelvin = float(celsius) + 273.15
    return con_kelvin

"Conversion for Celcius to fahrenheit"
def convertCelsiusToFahrenheit(celsius):
        con_fahrenheit = float(celsius) * 9 / 5 + 32
        return con_fahrenheit


"Conversion for Fahrenheit to Celcius"
def convertFahrenheitToCelsius(fahrenheit):
    con_celsius = (float(fahrenheit) - 32) * 5 / 9
    return con_celsius

"Conversion for Fahrenheit to Kelvins"
def convertFahrenheitToKelvin(fahrenheit):
    con_kelvin = (float(fahrenheit) + 459.67) * 5 / 9
    return con_kelvin

"Conversion for Kelvins to Celcius"
def convertKelvinToFahrenheit(kelvin):
    con_fahrenheit = float(kelvin) * 9 / 5 - 459.67
    return con_fahrenheit

"Conversion for Kelvins to Fahrenheit"
def convertKelvinToCelsius(kelvin):
    con_celsius = float(kelvin) - 273.15
    return con_celsius