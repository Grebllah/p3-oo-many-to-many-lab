class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author.name == self.name]
    
    def books(self):
        book_by_author = [book.book for book in Contract.all if book.author.name == self.name]
        return book_by_author

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total = total + contract.royalties
        return total

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book.title == self.title]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book.title == self.title]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if type(author) == Author:
            self.author = author
        else: raise Exception
        
        if type(book) == Book:
            self.book = book
        else: raise Exception
        
        if type(date) == str:
            self.date = date
        else: raise Exception
        
        if type(royalties) == int:
            self.royalties = royalties
        else: raise Exception
        
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
