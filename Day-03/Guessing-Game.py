#A Simple Guessing Game Using While Loop

word = "Giraffe"
turn = 5
guessed_word = ""

while guessed_word != word and turn > 0:

        guessed_word = input("Enter Guessed Word: ")
        if guessed_word != word:
            print(f"Wrong!\nHint: First letter is {word[0]}")
            turn -= 1
            print(f"Now you have {turn} chances left")
        else:
            print("You reached your limits!")
            break
if turn == 0:
     print(f"You lost! The word is {word}")

