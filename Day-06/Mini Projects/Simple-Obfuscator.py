text = input("Enter text to obfuscate: ")
obfuscated_text = text.replace("a", "@").replace("A", "@").replace("e", "3").replace("E", "3").replace("i", "1").replace("I", "1").replace("o", "0").replace("O", "0").replace("u", "#").replace("U", "#") #replaces vowels with symbols.
print(obfuscated_text)