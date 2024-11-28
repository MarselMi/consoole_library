from abc import ABC, abstractmethod

from models import Book


class Validator:

    def create_validate(self, obj_validate: Book):
        self.check_instance_obj(obj_validate)

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