FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install -v -r /app/requirements.txt
CMD python manage.py runserver 0.0.0.0:8000