# Student ID: 123456
# Student Name: SHASHA
# Topic: Book Lending System

# -------------------------------
# Helper: Update Book Status
# -------------------------------
def update_book_status(book_id, new_status):
    lines = []
    with open("books.txt", "r") as f:
        lines = f.readlines()

    with open("books.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == book_id:
                f.write(f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|{new_status}\n")
            else:
                f.write(line)

# -------------------------------
# Book Management
# -------------------------------
def view_books():
    print("\nList of Books:")
    with open("books.txt", "r") as f:
        for line in f:
            book_id, title, author, year, status = line.strip().split("|")
            print(f"{book_id} - {title} ({author}, {year}) [{status}]")

# -------------------------------
# Borrower Management
# -------------------------------
def view_borrowers():
    print("\nList of Borrowers:")
    with open("borrowers.txt", "r") as f:
        for line in f:
            student_id, name, book_id, days = line.strip().split("|")
            print(f"{student_id} - {name} borrowed {book_id} for {days} days")

def borrow_book():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    book_id = input("Enter Book ID to borrow: ")
    days = input("Enter number of days borrowed: ")

    # Add borrower record
    with open("borrowers.txt", "a") as f:
        f.write(f"{student_id}|{name}|{book_id}|{days}\n")

    # Update book status
    update_book_status(book_id, "Borrowed")
    print("Book borrowed successfully!")

def return_book():
    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID to return: ")

    # Update borrower record
    lines = []
    with open("borrowers.txt", "r") as f:
        lines = f.readlines()

    with open("borrowers.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == student_id and data[2] == book_id:
                f.write(f"{data[0]}|{data[1]}|None|0\n")
            else:
                f.write(line)

    # Update book status
    update_book_status(book_id, "Available")
    print("Book returned successfully!")

# -------------------------------
# Menus
# -------------------------------
def book_interface():
    while True:
        print("\n--- Book Management ---")
        print("1. View Books")
        print("2. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            break
        else:
            print("Invalid choice, try again.")

def borrower_interface():
    while True:
        print("\n--- Borrower Management ---")
        print("1. View Borrowers")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_borrowers()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

def main_menu():
    while True:
        print("\n=== Library System ===")
        print("1. Book Management")
        print("2. Borrower Management")
        print("3. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            book_interface()
        elif choice == "2":
            borrower_interface()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, try again.")

def update_book():
    book_id = input("Enter Book ID to update: ")
    new_title = input("Enter new Title: ")
    new_author = input("Enter new Author: ")
    new_year = input("Enter new Year: ")

    # Read all lines
    with open("books.txt", "r") as f:
        lines = f.readlines()

    # Rewrite with updated line
    with open("books.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == book_id:
                # Replace with new details, keep status unchanged
                f.write(f"{data[0]}|{new_title}|{new_author}|{new_year}|{data[4]}\n")
            else:
                f.write(line)

    print("Book updated successfully!")


def book_interface():
    while True:
        print("\n--- Book Management ---")
        print("1. View Books")
        print("2. Update Book")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            update_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

def update_borrower():
    student_id = input("Enter Student ID to update: ")
    book_id = input("Enter current Book ID: ")
    new_name = input("Enter new Name: ")
    new_book_id = input("Enter new Book ID (or None): ")
    new_days = input("Enter new Days Borrowed: ")

    # Read all lines
    with open("borrowers.txt", "r") as f:
        lines = f.readlines()

    # Rewrite with updated line
    with open("borrowers.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == student_id and data[2] == book_id:
                f.write(f"{data[0]}|{new_name}|{new_book_id}|{new_days}\n")
            else:
                f.write(line)

    print("Borrower updated successfully!")

def borrower_interface():
    while True:
        print("\n--- Borrower Management ---")
        print("1. View Borrowers")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Update Borrower")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_borrowers()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            update_borrower()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

def delete_borrower():
    student_id = input("Enter Student ID to delete: ")

    # Read all lines
    with open("borrowers.txt", "r") as f:
        lines = f.readlines()

    # Rewrite file without the matching borrower
    with open("borrowers.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] != student_id:  # Keep all except the one to delete
                f.write(line)

    print("Borrower deleted successfully!")

def borrower_interface():
    while True:
        print("\n--- Borrower Management ---")
        print("1. View Borrowers")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Update Borrower")
        print("5. Delete Borrower")
        print("6. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_borrowers()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            update_borrower()
        elif choice == "5":
            delete_borrower()
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")

    # Read all lines
    with open("books.txt", "r") as f:
        lines = f.readlines()

    # Rewrite file without the matching book
    with open("books.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] != book_id:  # Keep all except the one to delete
                f.write(line)

    print("Book deleted successfully!")

def book_interface():
    while True:
        print("\n--- Book Management ---")
        print("1. View Books")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

def add_book():
    book_id = input("Enter new Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")
    status = "Available"  # new books are always available at first

    # Append new book record to books.txt
    with open("books.txt", "a") as f:
        f.write(f"{book_id}|{title}|{author}|{year}|{status}\n")

    print("Book added successfully!")

def book_interface():
    while True:
        print("\n--- Book Management ---")
        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

def add_borrower():
    student_id = input("Enter new Student ID: ")
    name = input("Enter Name: ")
    book_id = input("Enter Book ID (or None if not borrowing yet): ")
    days = input("Enter Days Borrowed (0 if none): ")

    # Append new borrower record to borrowers.txt
    with open("borrowers.txt", "a") as f:
        f.write(f"{student_id}|{name}|{book_id}|{days}\n")

    print("Borrower added successfully!")

def borrower_interface():
    while True:
        print("\n--- Borrower Management ---")
        print("1. View Borrowers")
        print("2. Add Borrower")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Update Borrower")
        print("6. Delete Borrower")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == "1":
            view_borrowers()
        elif choice == "2":
            add_borrower()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            update_borrower()
        elif choice == "6":
            delete_borrower()
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")

def return_book():
    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID to return: ")

    # Read borrower records
    lines = []
    with open("borrowers.txt", "r") as f:
        lines = f.readlines()

    with open("borrowers.txt", "w") as f:
        for line in lines:
            data = line.strip().split("|")
            if data[0] == student_id and data[2] == book_id:
                days_borrowed = int(data[3])

                # --- Late Fee Calculation ---
                allowed_days = 7
                late_days = max(0, days_borrowed - allowed_days)
                late_fee = late_days * 1  # RM1 per day

                print(f"Book returned successfully!")
                if late_fee > 0:
                    print(f"Late fee = RM{late_fee}")
                else:
                    print("No late fee. Thank you for returning on time!")

                # Reset borrower record
                f.write(f"{data[0]}|{data[1]}|None|0\n")
            else:
                f.write(line)

    # Update book status back to Available
    update_book_status(book_id, "Available")

# -------------------------------
# Run Program
# -------------------------------
main_menu()

