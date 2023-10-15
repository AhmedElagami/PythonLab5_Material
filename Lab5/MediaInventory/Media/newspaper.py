from .media import Media

class Newspaper(Media):
    def __init__(self, title, author, copies, frequency):
        super().__init__(title, author, copies)
        self.frequency = frequency
    
    def __str__(self): # ! overriding the parent function __str__
        output = super().__str__()
        output += f"{self.frequency}"
        return output