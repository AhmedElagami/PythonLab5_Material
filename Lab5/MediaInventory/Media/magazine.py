from .media import Media as MyMedia

class Magazine(MyMedia):
    def __init__(self, title, author, copies, category):
        super().__init__(title, author, copies)
        self.category = category
    
    def __str__(self): # ! overriding the parent function __str__
        output = super().__str__()
        output += f"{self.category}"
        return output
