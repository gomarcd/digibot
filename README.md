# digibot

This is a basic shell to quickly start building a backend application with:

- Python
- Flask
- Gunicorn
- OpenAI

With this, you can hit the ground running and build using the OpenAI API.

## Requirements

You need [Docker + Docker Compose](https://docs.docker.com/engine/install/ubuntu/).

## Usage

- Clone repo & `cd` into dir
- `mv example.env .env` and fill as needed
- `mv example.docker-compose.yml docker-compose.yml` & change as needed
- Do `docker compose up -d`

Your application is now available at the specified port, default is: `localhost:5000`.

## Customizing

If you want to add or remove parts, just edit the `Dockerfile`. After saving your changes, make sure you build the image anew and then relaunch the container with the new image.

You can do something like:

`docker build --no-cache -t digibot .`

If you are using `docker compose up -d --build` and find that your changes aren't being applied in the new container, you can do something like:

`docker images | grep digibot` and then `docker rmi 038a9be924e5` to remove the old image and then redo your build command.

`docker system prune` can also help for clean up.

## Development server

By default, this comes with a production-ready WSGI server, Gunicorn running on port 5000. That may not necessarily be what you want during development, so one thing you can do without having to change the Dockerfile but still be able to make changes without having to rebuild the container every time, is simply add this `command` to the compose yaml to override the Gunicorn server with the Flask dev server:

```
version: '3'
services:
  digibot:
    build:
      context: .
      dockerfile: Dockerfile
    command: flask --app app run --host=0.0.0.0 --debug
    container_name: digibot
    restart: always
    volumes:
      - "./.env:/app/.env"
      - "./app/app.py:/app/app.py"
    ports:
      - "5000:5000"
```

So you can use that compose yaml in development, and just remove that `command` line in deployment.