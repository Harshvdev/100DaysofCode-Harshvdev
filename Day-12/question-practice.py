"""Functions"""
#Q-16: Write a function to check if a number is prime.
def check_prime(num): #Took me a WHILE to understand this one.
    num_1 = int(num)
    if num_1 <= 1:
        return f"{num_1} is not a prime number"
    for i in range(2, int(((num_1)**0.5)+1)): 
        if num_1 % i == 0:
            return f"{num_1} is not a prime number."
    return f"{num_1} is a prime number."

print(check_prime(5))
'''I learned that to check if a number is prime, you only need to divide it by all the whole numbers from 2 up to the square root of that number (inclusive).
For example, if I take 35, the square root of 35 is approximately 5.91, so I only need to check for divisibility by 2, 3, 4, and 5.
If any of these divides 35 exactly (i.e., remainder is 0), then 35 is not prime.
In this case, 35 is divisible by 5 (35 ÷ 5 = 7), so it's not a prime number.'''

#Q-17: Write a function that takes a string and returns it in uppercase.
def upper_converter(some_string):
    return some_string.upper()

some_string_input = input("Enter something to convert to uppercase: ").strip()
print(upper_converter(some_string_input))

#Q-18: Create a function to calculate the factorial of a number.
def factorial_calc(factorial_num):
    result = 1
    if factorial_num < 0:
        return "Factorial for negative numbers is not defined."
    while factorial_num > 1:
        result = factorial_num * result
        factorial_num -= 1
    return result

print(factorial_calc(0))

#Q-19: Write a recursive function to find Fibonacci numbers.
'''0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...'''
def fibo_finder(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibo_finder(num-1) + fibo_finder(num-2)

print(fibo_finder(2))
#I got a headache by figuring this out...

#Q-20: Write a function to return the sum of all items in a list.
def sum_calc(user_list):
    result = 0
    for list_sum in user_list:
        result += list_sum #I forgot about sum(). I'll use it below.
    return result

def sum_func(user_list):
    return sum(user_list)
user_list = [3, 4, 5, 2, 5, 2, 7, 9]

print(sum_calc(user_list))
print(sum_func(user_list))

"""String & File Handling"""
#Q-21: Count the number of vowels in a string.
vowel_string = "Harsh"
vowel_count = 0
for vowel in vowel_string:
    if vowel in "AEIOUaeiou":
        vowel_count += 1
print(f"There is/are {vowel_count} vowel(s) in the word '{vowel_string}'.")

#Q-22: Reverse a string without using slicing.
normal_input = input("Enter something to reverse: ")
def string_reverse(normal_input):
    reverse = []
    for normal in normal_input:
        reverse.append(normal)
    reversed_str = ""
    while reverse:
        reversed_str = reversed_str + reverse.pop()
    return reversed_str
print(string_reverse(normal_input))

#Q-23: Check if a string is a palindrome.
palin_string = input("Enter word: ")
reverse_palin = string_reverse(palin_string.strip().lower()) #I used the function from question 23.

if palin_string.strip().lower() == reverse_palin:
    print(f"Yes, '{palin_string}' is a palindrome string.")
else:
    print(f"No, '{palin_string}' is not a Palindrome string.")

#Q-24: Read a text file and count the number of words.

with open('practice.txt', 'r') as file:
    print(file.readlines())
    file.seek(0)
    words = file.read().splitlines()
    print(len(words))
    file.close()

#Q-25: Write user input to a file and then read it back.
user_input = input("Enter something: ")
with open('practice.txt', 'w+') as file2:
    file2.write(user_input)
    file2.seek(0)
    print(file2.read())

