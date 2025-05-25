while True:
    try:
        # Ask for input
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        # Perform division
        result = number1 / number2

    except ValueError:
        # Handling invalid value input
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        # Handling division by zero
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        # If There is no error,  then print result and break the loop
        print(f"The result of {number1} divided by {number2} is {result}")
        break
    finally:
        print("Attempt to perform division completed.\n")
