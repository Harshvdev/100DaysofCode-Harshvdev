num1 = float(input("Enter the first number: "))
op = int(input("Add (+): 1\nSubtract (-): 2\nMultiply (*): 3\nDivide (/): 4\n\n"))
num2 = float(input("\nEnter the second number: "))

if op == 1:
    print(f"{num1} plus {num2} is {num1+num2}")
elif op == 2:
    print(f"{num1} minus {num2} is {num1-num2}")
elif op == 3:
    print(f"{num1} multiplied by {num2} is {num1*num2}")
elif op == 4:
    if num2 == 0:
        print("Dividing by zero is not possible.")
    else:
        print(f"{num1} divided by {num2} is {num1/num2}")
else:
    print("\nError. Choose from 1 to 4.")