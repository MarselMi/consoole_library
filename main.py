import argparse

from crud import CreateBook, update_book, delete_book


def main():
    commands = ("new","update","del")
    information = argparse.ArgumentParser(description="CLI-приложение библиотеки")
    add_arguments = information.add_argument(
        "input", 
        help("""
        Для создания книги введите команду: "new"/n
        Для обновления: "update -id" где id это id книги/n
        Для удаления: "del -id" где id это id книги/n
        Для выхода: комбинация клавишь "ctrl+c"
        """)
    )
    input_arg = information.parse_args()[1]
    
    if input_arg not in commands:
        add_arguments()
    
    
if __name__ == "__main__":
    main()