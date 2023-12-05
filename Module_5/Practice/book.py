class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_genre(self):
        return self.genre
    
    def set_genre(self, genre):
        self.genre = genre

# my_book_collection = Book.__dict__

