import json
from typing import List, Dict, Union, Optional

Book = Dict[str, Union[int, str]]


class Library:
    def __init__(self, data_file: str = "library.json"):
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """Загружает данные о книгах из файла."""
        try:
            with open(self.data_file, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
            print(f"Создана новая база данных: '{self.data_file}'")

    def save_books(self) -> None:
        """Сохраняет данные о книгах в файл."""
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.books, file, indent=4)
        except IOError as e:
            print(f"Ошибка записи в файл: {e}")

    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена!")

    def delete_book(self, book_id: int) -> None:
        """Удаляет книгу по ID."""
        book_to_remove = next((book for book in self.books if book["id"] == book_id), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена!")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, key: str, value: str) -> List[Book]:
        """Ищет книги по заданному ключу и значению."""
        key = key.lower()
        if key not in ["id", "title", "author", "year", "status"]:
            print("Некорректное поле для поиска.")
            return []
        return [book for book in self.books if str(book.get(key, "")).lower() == value.lower()]

    def display_books(self) -> None:
        """Отображает список всех книг."""
        if not self.books:
            print("Библиотека пуста.")
            return
        print("\nСписок книг:")
        for book in self.books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                  f"Год: {book['year']}, Статус: {book['status']}")
        print()

    def update_status(self, book_id: int, status: str) -> None:
        """Обновляет статус книги по ID."""
        status = status.lower()
        if status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
            return
        book_to_update = next((book for book in self.books if book["id"] == book_id), None)
        if book_to_update:
            book_to_update["status"] = status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{status}'!")
        else:
            print(f"Книга с ID {book_id} не найдена.")
