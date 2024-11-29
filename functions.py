import json
import argparse

from crud import CreateBook, update_book, delete_book
from validate import BookValidator
from values import STATUS
from crud import open_file_for_read


def args_params() -> dict:
    '''
    Функция для реализации программы через консоль, c описанием работы,
    выводом именованных параметров в виде словаря
    '''
    parser = argparse.ArgumentParser(
        description="""
        CLI-приложение управления библиотекой\n
        Возможности:
        1. Добавление книги: --action new --title Название_книги --author Фамилия_Имя_Отчество --year год_издания.
        2. Удаление книги: --action del --id id_книги, которую нужно удалить.
        3. Поиск книги: --action filter --param title/author/year --equal образец_что_искать.
        4. Отображение всех книг: --action all выводит книги с данными.
        5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--action', type=str,
        help="Доступные действие: (new/del/update/all/filter)"
    )
    parser.add_argument(
        '--title', type=str,
        help='Название книги'
    )
    parser.add_argument(
        '--author', type=str,
        help='Автор'
    )
    parser.add_argument(
        '--year', metavar='int', type=int,
        help='Год издания'
    )
    parser.add_argument(
        '--id', metavar='int', type=int,
        help='ID Книги'
    )
    parser.add_argument(
        '--status', type=str,
        help='Статус книги'
    )
    args = parser.parse_args()

    return args.__dict__


def detect_action(param: dict) -> None:
    validator = BookValidator()

    if param.get("action") == "new":

        validator.validate(param)

        new_book = CreateBook(
            title=param.get("title"),
            author=param.get("author"),
            year=param.get("year"),
            status=STATUS["in_stock"]
        )

        print(new_book())
    elif param.get("action") == "del":
        print(delete_book(param.get("id")))
    elif param.get("action") == "all":
        books = open_file_for_read()
        if len(books):
            for book in open_file_for_read():
                print(book)
    elif param.get("action") == "update":

        validator.update_validate(param)

        print(update_book(book_id=param.get("id"), new_status=param.get("status")))
    elif param.get("action") == "filter":
        pass
    else:
        print("Введите корректный action, воспользуйтесь помощником добавив флаг -h либо --help")
