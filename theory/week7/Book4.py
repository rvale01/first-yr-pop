class Book:
    numberOfBooks = 0
    numberPrinted = 0

    def __init__(self, authors, date, title):
        self.authors = authors
        self.date = date
        self.title = title
        Book.numberOfBooks += 1

    def printBook(self):
        # display data in 'author (date) title' format
        print("%s (%i) %s " % (self.authors, self.date, self.title))
        Book.numberPrinted += 1

    def printInfo(self):
        print("\nBook summary")
        print("Number of books: %i" % Book.numberOfBooks)
        print("Number printed: %i" % Book.numberPrinted)

def instBook(authors, date, title):
    book = Book(authors, date, title)
    return book

books =[]

books.append(instBook("Greg M. Perry & Dean Miller",2014,"C Programming"))
books.append(instBook("John Hunt",2019,"A Beginners Guide to Python 3 Programming"))
books.append(instBook("Brian Kernighan & Dennis Ritchie",1988,"The C Programming Language"))
books.append(instBook("Mark Lutz",2013,"Learning Python"))

for x in books:
    x.printBook()

