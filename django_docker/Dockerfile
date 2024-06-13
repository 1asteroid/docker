
FROM python:3.12

WORKDIR /app

COPY . /app


RUN pip install -r requirements.txt

# Django migration va statik fayllarni yig'ish



# Ilovani ishga tushirish uchun buyruqni aniqlash
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]