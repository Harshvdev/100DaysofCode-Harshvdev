#I hate vowels game
vowel = 0
vowel_found = False
try:
    word = str(input("Enter shit: "))
    for entered_shit in word:
        if entered_shit in "aeiou":
            vowel += 1
            vowel_found = True
    if vowel_found == True:
        print(f"You entered a vowel x{vowel} times, Fuck you {vowel} times!")

    if vowel_found == False and word.isalpha():
        print("You didn't enter a vowel huh? You sneaky bastard!")
    if not word.isalpha():
        print("Enter a word you dumb bitch!")

except:
    print("WTF did you do?!")

quotes = open("anime2.txt", "w")
quotes.write("gaga")
quotes.close()
