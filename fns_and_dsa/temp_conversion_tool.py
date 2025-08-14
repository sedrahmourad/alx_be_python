
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    temp = float(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temp_type == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif temp_type == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError as e:
    print(f"Invalid temperature. Please enter a numeric value. ({e})")
