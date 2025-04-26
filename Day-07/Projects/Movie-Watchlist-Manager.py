movies = ['Harry Potter', 'Jurassic Park', 'Avengers', 'Tokyo Ghoul', 'Peaky Blinders']

run = True
while run: #run it True, so it loops the entire thing while run is True.
    op = input("\nWhat do you want to do? [add/show/remove/search/quit]\n\n--> ").lower() #Asks for user input.
    if op == "add":
        movie_name = input("Enter movie you want to add: ").title().strip()
        movies.append(movie_name) #Adds the new movie to the list.
        print(f"{movie_name} has been added to the list!\n")
    elif op == "show":
        print("\nYour Movie List: ")
        for movie in sorted(movies):
            print(f"- {movie}") #Prints all the movies in the list one by one.
    elif op == "remove":
        remove_movie = input("Enter movie you want to remove: ").title().strip()
        if remove_movie in movies: #Checks whether the movie is in the list so it can remove it.
            movies.remove(remove_movie)
            print(f"{remove_movie} has been removed from the list.\n")
        else:
            print(f'"{remove_movie}" doesn\'t exist in the list.')
        
    elif op == "search":
        searched_movie = input("Enter movie name you want to search for: ").title().strip()
        if searched_movie in movies: #Checks if searched movie is in the list.
            print(f"\nYes, {searched_movie} is in the list!")
        else:
            print(f'\nNo, "{searched_movie}" is not in the list.')
    elif op == "quit": 
        run = False #Changes the run value to fale so the while loop stops.
    else:
        print("\nError, please enter the correct option.\n")