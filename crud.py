import json

from models import BaseBook, Book


def open_file_for_read(exc: None | str = None) -> list:
    """
    Функция для чтения .json файла, возвращает список словарей книг,
    либо отлавливает исключение, если данные отсутсвуют
    """
    if exc:
        try:
            with open("books.json", "r") as fw:
                books: list = json.loads(fw.read()).get('Books')
                return books
        except FileNotFoundError:
            raise FileNotFoundError(f"{exc}")
    else:
        try:
            with open("books.json", "r") as fw:
                books: list = json.loads(fw.read()).get('Books')
        except FileNotFoundError:
            books: list = []
        return books


def open_file_for_write(update_books_list: list) -> None:
    """Функция принимает список из словарей, с помощью контекстного менеджера
     открывает файл для записи обновленных данных"""
    with open("books.json", "w") as fw:
        fw.writelines(json.dumps({"Books": update_books_list}))


class CreateBook(BaseBook):
    """
     CreateBook(title: str, author: str, year: int, status: str)()
     -> Book(id: int, title: str, author: str, year: int, status: str)
     or
     new_book = CreateBook(title: str, author: str, year: int, status: str)
     new_book() -> Book(id: int, title: str, author: str, year: int, status: str)
    """

    def __init__(self, title: str, author: str, year: int, status: str) -> None:
        super().__init__(title, author, year, status)

    def __call__(self, *args, **kwargs) -> Book:
        books: list = open_file_for_read()
        try:
            book_id = books[-1].get("id") + 1
        except IndexError:
            book_id = 1

        with open("books.json", "w") as fw:

            new_book: Book = Book(book_id, self.title, self.author, self.year, self.status)
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
        open_file_for_write(books)
        return f"Статус книги с id={book_id} изменен на {new_status}"
