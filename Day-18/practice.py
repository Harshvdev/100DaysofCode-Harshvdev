# Part -1 of practicing OOP (Object-Oriented Programming)

class Dog:

    def smart_dog(self, x, y):
        return x + y

    def bark(self):
        print("Bark-bark!")

d = Dog()
d.bark()
print(type(d))
print(d.smart_dog(1, 2))


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        return f"{self.name} meows"
    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."
    
m = Cat('Kuro', 2)

print(m.meow())
print(m.birthday())

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_grade(self):
        if self.marks >= 80:
            return "Grade: A"
        elif self.marks >= 60 and self.marks < 80:
            return "Grade: B"
        elif self.marks >= 40 and self.marks < 60:
            return "Grade: C"
        else:
            return "Failed."
        
    def display(self):
        return f"Name: {self.name}\nRoll Number: {self.roll_no}\nMarks: {self.marks}\n{Student.get_grade(self)}" #I used Student.get_grade(self) instead of self.get_grade(self). It works but I still asked ChatGPT and it said it's not recommended to use call the class. I won't fix it on purpose because I'd like to keep this "working" mistake as a memory.
    
student_1 = Student("Harsh", 16, 84)
print(student_1.get_grade())
print(student_1.display())

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} has been added to your account."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} has been withdrawn from your account."
        else:
            return "Not enough balance."

    def get_balance(self):
        return f"Account Balance: {self.balance}"
    
user_1 = BankAccount("Harsh", 0)

print(user_1.deposit(1000))

print(user_1.withdraw(2000))

print(user_1.get_balance())


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        pass