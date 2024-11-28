import json

from models import BaseBook, Book
from validate import Validator
from values import STATUS
from functions import open_file_for_read, open_file_for_write


class CreateBook(BaseBook):
    """
     CreateBook(title: str, author: str, year: int, status: str)()
     -> Book(id: int, title: str, author: str, year: int, status: str)
     or
     new_book = CreateBook(title: str, author: str, year: int, status: str)
     new_book() -> Book(id: int, title: str, author: str, year: int, status: str)

     Обьект класса CreateBook удаляется сразу после создания нового экземпляра класса Book

    """
    book_id = 0

    def __init__(self, title: str, author: str, year: int, status: str):
        super().__init__(title, author, year, status)

    def __call__(self, *args, **kwargs):
        books: list = open_file_for_read()

        with open("books.json", "w") as fw:
            self.book_id += 1
            new_book: Book = Book(self.book_id, self.title, self.author, self.year, STATUS["in_stock"])

            validator = Validator()
            validator.create_validate(new_book)

            books.append(new_book.__dict__)
            fw.writelines(json.dumps({"Books": list(books)}))
        return new_book


def delete_book(book_id: int) -> str:
    books: list = open_file_for_read(exc="Библиотека пуста! Нет книг для удаления!")

    update_books_list: list = list(filter(lambda a: a.get('id') != book_id, books))
    if len(books) == len(update_books_list):
        raise IndexError(f"Книга с id={book_id} отсутствует!")

    open_file_for_write(update_books_list)

    return f"Книга с id={book_id} удалена"


def update_book(book_id: int, new_status: str) -> str:
    books: list = open_file_for_read(exc="Библиотека пуста! Нет книг для обновления!")

    flag_change: bool = True

    for book in books:
        if book.get("id") == book_id:
            flag_change: bool = False
            book["status"] = new_status

    if flag_change:
        raise ValueError(f"Книга с id={book_id} отсутствует!")
    else:
        return f"Статус книги с id={book_id} изменен на {new_status}"
