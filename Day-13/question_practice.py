"""Mini Challenges"""
#Q-26: Write a number guessing game (user has to guess a number between 1–10).
import random as rnd

# guess = rnd.randint(1, 10)
# active = True

# while active:
#     try:
#         guessed_number = int(input("Enter your guessed number (1-10) [Enter 0 to quit.]: "))
#         if guessed_number == guess:
#             print(f"Correct! Hidden number is {guess}.")
#             break
#         elif guessed_number == 0:
#             active = False
#         else:
#             print("Wrong, try again:)")
#     except ValueError:
#         print("Please enter a valid number.")
#         continue

#Q-27: Build a simple calculator that supports +, -, *, /.
# def addition(num_1, num_2):
#     return num_1 + num_2
# def subtraction(num_1, num_2):
#     return num_1 - num_2
# def multiplication(num_1, num_2):
#     return num_1 * num_2
# def division(num_1, num_2):
#     return num_1 / num_2

# num_1 = float(input())
# num_2 = float(input())
# op = input()
# if op == '+':
#     print(addition(num_1, num_2))
# elif op == '-':
#     print(subtraction(num_1, num_2))
# elif op == '*':
#     print(multiplication(num_1, num_2))
# elif op == '/':
#     if num_2 == 0:
#         print("Cannot divide by zero.")
#     else:
#         print(division(num_1, num_2))
# else:
#     print("Enter correct operator.")
#Feeling lazy and it's boring and I have done this on Day-3 already so don't feel like doing.

#Q-28: Write a program to print the pattern:
# *
# **
# ***
# ****
# for i in range(1, 5):
#     print(i*'*')

#Q-29: Write a program to find the second largest number in a list.
# number_list = [2, 23, 3, 2, 6, 22, 55, 23, 66, 25, 36]
# temp_list = set(number_list)
# if len(temp_list) < 2:
#     print("List has less than 2 elements.")
# else:
#     temp_list.remove(max(temp_list))
#     print(f"{max(temp_list)} is the second largest number.")

#Q-30: Create a to-do list program where the user can add and remove tasks.
# todo_list = []
# todo_active = True

# while todo_active:
#     ask_user = input("What do you want to do? (add/remove/view/exit): ").strip().lower()
#     if ask_user == 'add':
#         add_task = input("Enter what you want to add: ")
#         todo_list.append(add_task)
#         print(f"'{add_task}' has been added to the list.")
#     elif ask_user == 'remove':
#         remove_task = input("Enter what you want to remove: ")
#         if remove_task in todo_list:
#             todo_list.remove(remove_task)
#             print(f"'{remove_task}' has been removed from the list.")
#         else:
#             print(f"'{remove_task}' is not in the list.")

#     elif ask_user == 'view':
#         print("Here are all the task in the list:\n")
#         for todo in todo_list:
#             print(todo)
#     elif ask_user == 'exit':
#         todo_active = False

"""Bonus (Slightly Advanced for Practice)"""
#Q-31: Create a function that returns a list of unique elements from another list.
# def unique(unilist):
#     return list(set(unilist))

# unilist = [1, 2, 2, 4, 2, 6, 6, 2, 3]
# print(unique(unilist))

#Q-32: Write a program to simulate a basic login system (username/password).
# login = {'Harsh': '12345678', 'Tony': 'Stark158', 'Hulk': 'Brucehulk789'}

# while True:
#     username = input("Enter your username: ")
#     if username in login.keys():
#         password =  input("Please enter your password: ")
#         if login[username] == password:
#             print("You're in!")
#             break
#         else:
#             print("Wrong password.")
#     else:
#         print("Incorrect username.")

#Q-33: Sort a list of dictionaries by a key (e.g., age).
dict_list = [{'Harsh': 18}, {'Toney': 45}, {'Sarah': 19}]


#Q-34: Create a dictionary from two lists using zip.


#Q-35: Build a rock-paper-scissors game in Python.
game_on = True
game_list = ['rock', 'paper', 'scissor']
while game_on:
    user_choice = input("[Rocl/Paper/Scissor]: ")
    bot_choice = rnd.choice(game_list)
    for check in game_list:
        if user_choice == 'rock' and bot_choice == 'paper':
            print(f"Bot: {bot_choice}, You: {user_choice}\nBot won.")
        elif user_choice == 'rock' and bot_choice == 'scissor':
            print(f"Bot: {bot_choice}, You: {user_choice}\nYou won!")
        













