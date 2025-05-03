double = lambda d: d*2
print(double(3))
sum = lambda a, b: a+b
print(sum(4, 5))

def appl(fx, value):
    try:
        return fx * value
    except ValueError:
        print("Error")
    finally: #It always executes. Even after return statement.
        print("Nope")


print(appl(sum(3, 4), 5))
print(appl(sum(4, 5), double(5)))

appl2 = lambda sum, double: sum * double
print(appl2(sum(4, 5), double(5)))

num_list = [2, 3, 5, 1, 2, 4, 5, 6]

print(list(map(lambda d: d*d*2, num_list))) #Applies a function to every item in an iterable (like a list) and returns a new map object (which you usually convert into a list).
print(list(map(lambda x: x**2, range(3, 9))))

print(list(filter(lambda x: x/2 > 2, num_list)))
print(list(filter(lambda x: x % 2 == 0, range(1, 11)))) #Even numbers
print(list(filter(lambda x: x % 2 == 1, range(1, 11)))) #Odd numbers

test_dict = {'Harsh': 18, 'Wargon': 56, 'Ialva': 23}
print(test_dict.get('Harsw', "Nope. It doesn't exist."))

import temp