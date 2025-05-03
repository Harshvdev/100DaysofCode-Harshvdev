import random

print(random.random()) #Returns a float between 0.0 and 1.0 (exclusive of 1.0).

print(random.uniform(1, 4)) #Returns a random float between 1 and 4.

print(random.randint(1, 6)) #Returns a random integer between a and b (inclusive).

print(random.randrange(0, 11, 2)) #Returns a number from the range [start, stop) with step. i.e, it'll return random even int value in this case.

test_list = ['Apple', 'Banana', 'Tomato', 'Grapes']
print(random.choice(test_list)) #Returns a random item from the list.
print(random.choices(test_list, k=2)) #Select 2 items with replacemen

items = [1, 2, 3, 4, 5]
random.shuffle(items) # Shuffles the list in place
print(items)

random.seed(1) # Set a seed to reproduce the same random results
print(random.randint(1, 100)) #Now it will produce 18 every time because of seed function above it.








