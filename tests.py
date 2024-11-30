import copy
import unittest

from models import Book
from crud import delete_book, update_book
from validate import BookValidator


class TestBook(unittest.TestCase):

    correct_data = {
        "title": "name",
        "author": "Correct",
        "year": 2000,
        "status": "в наличии",
    }

    correct_book_str = f"<id: {1}, title: {
    correct_data.get('title')
    }, author: {
    correct_data.get('author')
    }, year: {
    correct_data.get('year')
    }, status: {
    correct_data.get('status')
    }>"

    def test_success_create_book(self):
        validator = BookValidator()
        validator.validate(self.correct_data)
        new_book = Book(**self.correct_data)
        self.assertEqual(str(new_book), self.correct_book_str)
