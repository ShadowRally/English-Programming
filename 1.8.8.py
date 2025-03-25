def to_fahrenheit(Celsius):
    return (Celsius * 9/5) + 32

def to_celsius (Fahrenheit):
    return (Fahrenheit - 32) * 5/9



while True:
    print("1. Celsius to Fahrenheit ")
    print("2. Fahrenheit to Celsius ")
    print("0. End")
    
    menu=input(":")

    if menu=="1":
        Celsius = float (input("Please enter how many degrees of Celsius you want to change: "))
        print(to_fahrenheit(Celsius))

    elif menu=="2":
        Fahrenheit = float (input("Please enter how many degrees of Fahrenheit you want to change: "))
        print(to_celsius(Fahrenheit))

    elif menu=="0":
        break