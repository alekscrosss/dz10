# Используйте официальный образ Python как основу
FROM python:3.11

# Установите рабочую директорию в контейнере
WORKDIR /usr/src/app

# Скопируйте файл зависимостей и установите зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте исходный код проекта в контейнер
COPY . .

# Откройте порт, на котором работает Django
EXPOSE 8000

# Запустите сервер разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
