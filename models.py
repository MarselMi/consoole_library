from abc import ABC
import json
from json import JSONDecodeError

from mixins import JsonMixin


class BaseBook(ABC):

    def __init__(self, title: str, author: str, year: int, status: str):
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status.lower()

    def save_to_json(self):
        pass


class Book(BaseBook, JsonMixin):
    '''
    Book("Title", "Author Of The Book", 2021, "status")
    При инициализации создается новый обьект книги, ID-книги генерируется атоматически
    путем инкрементации от крайнего сохраненного обьекта.
    '''

    def __init__(self, title: str, author: str, year: int, status: str):
        super().__init__(title, author, year, status)

        books: list = self.open_file_to_read()
        try:
            _book_id = books[-1].get("id") + 1
        except IndexError:
            _book_id = 1
        self.books = books
        self._id = _book_id

    def __str__(self):
        return f"<id: {self._id}, title: {self.title}, author: {self.author}, year: {self.year}, status: {self.status}>"

    def __repr__(self):
        return f"<id: {self._id}, title: {self.title}, author: {self.author}, year: {self.year}, status: {self.status}>"

    def __dict__(self):
        return {
            "id": self._id,
            "author": self.author,
            "title": self.title,
            "status": self.status,
            "year": self.year
        }

    @staticmethod
    def open_file_to_read() -> list:
        """
        Функция для чтения .json файла, возвращает список из словарей книг,
        либо отлавливает исключение, и возвращает пустой список, если данные отсутсвуют
        """
        try:
            with open("books.json", "r") as fw:
                try:
                    books: list = json.loads(fw.read()).get('Books')
                except JSONDecodeError:
                    books: list = []
        except FileNotFoundError:
            books: list = []
        return books
