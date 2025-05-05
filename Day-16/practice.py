class Magic:
    def __init__(self, fire_attribute, wind_attribute, earth_attribute, water_attribute):
        self.fire_attribute = fire_attribute
        self.wind_attribute = wind_attribute
        self.earth_attribute = earth_attribute
        self.water_attribute = water_attribute


text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char, index)


#I spent most of the time on freeCodeCamp where I had to use their online code editor. So nothing much here.