# Документация

# Файл main.py
1. Модуль:
   Строка from Library import Library выполняет импорт класса Library из модуля Library.
   - from Library озночает, что Python будет искать файл в катологе проекта или путях, указанных в переменной PYTHONPATH.
   - Если файл не найден поиск будет в стандартной библиотеке, либо в установленных.
   import Library - импорт конкретного объекта с именем Library из модула Library.

2. Константы:

```python
    # Словари с возможными полями для поиска и статусами книг
SEARCH_FIELDS = {
    "1": "title",   # Поиск по названию
    "2": "author",  # Поиск по автору
    "3": "year"     # Поиск по году издания
}

STATUS_OPTIONS = {
    "1": "в наличии",  # Статус "в наличии"
    "2": "выдана"      # Статус "выдана"
}

MENU_OPTIONS = {
    "1": "Добавить книгу",  # Добавить книгу
    "2": "Удалить книгу",   # Удалить книгу
    "3": "Поиск книги",     # Поиск книги
    "4": "Показать все книги", # Показать все книги
    "5": "Изменить статус книги",  # Изменить статус книги
    "6": "Выйти"           # Выйти из программы
}
```

  - SEARCH_FIELDS - словарь, в котором отображает числовые опции для поиска книг по известным полям: название, автор и год.
  - STATUS_OPTIONS - словарь с возможными статусами книг.
  - MENU_OPTIONS - словарь с доступными основновными действиями в меню программы.

3. Функции:
    -  display_menu() - отображает доступные опции в меню программы.
    -  get_user_choice(options: dict, prompt: str) -> str - получает выбор пользователя из списка вариантов. Применяется для получения выбора поля для поиска и статуса книги.
    -  main() - основная функция программы; отвечает за выбор пользователя, вызывает соответствующие методы для добавления, удаления, поиска и изменения статуса книги.
4. Пример использования:
   Для использования достаточно запустить main и следовать действиям, появившимся в консоли.
   
# Файл Library.py
Класс Library представляет собой системой для управления библиотекой (добавление книги, удаление книги, поик книг, отображение всех книг в библиотеке и изменение статуса книги).
 __init__(self, data_file: str = "library.json") -> None - Конструктор класса, инициализирует объект библиотеки и загружает книги из файла.

data_file (str) - путь к файлу, содержащему данные для библиотеки по умолчанию используется - library.json
save_books(self) -> None - Сохраняет данные о книгах в файл JSON.

1. add_book(self, title: str, author: str, year: str) -> None - Добавляет новую книгу в библиотеку.

Параметры:

title (str): Название книги.
author (str): Автор книги.
year (str): Год выпуска книги.
Возвращаемое значение: None

Примечание: Книга добавляется с уникальным ID, который равен количеству книг в списке плюс один. Статус книги изначально устанавливается как "в наличии"

 1. Добавлять книги — пользователь может добавить новую книгу в библиотеку, указав её название, автора и год издания (title, author, year).
    
 2. Удалять книги — удаление книги из библиотеки по уникальному идентификатору (ID).

 3. Искать книги — поиск книг по трём параметрам:
     - Название книги (title),
     - Автор книги (author),
     - Год издания книги (year).

4. Пользователь выбирает поле для поиска (title, author, year), вводит значение и получает список книг.
5. Просматривать список книг — пользователь может вывести на экран полный список всех книг в библиотеке с их данными (ID, название, автор, год, статус).
6. Изменять статус книги — пользователь может изменить статус книги (например, "в наличии" или "выдана"). Для этого нужно ввести ID книги и выбрать новый статус.
7. Выход из программы — выход из приложения.

# Описание функционала приложения для управления библиотекой

 Консольное приложение для управления библиотекой представляет собой программу, которая даёт возможность пользователю выполнять различные действия с книгами, например, их можно добавить, удалить, искать в библиотеке, обновить их статус (в наличии или выдана) и отобразить список всех книг. Основой приложения является класс Library, который управляет данными о книгах, хранящимися в файле JSON.

Основные компоненты приложения:

1. Класс Library:
  - Отвечает за управление книгами в библиотеке, включая их сохранение и загрузку из файла, а также реализует функционал добавления, удаления, поиска, обновления статуса и отображения книг.
2. Функции интерфейса:
  - Обеспечиваются посредством взаимодействия с пользователем через командное меню.

Описание функционала:

- Добавление книги:
  Пользователь может добавить новую книгу в библиотеку, предоставив название, автора и год издания.
Книга сохраняется с уникальным ID, который автоматически присваивается на основе количества уже существующих книг в библиотеке.
Cтатус книги изначально устанавливается как "в наличии".

- Удаление книги:

  Пользователь может удалить книгу, указав её ID.
Если книга с заданным ID не найдена, выводится сообщение об ошибке.

- Поиск книги:

  Пользователь может искать книгу по полям: название, автор и год издания.
Программа выводит все книги, удовлетворяющие критериям поиска. Если книги не найдены, выводится соответствующее сообщение.

- Отображение списка книг:

  Пользователь может просмотреть весь список книг, находящихся в библиотеке.
Если библиотека пуста, выводится сообщение об этом.

- Изменение статуса книги:

  Пользователь может изменить статус книги, указав её ID и новый статус ("в наличии" или "выдана").
Если статус некорректен, программа уведомляет об этом.

- Выход из программы:

  Пользователь может завершить работу программы.

  # Разбор кода

1. Импорты и типы данных:
    json используется для работы с файлом данных в формате JSON.
typing импортирует типы для аннотации аргументов и возвращаемых значений.
Тип данных Book определяет структуру книги как словарь (Dict) с ключами и значениями (строка или число) - Book = Dict[str, Union[int, str]]

2. Класс Library:
-  __init__(self, data_file: str = "library.json"): Инициализирует объект библиотеки и загружает данные из указанного файла.
- load_books(self): Загружает книги из файла. Если файл отсутствует или его содержимое некорректно, создается новая пустая библиотека.
- save_books(self): Сохраняет список книг в файл JSON.
a dd_book(self, title: str, author: str, year: str): Добавляет новую книгу в библиотеку.
- delete_book(self, book_id: int): Удаляет книгу по ID.
- search_books(self, key: str, value: str): Выполняет поиск книг по заданному ключу и значению.
- display_books(self): Печатает список всех книг.
- update_status(self, book_id: int, status: str): Обновляет статус книги по ID.

3. Функции интерфейса:

- display_menu()- пчатает меню с доступными действиями.
- get_user_choice(options: dict, prompt: str)- запрашивает у пользователя выбор из заданных вариантов и возвращает выбранное значение.
- main()- основная функция, реализующая цикл программы, в котором пользователь может выбирать действия и взаимодействовать с библиотекой.
5. Основные элементы интерфейса
- Меню (MENU_OPTIONS) - пункты меню, соответствующие действиям: добавление книги, удаление книги, поиск, отображение списка, изменение статуса и выход.

Поля поиска (SEARCH_FIELDS) - определяют поля, по которым можно искать книги: название, автор, год издания.

Опции статуса (STATUS_OPTIONS) - возможные статусы книги: "в наличии" и "выдана".

6. Пример работы программы
  - Добавление книги:
Появляется запрос на ввод названия, автора и года издания книги. После ввода данных о книге, программа добавляет её в библиотеку и сохраняет изменения.

  - Удаление книги:
Появляется запрос на ввод ID книги. Если ID найден, книга удаляется; если нет — выводится сообщение об ошибке.
  
  - Поиск книги:
Появляется запрос на выбор поля (title, author, year) для поиска и ввод значения. Программа выводит книги, подходящие под критерии поиска.

  - Изменение статуса книги:

Появляется запрос на ввод ID книги и новый статус ("в наличии" или "выдана"). Статус обновляется, если введенные данные корректны.

  - Отображение списка книг:

Печатается полный список книг с их ID, названием, автором, годом издания и статусом.



#Пример использования программы
```
==================================
        Управление Библиотекой
==================================
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Показать все книги
5. Изменить статус книги
6. Выйти
==================================
```
Выберите действие: 1
Введите название книги: Золотые яблоки солнца
Введите автора книги: Рэй Брэдбери
Введите год издания книги: 2023
Книга 'Золотые яблоки солнца' успешно добавлена!
