# digibot

This is a containerized Python + Flask + Gunicorn shell that can be used to quickly start building a simple backend application.

## Requirements

You need [Docker + Docker Compose](https://docs.docker.com/engine/install/ubuntu/).

## Usage

- Clone repo
- Make desired changes to `docker-compose.yml`
- Do `docker compose up -d`

Your application is now available at the specified port, default is: `localhost:5000`.