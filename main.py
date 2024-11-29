import argparse

from crud import CreateBook, update_book, delete_book


def main():
    commands = ("new","update","del")
    information = argparse.ArgumentParser(description="CLI-приложение библиотеки")
    
    while True:
        add_arguments = information.add_argument(
            "input", 
            help("""
            Для создания книги введите команду: "-c 'new' -p 'book_title book_author book_year'" -/n
            Для обновления: "-с 'update' -p 'book_id new_status'" где id это id книги/n
            Для удаления: "-c 'del' -p 'book_id'" где id это id книги/n
            Для выхода: комбинация клавишь "ctrl+c"
            """)
        )
        input_arg = information.parse_args()
        
    
    
if __name__ == "__main__":
    main()