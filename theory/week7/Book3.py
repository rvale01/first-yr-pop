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


book1 = Book("Greg M. Perry & Dean Miller", 2014, "C Programming")
book2 = Book("John Hunt", 2019, "A Beginners Guide to Python 3 Programming")

books = []

books.append(book2)
books.append(book1)

for x in books:
    x.printBook()

