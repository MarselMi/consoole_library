import argparse

from models import Book
from validate import BookValidator
from values import STATUS
from crud import open_file_to_read, save_to_file, update_book, delete_book


def args_params() -> dict:
    '''
    Функция для реализации программы через консоль, c описанием работы,
    выводом именованных параметров в виде словаря
    '''
    parser = argparse.ArgumentParser(
        description="""
        CLI-приложение управления библиотекой\n
        Возможности:
        1. Добавление книги: --action new --title Название_книги --author "Фамилия_Имя_Отчество" --year год_издания.
        2. Удаление книги: --action del --id id_книги, которую нужно удалить.
        3. Поиск книги: --action filter --title/--author/--year "образец_что_искать".
        4. Отображение всех книг: --action all выводит книги с данными.
        5. Изменение статуса книги: --action update --id id_книги --status "в наличии"/"выдана".
        
        ОБРАТИТЕ ВНИМАНИЕ ЧТО В КОНСОЛЬНОМ ПРИЛОЖЕНИИ АРГУМЕНТЫ ОТДЕЛЯЮТСЯ МЕЖДУ СОБОЙ ПРОБЕЛОМ, 
        ПОЭТОМУ ДЛЯ КОРРЕКТНОЙ РАБОТЫ, ПРИ ВВОДЕ ДАННЫХ ГДЕ ИМЕЕТСЯ ПРОБЕЛ, ВОСПОЛЬЗУЙТЕСЬ " КАВЫЧКАМИ "
        
        ПРИМЕР: --author "Иванов Иван Иванович"
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--id', metavar='int', type=int,
        help='ID Книги'
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
        '--status', type=str,
        help='Статус книги'
    )
    args = parser.parse_args()

    return args.__dict__


def detect_action(param: dict) -> None:
    '''
    Функция для определения действий вводимых пользователем через консоль и
    для вывода информации об успешном завершении, либо выводом сообщением
    о возникшей ошибке
    :param param:
    :return:
    '''
    validator = BookValidator()

    if param.get("action") == "new":

        validator.validate(param)

        new_book = Book(
            title=param.get("title"),
            author=param.get("author"),
            year=param.get("year"),
            status=STATUS["in_stock"]
        )
        update_list = new_book.books
        update_list.append(new_book.__dict__())
        save_to_file(update_list)
        print(new_book)
    elif param.get("action") == "del":
        print(delete_book(param.get("id")))
    elif param.get("action") == "all":
        books = open_file_to_read()
        if len(books):
            for book in books:
                print(book)
    elif param.get("action") == "update":

        validator.update_validate(param)

        print(update_book(book_id=param.get("id"), new_status=param.get("status")))
    elif param.get("action") == "filter":
        filter_key = None
        equal = None
        for key, val in param.items():
            if val is not None:
                equal = val
                filter_key = key
        books = open_file_to_read()
        books_result = list(filter(
            lambda a: a.get(filter_key) == equal,
            books
        ))
        for book in books_result:
            print(book)
    else:
        print("Введите корректный action, воспользуйтесь помощником -h либо --help")
