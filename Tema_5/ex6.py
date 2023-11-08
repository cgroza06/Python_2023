class LibraryItem:
    def __init__(self, title, item_id, is_checked_out=False):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = is_checked_out

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Checked Out: {self.is_checked_out}"

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

class Book(LibraryItem):
    def __init__(self, title, item_id, author, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.author = author

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Checked Out: {self.is_checked_out}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.director = director

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Director: {self.director}, Checked Out: {self.is_checked_out}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.issue_number = issue_number

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Issue Number: {self.issue_number}, Checked Out: {self.is_checked_out}"


book = Book("Harry Potter", 1, "J.K. Rowling")
dvd = DVD("Avengers", 2, "Joss Whedon")
magazine = Magazine("Time", 3, 123)

print(book.display_info())
print(book.check_out())
print(book.display_info())
print(book.return_item())
print(book.display_info(), end='\n\n')

print(dvd.display_info())
print(dvd.check_out())
print(dvd.display_info())
print(dvd.return_item())
print(dvd.display_info(), end='\n\n')

print(magazine.display_info())
print(magazine.check_out())
print(magazine.display_info())
print(magazine.return_item())
print(magazine.display_info(), end='\n\n')
