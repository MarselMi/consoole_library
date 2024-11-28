import json


def open_file_for_read(exc: None | str = None) -> list:
    """Функция работает с .json файлом, возвращает список словарей """
    if exc:
        try:
            with open("books.json", "r") as fw:
                books: list = json.loads(fw.read()).get('Books')
                return books
        except FileNotFoundError as err:
            f"{err}\n {exc}"
    else:
        try:
            with open("books.json", "r") as fw:
                books: list = json.loads(fw.read()).get('Books')
        except FileNotFoundError:
            books = []
        return books


def open_file_for_write(update_books_list: list) -> None:
    """Функция принимает список из словарей, с помощью контекстного менеджера
     открывает файл для записи обновленных данных"""
    with open("books.json", "w") as fw:
        fw.writelines(json.dumps({"Books": update_books_list}))
