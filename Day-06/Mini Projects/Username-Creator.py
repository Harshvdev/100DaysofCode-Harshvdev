name = input("Enter Your Name: ").strip() #Strips the extra spaces in the user input.
parts = name.split(" ") #Divides user's first name, and middle name/last name.
first_name = parts[0] 
last_name = parts[-1]

print(f"Your username is {first_name[0].lower()+last_name.lower()}") #Outputs the first letter of the first name+lastname in lowercase.
