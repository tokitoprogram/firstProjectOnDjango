# Используем базовый образ Python
FROM python:3.12

# Устанавливаем переменную окружения для не вывода сообщений от Python
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри Docker контейнера
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install django

# Копируем код проекта
COPY . /app/

# Выполняем миграции и собираем статические файлы Django
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Определяем команду, которую Docker будет выполнять при запуске контейнера
CMD ["gunicorn", "metanit.wsgi:application", "--bind", "0.0.0.0:8000"]