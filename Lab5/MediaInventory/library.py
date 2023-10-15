from .Media.media import Media
from .exceptions import InvalidMediaType, MediaNotFound

class Library:
    """class representing a library which contains various media items."""

    def __init__(self):
        self.__inventory = []

    def add_media(self, media):
        if(isinstance(media, Media)):
            self.__inventory.append(media)
        else:
            raise InvalidMediaType
    
    def search_by_title(self, title):
        for media in self.__inventory:
            if media.title == title:
                return media

        raise MediaNotFound()
    
    def display_inventory(self):
        for media in self.__inventory:
            print(media)
