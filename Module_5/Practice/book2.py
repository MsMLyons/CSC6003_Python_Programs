class Book(object):
    def __init__(self):      
        self.book_collection = {}

    def get_title(self):
        return self.book_collection.get("title")
    
    def set_title(self, title):
        self.book_collection["title"] = title

    def get_author(self):
        return self.book_collection.get("author")
    
    def set_author(self, author):
        self.book_collection["author"] = author

    def display_book(self):
        print("Books in my collection:")
        print(f"Title: {self.get_title()}, Author: {self.get_author()}")


book_collection = Book()

book_title = input("Please enter the title of a book you enjoy: ")
book_collection.set_title(book_title)

book_author = input("Please enter the author of that book: ")
book_collection.set_author(book_author)

book_collection.display_book()