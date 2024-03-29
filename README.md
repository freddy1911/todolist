-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                      
                             Учебный дипломный проект - приложение для планирования целей с реализацией:
                             
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                                
                              Backend stack: 
            
                              1) Django RestFramework
                              2) Python
                              3) Postgres
            
            
            
                              Запуск Проекта:
            
                              1) Клонировать репозиторий по ссылке
                              git clone https://github.com/example
            
                              2) Установка зависимостей:
                              pip install -r requirements.txt
            
                              3) Закатить миграции:
                              ./manage.py makemigrations- создаем миграции
                              ./manage.py migrate - накатываем миграции
            
                              4) Docker build
                              docker pull python:3.10.7-slim
                              poetry add gunicorn - установка gunicorn
                              docker-compose up -d db - запуск базы
                              docker-compose down - останавливаем базу
                              docker-compose up --build - сборка образа
                              docker-compose up  - поднимаем образ
                              python manage.py runserver - запуск сервера
                              docker-compose exec api /bin/bash - вход в контейнер
                              ls -la - просмотр что содержит
            
                              5) Создаем Суперпользователя:
                              python manage.py createsuperuser
            
                              6) Запустить проект
            
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
О самом приложений
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

1) Вход/регистрация/аутентификация через вк.
2) Создание целей.
3) Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
4) Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
5) Выбор приоритета цели (статичный список minor, major, critical и т. п.).
6) Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).
7) Изменение целей.
8) Изменение описания цели.
9) Изменение статуса.
10) Дать возможность менять приоритет и категорию у цели.
11) Удаление цели. При удалении цель меняет статус на «в архиве».
12) Поиск по названию цели.
13) Фильтрация по статусу, категории, приоритету, году.
14) Выгрузка целей в CSV/JSON.
15) Заметки к целям.
16) Реализован функционал "Доска" с возможностью добавлять в нее нескольких пользователей.
17) Создан ТГ бот с возможностью просмотра целей, категорий пользователя, возможность создавать новые цели.
