CELCIUS = "celcius"
KELVIN = "kelvin"

def kelvinToCelciusOrCelciusToCelvinConversion(temperature, formula):
    '''
        This function is used to convert temperature from kelvin to celcius or the contrary.
        :param temperature: Input temperature | int or float
        :param formula: Input kelvin to celcius formula or the contrary | lambda
        
        :return: formula(temperature): result of calculation from formula with temperature as the argument of lambda | int or float
    '''
    return formula(temperature)

def toFahrenheit(temperature, fromTemp = CELCIUS):
    '''
        This function is used to convert temperature from celcius to fahrenheit or kelvin to fahrenheit.
        :param temperature: Input temperature | int or float
        :param formula: Input indicates origin temperature type | string
  
        :return: result: result of calculation from conversion formula based on origin temperature type | int or float
    '''
    return f"{round((temperature * 9/5) + 32, 2)} F" if (fromTemp == CELCIUS) else f"{round((temperature - 273.15) * 9/5 + 32, 2)} F"
        
def fromFahrenheit(temperature, toTemp = CELCIUS):
    '''
        This function is used to convert temperature from fahrenheit to celcius or fahrenheit to kelvin.
        :param temperature: Input temperature | int or float
        :param formula: Input indicates result temperature type | string
  
        :return: result: result of calculation from conversion formula based on result temperature type | int or float
    '''
    return f"{round((temperature - 32) * 5/9, 2)} C" if (toTemp == CELCIUS) else f"{round((temperature - 32) * 5/9 + 273.15, 2)} K"

kelvinToCelciusFormula = lambda temperature: f"{round(temperature - float(273.15), 2)} C"
CelciusToKelvinFormula = lambda temperature: f"{round(temperature + float(273.15), 2)} K"

temperature = 100

print("\n=== TO FAHRENHEIT CONVERSION ====")
print(f"CELCIUS TO FAHRENHEIT: {toFahrenheit(temperature)}")
print(f"KELVIN TO FAHRENHEIT: {toFahrenheit(temperature, KELVIN)}")

print("\n=== FROM FAHRENHEIT CONVERSION ====")
print(f"FAHRENHEIT TO CELCIUS: {fromFahrenheit(temperature)}")
print(f"FAHRENHEIT TO KELVIN: {fromFahrenheit(toTemp = KELVIN, temperature = temperature)}")

print("\n=== KELVIN TO CELCIUS OR CELCIUS TO KELVIN CONVERSION ====")
print(f"KELVIN TO CELCIUS: {kelvinToCelciusOrCelciusToCelvinConversion(temperature, kelvinToCelciusFormula)}")
print(f"CELCIUS TO KELVIN: {kelvinToCelciusOrCelciusToCelvinConversion(temperature, CelciusToKelvinFormula)}")