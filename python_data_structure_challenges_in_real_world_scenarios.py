'''
Task 1: Library System Enhancement 
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def add_book(lib_list):
    while True:
        title = input("What is the title of the book you'd like to add to the library? ")
        author = input(f"Who is the author of {title}? ")
        new_book_tuple = (title, author)
        if new_book_tuple in lib_list:
            return print("Book already in library.")
        else:
            lib_list.append(new_book_tuple)
            print(f"{new_book_tuple[1]}'s '{new_book_tuple[0]}' has been added to the library.")
            choice = input("Add another? (y/n): ").lower()
            if choice == 'n':
                print("FULL LIBRARY LIST:")
                for tup in lib_list:
                    print(f"- {tup[0]} by {tup[1]}")
                break

add_book(library)