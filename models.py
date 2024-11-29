from abc import ABC


class BaseBook(ABC):

    def __init__(self, title: str, author: str, year: int, status: str):
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status


class Book(BaseBook):

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str):
        super().__init__(title, author, year, status)
        self.id: int = book_id

    def __str__(self):
        return f"<id: {self.id}, title: {self.title}, author: {self.author}, year: {self.year}, status: {self.status}>"

    def __repr__(self):
        return f"<id: {self.id}, title: {self.title}, author: {self.author}, year: {self.year}, status: {self.status}>"

