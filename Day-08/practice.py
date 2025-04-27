books = {'The 48 Laws of Power': 'Robert Greene', 'Atomic Habits': 'James Clear'}
print(books['The 48 Laws of Power'])
books['Ogre'] = 90
books['Harry Potter'] = 'J.K Rowling'
print(books)
del books['Ogre']
print(f"\nAfter deleting 'Ogre':\n {books}")
# text = input("Enter the key you want to check: ")
# new_book = books.get(text, 'Key Not Found') #Use get() if you are unsure whether a value exist in the dictionary. You can specify a custom error as well.
# print(new_book)

iterator = iter(books)
print(iterator)

print(next(iter(books)))
new_books = list(books)
print(new_books[1])

for key in books.keys():
    print(key)

for key, value in books.items():
    print(f"Key: {key}\nValue: {value}")

for value in books.values():
    print(value)

info = {'aketchum':{
    'first_name': 'Ash',
    'last_name': 'Ketchum',
    'location': 'Pallete Town'

}, 'kken':{
    'first_name': 'Ken',
    'last_name': 'Kaneki',
    'location': 'Tokyo'
}}

for username, user_info in info.items():
    print(f"\n\nUsername: {username}")
    full_name = user_info['first_name']+ " " +user_info['last_name']
    user_location = user_info['location']
    print(f"\tFull name: {full_name}\n\tLocation: {user_location}")
