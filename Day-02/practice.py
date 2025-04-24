from math import *

#Day-2

#Math and string functions

book = "Python Crash Course"
num = 18
print(book.upper())
print(book.isupper())
print(book.istitle())
print(book.lower())
print(len(book))
print(book[2])
print(book.index("t"))
print(book.replace("Python", "JavaScript"))
print("Hello, Mr. "+str(num))
print(pow(num, 2))
print(round(5.50000))
print(floor(234.241841453672))
print(ceil(234.245465646521))

user = input("Please enter your name: ")
print(f"Hi, {user.title()}, how are you doing?")



#Lists:

friends = ["Harsh", "Tanjiro", "Muzan", "Saitama", "Kaneki"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[2:])
print(friends[0:3])
friends[2] = "Rimuru"
print(friends)
friends.append("Zoro")
print(friends[5])
friends.insert(3, "Tony Stark")
print(friends[3])
friends.remove("Kaneki")
print(friends)
print(friends.index("Zoro"))
friends2 = friends.copy()



#Tuples:

coordinates = (4, 3) #Tuples CANNOT be changed. You can also create a list of tuples!
print(coordinates)
print(coordinates[0])




#functions

def greet_user(name):
    print(f"Nice to meet you {name}!")

greet_user(input())

def coordinates(x, y):
    print(f"Your x coord is {x}, and y coord is {y}")

coordinates(input("Enter x coordinate: "), input("Enter y coordinate: "))