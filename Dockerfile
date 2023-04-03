FROM python:3.11.2
RUN pip3 install --upgrade pip wheel python-dotenv gunicorn flask Flask-JWT-Extended openai
COPY ./app/* /app/
WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]