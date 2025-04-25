#Revising String Manipulation

name = 'elric'
language = 'python'

print(f"\nHey {name.title()}, would you like to learn some {language.title()} today?\n\n") #.title() capitalizes the first letter of a single word.

author = 'albert einstein'
quote = "a person who never made a mistake never tried anything new."

print(f"{author.title()} once said, \"{quote.capitalize()}\"\n\n") #\" allows to use double quotes inside double quotes; you can also use single quotes inside double quotes. .capitalize() capitalizes the first letter in a sentence or a single word.

name2 = '  kaneki Ken           '
manga = 'tokyo ghoul'
quote2 = "Courage is not the absence of fear, but the ability to face it head-on"
print(f"\"{quote2.capitalize()}\"\n\t\t\t\t\t\t\t\t\t   -{name2.strip().title()} from {manga}\n\n") #used \t and \n and added some space after \t on purpose.

file_name = 'suffix-prefix.txt'

print(f"File name is {file_name.removesuffix(".txt")}, and file type is {file_name.removeprefix("suffix-prefix")}\n\n")



