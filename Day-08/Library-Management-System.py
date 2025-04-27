books = {
        
         'Pride and Prejudice': 'Jane Austen', 
         'Great Expectations': 'Charles Dickens', 
         'The Adventures of Huckleberry Finn': 'Mark Twain',
         'To the Lighthouse': 'Virginia Woolf',
         'War and Peace': 'Leo Tolstoy',
         'Crime and Punishment': 'Fyodor Dostoevsky',
         'Norwegian Wood': 'Haruki Murakami',
         'One Hundred Years of Solitude': 'Gabriel García Márquez',
         'Things Fall Apart': 'Chinua Achebe',
         'The Handmaid’s Tale': 'Margaret Atwood'

         }

active = True

def update_search_books():
    search_books = {} #To-be filled with lowercase books keys with original book values.
    for book in books: 
        search_books[book.lower()] = book
    return search_books
search_books = update_search_books()
while active:
    ip = input("\nWhat do you want to do? [show/borrow/return/search/quit]: ").lower().strip()

    if ip == 'show':
        print(f"Here are all the books in the library:\n")
        for book, author in sorted(books.items()):
            print(f"{book} by {author}")

    elif ip == 'borrow':
        borrowed_book = input("Enter the name of the book you'd like to borrow: ").lower().strip()
        if borrowed_book in search_books:
            original_title = search_books[borrowed_book]
            books.pop(original_title)
            search_books = update_search_books()
            print(f"{original_title} has been given to you.")
        else:
            print("Sorry, this book is not available.")

    elif ip == 'return':
        returned_book = input("Which book do you want to return?:\n: ").strip()
        returned_book_author = input("What is the name of the author?\n: ").title().strip()
        books[returned_book] = returned_book_author
        search_books = update_search_books()

    elif ip == 'search':
        searched_book = input("Enter the name of the book you want to search for: ").lower().strip()
        if searched_book in search_books:
            print("Yes, it's available.")
        else:
            print("Sorry, it's not availble.")

    elif ip == 'quit':
        active = False

print("\nPlease come again! ^^")

#I'll need to practice more because my head is spinning after reading all this -_-
#Tomorrow I'll practice more with Dictionaries before advancing to the next topic.