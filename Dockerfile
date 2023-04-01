FROM python:3.11.2
RUN pip3 install --upgrade pip
RUN pip3 install wheel gunicorn flask openai
COPY ./app/* /app/
WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]