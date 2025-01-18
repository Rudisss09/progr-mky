import time

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    elif from_unit == "Celsius":
        celsius = value
    else:
        return None

    if to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    elif to_unit == "Celsius":
        return celsius
    else:
        return None

def getValues():
    value = float(input("Zadejte hodnotu teploty: "))

    from_unit = input("Zadejte typ (Celsius, Fahrenheit, Kelvin): ")
    to_unit = input("Zadejte typ na který to chcete přeložit (Celsius, Fahrenheit, Kelvin): ")

    result = convert_temperature(value, from_unit, to_unit)

    if result is not None:
        print(value, from_unit, "se rovná", result, to_unit)
        time.sleep(2)
        getValues()
    else:
        print("Neznámé jednotky, zkuste prosím znovu")
        getValues()

getValues()