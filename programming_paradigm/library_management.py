class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that contains books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if successful, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if successful, False if book not found or not checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Return a list of available books (title and author) in the library."""
        return [(book.title, book.author) for book in self._books if book.is_available()]
 
