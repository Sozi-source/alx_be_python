FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
   return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_f = float(input("Enter temperature in fahreheit: "))
print(f"In Celcius: ", convert_to_celsius(temp_f))

temp_c = float(input("Enter temperature in Celcius: "))
print(f"In fahrenheit: ", convert_to_fahrenheit(temp_c))