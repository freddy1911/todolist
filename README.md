                     todolist - Приложение для отслеживания выполнения задач
                     
                                
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
            
            
