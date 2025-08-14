FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = input("Enter the temperature to convert: ")
if isinstance(temp, float):
    temp = float(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if temp_type == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
elif temp_type == "F":
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
else:
    print("invalid temp type")



