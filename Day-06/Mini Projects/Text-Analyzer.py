
text = input("Enter a word or a letter: ").lower()
print(len(text)) #Count the total number of characters (including spaces).

letter = input("Enter which letter you want to count in the text provided: ").strip().lower()
print(text.count(letter)) #Count how many times a specific letter (provided by the user) appears in the sentence.

word = input("Enter the word you would like to find the position of: ").strip().lower()
print(text.index(word)) #Find the position where a specific word starts in the sentence.










