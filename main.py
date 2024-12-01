from Library import Library  

SEARCH_FIELDS = {
    "1": "title",
    "2": "author",
    "3": "year"
}

STATUS_OPTIONS = {
    "1": "в наличии",
    "2": "выдана"
}

MENU_OPTIONS = {
    "1": "Добавить книгу",
    "2": "Удалить книгу",
    "3": "Поиск книги",
    "4": "Показать все книги",
    "5": "Изменить статус книги",
    "6": "Выйти"
}

def display_menu():
    """Отображает меню для пользователя."""
    menu_content = "\n==================================\n" \
                   "        Управление Библиотекой\n" \
                   "==================================\n" \
                   + "\n".join(f"{key}. {value}" for key, value in MENU_OPTIONS.items()) + \
                   "\n=================================="
    print(menu_content)


def get_user_choice(options: dict, prompt: str) -> str:
    """Получает выбор пользователя из списка вариантов."""
    while True:
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input(f"{prompt}: ").strip()
        if choice in options:
            return choice
        print("Некорректный выбор. Попробуйте снова.")

def main():
    """Основной цикл программы."""
    library = Library("library.json")

    while True:
        display_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":  
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = input("Введите год издания книги: ").strip()
            library.add_book(title, author, year)

        elif choice == "2":  
            try:
                book_id = int(input("Введите ID книги для удаления: ").strip())
                library.delete_book(book_id)
            except ValueError:
                print("Некорректный ID. Введите число.")

        elif choice == "3":  
            field_choice = get_user_choice(SEARCH_FIELDS, "Выберите поле для поиска")
            field = SEARCH_FIELDS[field_choice]
            value = input(f"Введите значение для поиска по '{field}': ").strip()
            results = library.search_books(field, value)

            if results:
                for book in results:
                    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                          f"Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книги не найдены.")

        elif choice == "4":  
            library.display_books()

        elif choice == "5":  
            try:
                book_id = int(input("Введите ID книги для изменения статуса: ").strip())
                status_choice = get_user_choice(STATUS_OPTIONS, "Выберите новый статус книги")
                status = STATUS_OPTIONS[status_choice]
                library.update_status(book_id, status)
                print(f"Статус книги с ID {book_id} успешно обновлен на '{status}'.")
            except ValueError:
                print("Некорректный ID. Введите число.")

        elif choice == "6":  # Выйти
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
