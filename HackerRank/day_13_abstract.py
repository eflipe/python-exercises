from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    def display(self):

        print(f'''Title: {self.title}
Author: {self.author}
Price: {self.price}''')
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

#otra

class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))
