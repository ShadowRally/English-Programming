def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("0. End")
    
    menu = input("Choose an option: ")

    if menu == "1":
        celsius = float(input("Please enter the temperature in Celsius: "))
        print(f"{celsius}°C is {to_fahrenheit(celsius):.2f}°F")

    elif menu == "2":
        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {to_celsius(fahrenheit):.2f}°C")

    elif menu == "0":
        break

    else:
        print("Invalid option. Please try again.")

