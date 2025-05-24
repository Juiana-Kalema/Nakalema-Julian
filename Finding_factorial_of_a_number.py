import math
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

# Find the factorial of 5 without using the imported math class
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Finding the factorial of any number from user input without using the impoirted math class
number = int(input("Enter a number whose factorial you are to find: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
#print(result)

#using the imported math class to find factorial of 5
print(f"The factorial of 5 is: {math.factorial(5)}")

