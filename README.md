# zepto-test-task
## Основные ресурсы API
* `/books/` - книги
* `/authors/` - авторы
* `/books/{book_id}/comments` - комментарии к книгам
## Генерация тестовых данных
Для генерации тестовых данных необходимо набрать команду:  
`python manage.py gen_fake_data [--authors={число авторов}]`
## Тесты
Тесты находятся в папке tests.
Для запуска всех тестов необходимо набрать команду:  
`pytest tests`  
Содержимое тестов можно найти в следующих файлах:  
```
tests  
├── test_accounts_app  
│   ├── endpoints_tests.py # тесты API CRUD  
│   ├── permissions_tests.py # тесты для ограничений доступа (permissions)  
└── test_books_app  
    ├── endpoints_tests.py  
    ├── permissions_tests.py  
 ```
