def calculator():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter a second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        print('''Choose operation:
        * 
        + 
        -
        / 
        exit = Exit from the program''')
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '+':
            print(f"The result of {num1} + {num2} is {num1 + num2}")
        elif choice == '-':
            print(f"The result of {num1} - {num2} is {num1 - num2}")
        elif choice == '*':
            print(f"The result of {num1} * {num2} is {num1 * num2}")
        elif choice == '/':
            if num2 != 0:
                print(f"The result of {num1} / {num2} is {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Please choose a valid operation.")
            
calculator()