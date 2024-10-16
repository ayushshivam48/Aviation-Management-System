def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    """Function to convert temperature between Celsius, Fahrenheit, and Kelvin."""
    print("Temperature Converter")
    print("Select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    # Get user input
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        temperature = float(input("Enter the temperature to convert: "))

        # Perform conversion based on user choice
        if choice == '1':
            print(f"{temperature} °C = {celsius_to_fahrenheit(temperature)} °F")
        elif choice == '2':
            print(f"{temperature} °F = {fahrenheit_to_celsius(temperature)} °C")
        elif choice == '3':
            print(f"{temperature} °C = {celsius_to_kelvin(temperature)} K")
        elif choice == '4':
            print(f"{temperature} K = {kelvin_to_celsius(temperature)} °C")
        elif choice == '5':
            print(f"{temperature} °F = {fahrenheit_to_kelvin(temperature)} K")
        elif choice == '6':
            print(f"{temperature} K = {kelvin_to_fahrenheit(temperature)} °F")
    else:
        print("Invalid input! Please select a valid conversion.")

if __name__ == "__main__":
    temperature_converter()
