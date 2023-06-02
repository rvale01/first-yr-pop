class Book:
    def __init__(self, authors, date, title):
        self.authors = authors
        self.date = date
        self.title = title
    
    def printBook(self):
        # display data in 'author (date) title' format
        print("%s (%i) %s " %(self.authors, self.date, self.title))

book1 = Book("Greg M. Perry & Dean Miller",2014,"C Programming")
book2 = Book("John Hunt",2019,"A Beginners Guide to Python 3 Programming")

book1.printBook()
book2.printBook()