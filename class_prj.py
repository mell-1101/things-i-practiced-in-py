class Book:
    
    all_books=[]
    def __init__(self,title,year,author,check="free"):
        self.title=title
        self.year=year
        self.author=author
        self.check=check
        Book.all_books.append(self)
 

    def availability(self):
        try:
            if self.check=="free":
                print("the book can be borrowed")
            elif self.check=="taken":
                print("the book cannot be borrowed")
        except():
            print("access denied")
    def borrow(self):
        if self.check=="free":
            self.check="taken"
            print("the book was borrowed")
        elif self.check=="taken":
            print("the book is taken")

    def return_book(self):
        if self.check=="taken":
            self.check="free"
            print("the book was returned")
        elif self.check=="free":
            print("the book is not borrowed thus it cannot be returned")

    def info(self):
        print(f"the author is {self.author} and the year of publish is {self.year} and the title is {self.title}")


Test=Book("math",1998,"max","taken")

Test.availability()
Test.info()
Test.return_book()
Test.availability()
