text = input("Enter your text: ").strip() #Takes input from the user and strips the accidental spaces.
word = input("Enter the word you want to censor: ").strip() #||
count = "*" * len(word) #Multipleis asterisk with the number of letters in 'word'
censored = text.replace(word, count) #replaces normal word with censored word.
print(f"\nCensored word: {censored}") #Prints the sentence with censored word.