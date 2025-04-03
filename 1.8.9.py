Calculator = []
while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("Q. Quit")

    MenuChoice=input(":")


    if MenuChoice=="1": #Addition
        def Addition(Addition1,Addition2):
            return Addition1 + Addition
        try:
            Addition1 = int (input("Add a number: "))
            Addition2 = int (input("Add another: "))
            print("The number is",(Addition1)+(Addition2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="2": #Subtraction
        def Subtraction(Subtraction1,Subtraction2):
            return Subtraction1 - Subtraction2

        try:
            Subtraction1 = int (input("Enter a number: "))
            Subtraction2 = int (input("What do you want to subtract: "))
            print("The number is",(Subtraction1)-(Subtraction2))
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    elif MenuChoice=="3": #Multiplication
        def Multiplication(Multiplication1,Multiplication2):
            return Multiplication1 * Multiplication2
        try:
            Multiplication1 = int (input("Whats the first number do you want to use: "))
            Multiplication2 = int (input("Whats the second number do you want to use: "))
            print("The number is",(Multiplication1)*(Multiplication2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="4": #Division
        def Division(Division1,Division2):
            return Division1 / Division2
        try:
            Division1 = int (input("Whats the first number do you want to use: "))
            Division2 = int (input("Whats the second number do you want to use: "))
            print("The number is",(Division1)/(Division2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="5": #Exponentiation
        def Exponentiation(Exponentiation1,Exponentiation2):
            return Exponentiation1 ** Exponentiation2
        try:
            Exponentiation1 = int(input("Enter the base number: "))
            Exponentiation2 = int(input("Enter the exponent: "))
            print("The number is",(Exponentiation1)**(Exponentiation2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice=="6": #Square Root
        def Square_Root(Square_Root):
            return Square_Root ** (1/2)
        try:
            Square_Root = int (input("Enter a number: "))
            print("The number is",(Square_Root)**(1/2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif MenuChoice.lower() =="q": #Quit
        break
    
    else:
        print("You sir, didn't use the right choice. Do better!")
    