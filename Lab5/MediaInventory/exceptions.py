class MediaNotFound(Exception):
    def __init__(self, message="Media not found"):
        self.message = message
        super().__init__(self.message)
        
class InvalidMediaType(Exception):
    def __init__(self, message="Invalid Media Type"):
        self.message = message
        super().__init__(self.message)
