FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
   
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
   
    
temp = float(input("enter a temperature to convert:"))
temp_type = input("is this temperature in celsius or fahrenheit(C/F):").strip().upper()
if temp_type == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp} is {result}")
elif temp_type == "F":
    result = convert_to_celsius(temp)
    print(f"{temp} is {result}")
else:
    print("invalid input")
    

