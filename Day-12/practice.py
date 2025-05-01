class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Shiro', 2)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")