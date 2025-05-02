# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"This is {self.restaurant_name} restaurant. We serve {self.cuisine_type} cuisine.")
    
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} restaurant is open!")

#     def close_restaurant(self):
#         print(f"{self.restaurant_name} is closed.")

# my_restaurant = Restaurant('Sushi Wars', 'Japanese')
# my_restaurant.open_restaurant()
# my_restaurant.describe_restaurant()

# my_restaurant_1 = Restaurant('Pasta Wars', 'Italian')
# my_restaurant_2 = Restaurant('Taco Wars', 'Mexican')
# my_restaurant_3 = Restaurant('Samosa Wars', 'Indian')
# print("")
# my_restaurant_1.open_restaurant()
# my_restaurant_1.describe_restaurant()
# print("")
# my_restaurant_2.open_restaurant()
# my_restaurant_2.describe_restaurant()
# print("")
# my_restaurant_3.open_restaurant()
# my_restaurant_3.describe_restaurant()

class User:
    def __init__(self, first_name, region):
        self.first_name = first_name
        self.last_name = "Apple"
        self.region = region
    def describe_user(self):
        print(f"Hi, I'm {self.first_name} {self.last_name}. I'm from {self.region}.")
    def greet_user(self):
        print(f"Welcome {self.first_name}! Nice to meet you!")

harsh_user = User('Harsh', 'India')
harsh_user.describe_user()
harsh_user.greet_user()
print("")
harsh_user.last_name = "Vardhan"
harsh_user.describe_user()

        