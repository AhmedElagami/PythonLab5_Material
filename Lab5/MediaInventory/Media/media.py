class Media:
    """Base/Parent/Super class for representing a media item."""

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        output = f"Type#{self.__class__}\n"
        output += f"{self.title}\n"
        output += f"{self.author}\n"
        output += f"{self.copies}\n"
        return output 
    
    def __repr__(self):
        return self.__str__