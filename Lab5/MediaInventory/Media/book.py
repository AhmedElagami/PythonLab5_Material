from .media import Media

class Book(Media):
    def __init__(self, title, author, copies, year_published):
        super().__init__(title, author, copies)
        self.year_published = year_published
    
    def __str__(self): # ! overriding the parent function __str__
        output = super().__str__()
        output += f"{self.year_published}"
        return output