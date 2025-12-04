# BryanHadro.com

My blog website, written in Python/Django.

# Setup

Setup Python virtual environment, install packages restructure the default:

    make setup
    make startproject

Start the server:

    make serve

# Docker

## Initial Setup

    docker compose build

If you wish to check current python packages:

    docker compose run web pip "freeze"

## Serve

    docker compose up

## Troubleshooting

Make changes, then run:

    docker compose down -v
    docker compose build --no-cache
    docker compose up

