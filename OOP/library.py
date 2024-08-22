class Library:
    def __init__(self):
       self.books = {}

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books[book_name] = 1
        else:
            self.books[book_name] += 1

    def remove_book(self, book_name):
        if book_name not in self.books:
            return 
        elif self.books[book_name] == 1:
            self.books.pop(book_name)
        else:
            self.books[book_name] -= 1

    def book_count(self, book_name):
        count = self.books.get(book_name, 0)
        print(f"We have {count} copies of '{book_name}' in our library")

lb = Library()
lb.add_book("Google for Dummies")
lb.add_book("Google for Dummies")
lb.add_book("Harry")
lb.add_book("Harry")
lb.remove_book("Harry")
lb.book_count("Google for Dummies")
lb.book_count("Harry")
print(lb.books)