FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert:"))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

match scale:
    case "C":
        converted_value = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"Temperature in fahrenheit is {converted_value}")

    case "F":
        converted_value = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"Temperature in Celcius is {converted_value}")
    case _:
        print("Invalid temperature. Please enter a numeric value.")