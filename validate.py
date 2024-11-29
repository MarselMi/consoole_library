from abc import ABC, abstractmethod

from values import MAX_LENGHT
from models import Book


class Validator(ABC):
    
    @abstractmethod
    def validate(self, obj_validated):
        pass
    
    
class ArgsValidator(Validator):
    
    def validate(self, obj_validated):
        self.create_validator(obj_validated)
        self.update_validator(obj_validated)
    
    @staticmethod
    def create_data_validator(obj_validated):
        for key, val in obj_validated.items():
            if len(val) > MAX_LENGHT:
                raise IndexError("Поле {key} содеожит слишком много символов")
                
        if not obj_validated.year.isnumeric():
            raise ValueError("Поле год должно содержать только цифры")
        else:
            int_year = int(obj_validated.year)
            if int_year < 1:
                raise ValueError("Год не может быть отрицательным числом")        

    @staticmethod
    def update_data_validator(obj_validated):
        allowed_statuses = ("В наличии", "Выдана")
        if obj_validated[-1] not in allowed_statuses:
            raise ValueError("Доступные статусы: 'В наличии'/'Выдана'")
    
    
class BookValidator(Validator):
    """
    validator = Validator()
    validator.validate(book_instance: Book)
    Для валидации данных при создании необходимо инициализировать
    класс Validator, затем ввзвать метод .validate
    передав в него обьет класса Book
    """

    def validate(self, obj_validated: Book):
        self.check_instance_obj(obj_validated)
        self.check_year(obj_validated)
        self.check_lenght_str_fields(obj_validated)
 
    @staticmethod
    def check_instance_obj(obj_validated: Book | None):
        if not isinstance(obj_validated, Book):
            raise ValueError("Обьект не является экземпляром Книги")

    @staticmethod
    def check_year(obj_validated: Book):
        if isinstance(obj_validated.year, str):
            if not obj_validated.year.isnumeric():
                raise ValueError("Поле год должно содержать только цифры")

        if not isinstance(obj_validated.year, int):
            raise ValueError("Поле год числовое значение")

        if obj_validated.year < 0:
            raise ValueError("Год издания не может быть отрицательным")
            
    @staticmethod
    def check_lenght_str_fields(obj_validated: Book):
        for key, value in obj_validated.items():
            if isinstance(value, str) and len(value) > MAX_LENGHT:
                raise IndexError(f"В поле {key} превышение максимальной допустимой длинны строки")
                
        
        