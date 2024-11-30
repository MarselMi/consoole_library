import json


def open_file_to_read(exc: None | str = None) -> list:
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


def save_to_file(books: list) -> None:
    """Функция принимает список из словарей, с помощью контекстного менеджера
     открывает файл для записи обновленных данных"""
    with open("books.json", "w") as fw:
        fw.writelines(json.dumps({"Books": list(books)}))


def delete_book(book_id: int) -> str:
    books: list = open_file_to_read(exc="Библиотека пуста! Нет книг для удаления!")

    update_books_list: list = list(filter(lambda a: a.get('id') != book_id, books))
    if len(books) == len(update_books_list):
        raise IndexError(f"Книга с id={book_id} отсутствует!")

    save_to_file(update_books_list)

    return f"Книга с id={book_id} удалена"


def update_book(book_id: int, new_status: str) -> str:
    books: list = open_file_to_read(exc="Библиотека пуста! Нет книг для обновления!")
    new_status = new_status.lower()

    flag_change: bool = True

    for book in books:
        if book.get("id") == book_id:
            flag_change: bool = False
            book["status"] = new_status

    if flag_change:
        raise ValueError(f"Книга с id={book_id} отсутствует!")
    else:
        save_to_file(books)
        return f"Статус книги с id={book_id} изменен на {new_status}"
