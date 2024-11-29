from abc import ABC, abstractmethod

from values import MAX_LENGHT
from models import Book


class Validator:
    """
    validator = Validator()
    validator.book_create_validate(book_instance: Book)
    Для валидации данных при создании необходимо инициализировать
    класс Validator, затем ввзвать метод .book_create_validate
    передав в него обьет класса Book
    """

    def book_create_validate(self, obj_validate: Book):
        self.check_instance_obj(obj_validate)
        self.check_year(obj_validate)
        self.check_lenght_str_fields(obj_validate)

    @staticmethod
    def check_instance_obj(obj_validate: Book | None):
        if not isinstance(obj_validate, Book):
            raise ValueError("Обьект не является экземпляром Книги")

    @staticmethod
    def check_year(obj_validate: Book):
        if isinstance(obj_validate.year, str):
            if not obj_validate.year.isnumeric():
                raise ValueError("Поле год должно содержать только цифры")

        if not isinstance(obj_validate.year, int):
            raise ValueError("Поле год числовое значение")

        if obj_validate.year < 0:
            raise ValueError("Год издания не может быть отрицательным")
            
    @staticmethod
    def check_lenght_str_fields(obj_validate: Book):
        for key, value in obj_validate.items():
            if isinstance(value, str) and len(value) > MAX_LENGHT:
                raise IndexError(f"В поле {key} превышение максимальной допустимой длинны строки")
                
        
        