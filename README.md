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

- Clone repo
- Make desired changes to `docker-compose.yml`
- Do `docker compose up -d`

Your application is now available at the specified port, default is: `localhost:5000`.

## Customizing

If you want to add or remove parts, just edit the `Dockerfile`. After saving your changes, make sure you build the image anew and then relaunch the container with the new image.

You can do something like:

`docker build --no-cache -t digibot .`

If you are using `docker compose up -d --build` and find that your changes aren't being applied in the new container, you can do something like:

`docker images | grep digibot` and then `docker rmi 038a9be924e5` to remove the old image and then redo your build command.

`docker system prune` can also help for clean up.