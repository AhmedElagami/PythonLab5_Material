from MediaInventory.library import Library
from MediaInventory.Media.book import Book
from MediaInventory.Media.magazine import Magazine
from MediaInventory.Media.newspaper import Newspaper

def main():
    lib = Library()

    lib.add_media(Book("To Kill a Mockingbird", "Harper Lee", 30, 1960))
    lib.add_media(Magazine("Time", "Editorial Team", 5, "News"))
    lib.add_media(Newspaper("The Washington Post", "The Editorial Team", 30, "Daily"))

    lib.display_inventory()

if __name__ == "__main__":
    main()

    

