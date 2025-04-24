def translator(word): #A custom function
    translated = "" #Empty string
    for letter in word: #Looping through every letter in word
        if letter.lower() in "aeiou": #Checks whether there's a vowel in "word"
            if letter.isupper():
                translated = translated+"G" #Replaces the vowel with "g"
            else:
                translated = translated + "g"
        else:
            translated = translated+letter #If it's not a vowel, it just adds the letter to the empty string
    return translated #Returns the translated word

print(translator(input('Enter word to translate: '))) #Prints the translated word