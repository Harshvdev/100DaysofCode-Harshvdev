# num = 0

# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue # Continue tells Python to stop and go back to the beginning of the loop if the modulo of 1 and 2 is 0.
#     print(num)

# unverified_users = ['Alice', 'Brian', 'Harsh']
# verified_users = []

# while unverified_users:
#     current_user  = unverified_users.pop()
#     print(f"Veryfying {current_user}...")
#     verified_users.append(current_user)

# print(f"\nSuccessfully added the following users: \n")

# for users in verified_users:
#     print(users)


# pets = ['cat', 'dog', 'dog', 'cat', 'stone', 'stone', 'fridge']

# while 'fridge' in pets or 'stone' in pets:
#     if 'fridge' in pets:
#         pets.remove('fridge')
#     if 'stone' in pets:
#         pets.remove('stone')


# print(pets)


# choco_poll = True
# responses = {}
# while choco_poll:
#     name = input("Enter your name: ").lower().strip()
#     response = input("\nDo you choose death or chocolate?\n: ").lower().strip()
#     responses[name] = response
#     continue_poll = input("\nDoes anyone else want to choose? (yes/no)\n: ").lower().strip()
#     if continue_poll == 'no':
#         choco_poll = False

# print("**********POLL RESULTS**********\n")

# for name, response in responses.items():
#     print(f"{name.title()} chose {response.upper()}!")
# print("\nAll participants will get what they wanted 🤗")

def greet_user():
    return "Hello"

print(greet_user())

def user_name(first, last):
    person = {'first_name': first, 'last_name': last}
    return person

print(user_name("Harsh", "Vardhan"))

def build_person(first, last, age=None):
    person = {'first_n': first, 'last_n': last}
    if age:
        person['age'] = age
    return person

print(build_person("Harsh", "Vardhan", age=18))
print(build_person("Harsh", "Vardhan"))

unprinted_designs = ['phone_case', 'bracelet', 'locket']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing {current_design}...")
    completed_models.append(current_design)
print(completed_models)    