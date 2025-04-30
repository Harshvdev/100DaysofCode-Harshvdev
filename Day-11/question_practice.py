"""Basic Syntax and Concepts"""
#Q-1: Write a Python program to swap two variables.
var_1 = "Harsh"
var_2 = "Optimus"
print(f"Variable-1: {var_1}, Variable-2: {var_2}")
temp_var = var_1
var_1 = var_2
var_2 = temp_var
print(f"Variable-1: {var_1}, Variable-2: {var_2}")

#Q-2: Create a variable of each type: int, float, string, list, tuple, set, dictionary.
int_variable = 999
print(int_variable)
float_variable = 9.99
print(float_variable)
string_variable = "Harsh"
print(string_variable)
list_variable = ["One", "Two", "Three"]
print(list_variable)
tuple_variable = (999, 21, "Harsh")
print(tuple_variable)
set_variable = {'Harsh', 2, 4, 5, 'Goku', 'Goku'} #Duplucate items are removed. It's unordered.
print(set_variable)
dictionary_variable = {'Harsh': 'Person', 'Cat': 'Animal', 'Dog': 'Animal'}
print(dictionary_variable)

#Q-3: What’s the difference between = and == in Python?
#####Answer: '=' is used when assigning a value to something (e.g variable); '==' is used as equality, to compare two items or vairables (e.g: if var_1 == 'Harsh').#####

#Q-4: Write a program to check if a number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

try:
    number = input("Enter a number to check: ")
    int_convert = int(number)
    print(check_even_odd(int_convert))
except ValueError:
    print("Please enter a valid integer.")

# #Q-5: Write a program that takes user input and prints it in reverse.
normal_input = input("Enter something to reverse: ")
reverse = []
for normal in normal_input:
    reverse.append(normal)
reversed_str = ""
while reverse:
    temp_var = reverse.pop()
    reversed_str = reversed_str + temp_var
print(reversed_str)

"""Control Flow (If, Loops)"""
#Q-6: Write a program to find the largest of three numbers using if statements.
try:
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    third_num = float(input("Enter third number: "))

    if first_num == second_num and first_num == third_num:
        print(f"All three numbers are equal.")
    elif second_num >= first_num and second_num >= third_num:
        print(f"{second_num} is the biggest.")
    elif third_num >= first_num and third_num >= second_num:
        print(f"{third_num} is the biggest.")
    else:
        print(f"{first_num} is the biggest.")
        
except ValueError:
    print("Please Enter a Valid Number.")

#Q-7: Print all numbers from 1 to 100 using a for loop.
for i in range(1, 101):
    print(i, end=' ') #Prints horizontly.
for j in range(1, 101):
    print(j) #Prints vertically.

#Q-8: Print the multiplication table of a number (entered by the user).
try:
    multiply_num = input("Which number's multiplication table do you want?\n: ")
    for m in range(1, 11):
        if '.' in multiply_num:
            num_type = float(multiply_num)
            result = m*num_type
            print(f"{num_type} x {m} = {result}")
        else:
            num_type = int(multiply_num)
            result = m*num_type
            print(f"{num_type}x{m} = {result}")
except ValueError:
    print("Enter a valid number.")

#Q-9: Use a while loop to find the sum of numbers from 1 to 50.
sum_num = 0
sum_result = 0
while sum_num < 50:
    sum_num += 1
    sum_result += sum_num
print(sum_result)
print((50) * (50 + 1) // 2) #Not related to the question.

#Q-10: Write a program that prints only even numbers from 1 to 20 using a loop.
for even_number in range(1, 21):
    if even_number % 2 == 0:
        print(even_number)
    else:
        pass
#OR
for even_number2 in range(2, 21, 2):
    print(even_number2) #I had forgotten about this :p

"""Data Structures (List, Tuple, Dict, Set)"""
#Q-11: Create a list of 5 numbers. Print the square of each number using a loop.
five_numbers = [1, 2, 3, 4, 5]
for square in five_numbers:
    print(f"Square of {square} is {square**2}.")

#Q-12: Take 5 inputs from the user and store them in a list.
times = 5
user_list = []
while times > 0:
    ask_user = input("Enter something to store in a list: ")
    user_list.append(ask_user)
    times -= 1
print(user_list)

#Q-13: Add and remove elements from a set. Show the output.
random_set = {'harsh', 2, 33, 9.2, 'vardhan'}
set_active = True

while set_active:
    user_input = input("What would you like to do? (add/remove/view/quit): ")
    if user_input.lower() == 'add':
        add_element = input("What would you like to add to the set? ")
        random_set.add(add_element)
        print(f"{add_element} has been added.")
    elif user_input.lower() == 'remove':
        remove_element = input("What would you like to remove from the set? ")
        random_set.remove(remove_element) #Use .discard() to avoid error on removing an item that doesn not exist.
        print(f"{remove_element} has been removed.")
    elif user_input.lower() == 'view':
        print("These are all the elements in the set:\n")
        for set_element in random_set:
            print(set_element)
    elif user_input.lower() == 'quit':
        set_active = False
    else:
        print("Maybe you made a mistake")

#Q-14: Create a dictionary to store names and ages. Print all names above age 18.
people = {'Harsh': 18, 'Tony Stark': 37, 'Sarah': 23, 'Goblin': 47, 'Anya': 8, 'Shinosuke': 5, 'Ash Ketchum': 10}
for name, age in people.items():
    if age >= 18:
        print(name)

# Q-15: Convert a tuple into a list and then sort it.
a_tuple = ('Harsh', 'Zorua', 'Omnitryx', 'Giga')
a_list = list(a_tuple)
a_list.sort()
print(a_list)

"""Functions"""
#Q-16: Write a function to check if a number is prime.


#Q-17: Write a function that takes a string and returns it in uppercase.
#Q-18: Create a function to calculate the factorial of a number.
#Q-19: Write a recursive function to find Fibonacci numbers.
#Q-20: Write a function to return the sum of all items in a list.
"""String & File Handling"""
#Q-21: Count the number of vowels in a string.
#Q-22: Reverse a string without using slicing.
#Q-23: Check if a string is a palindrome.
#Q-24: Read a text file and count the number of words.
#Q-25: Write user input to a file and then read it back.
"""Mini Challenges"""
#Q-26: Write a number guessing game (user has to guess a number between 1–10).
#Q-27: Build a simple calculator that supports +, -, *, /.
#Q-28: Write a program to print the pattern:
# *
# **
# ***
# ****

#Q-29: Write a program to find the second largest number in a list.
#Q-30: Create a to-do list program where the user can add and remove tasks.
"""BOnus (Slightly Advanced for Practice)"""
#Q-31: Create a function that returns a list of unique elements from another list.
#Q-32: Write a program to simulate a basic login system (username/password).
#Q-33: Sort a list of dictionaries by a key (e.g., age).
#Q-34: Create a dictionary from two lists using zip.
#Q-35: Build a rock-paper-scissors game in Python.
