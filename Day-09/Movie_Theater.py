# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

active = True
prices = {'less than 3': 'free', 'between 3 and 12': '$10', 'over 12': '$15'}

def age_check(age):
    if age < 0:
        print("\nAge can't be negative.")
        return False
    return True

while active:
    ip = input("What is your age?\n: ")
    if ip.lower() == "quit":
        break

    try:
        age = int(ip)
        if age_check(age):
            if age < 3:
                age_group = 'less than 3'
                print(f"\nYour ticket is {prices[age_group]}\n")
            elif age >= 3 and age <= 12:
                age_group = 'between 3 and 12'
                print(f"\nYour ticket is {prices[age_group]}\n")
            elif age > 12:
                age_group = 'over 12'
                print(f"\nYour ticket is {prices[age_group]}\n")
        else:
            print("Please enter your age correctly.\n")

    except ValueError:
        print("\nPlease enter a valid number for age.\n")
#I could make simpler version but wanted to use dictionary.