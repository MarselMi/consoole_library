from abc import ABC, abstractmethod
from datetime import datetime as dt

from values import MAX_LENGTH, STATUS
from models import Book


class Validator(ABC):
    
    @abstractmethod
    def validate(self, obj_validated):
        pass
    
    
class ArgsValidator(Validator):
    
    def validate(self, obj_validated):
        self.create_data_validator(obj_validated)
    
    @staticmethod
    def create_data_validator(obj_validated):
        for key, val in obj_validated.items():
            if len(val) > MAX_LENGTH:
                raise IndexError(f"Поле {key} содеожит слишком много символов")

        int_year = obj_validated.get("year")
        if int_year < 1 or int_year > dt.now().year:
            raise ValueError("Год не может быть отрицательным числом")
    
    
class BookValidator(Validator):
    """
    validator = Validator()
    validator.validate(book_instance: Book)
    Для валидации данных при создании необходимо инициализировать
    класс Validator, затем ввзвать метод .validate
    передав в него обьет класса Book
    """

    def validate(self, obj_validated: dict):
        self.check_fields(obj_validated)
        self.check_year(obj_validated)
        self.check_length_str_fields(obj_validated)

    def update_validate(self, obj_validated: dict):
        self.update_status_validator(obj_validated)

    @staticmethod
    def check_instance_obj(obj_validated: dict | None):
        if not isinstance(obj_validated, Book):
            raise ValueError("Обьект не является экземпляром Книги")

    @staticmethod
    def check_year(obj_validated: dict):
        if obj_validated.get("year") is None:
            raise ValueError("Год это обязательный аргумент")

        if isinstance(obj_validated.get("year"), str):
            if not obj_validated.get("year").isnumeric():
                raise ValueError("Аргумент год должно содержать только цифры")

        if not isinstance(obj_validated.get("year"), int):
            raise ValueError("Аргумент год должен содержать числовое значение")

        if obj_validated.get("year") < 1:
            raise ValueError("Год не может быть отрицательным числом")
        if obj_validated.get("year") > dt.now().year:
            raise ValueError("Год не может быть больше текущего")
            
    @staticmethod
    def check_length_str_fields(obj_validated: dict):
        for key, value in obj_validated.items():
            if isinstance(value, str) and len(value) > MAX_LENGTH:
                raise IndexError(f"В аргумент {key} превышение максимально допустимой длинны строки")

    @staticmethod
    def check_fields(obj_validated: dict):
        required_keys = ("title", "author", "year")
        for key, value in obj_validated.items():
            if value is None and key in required_keys:
                raise ValueError(f"Аргумент {key} обязательный при создании книги")

    @staticmethod
    def update_status_validator(obj_validated):
        if obj_validated.get("status") not in STATUS.values():
            raise ValueError(f"Доступные статусы: {list(STATUS.values())}")
