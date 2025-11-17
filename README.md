URL Shortener

A simple URL shortening service built with FastAPI, PostgreSQL, Redis, and Docker Compose.
The project supports generating short URLs, redirecting users, and storing basic analytics like click count and timestamps.


Features

Shorten long URLs into a compact short code
Redirect from short URL to original URL
Store URLs in PostgreSQL
Use Redis for fast caching during redirects
Automatically track click count and last access time
Swagger UI for testing the API


Tech Stack

FastAPI
PostgreSQL
Redis
Docker & Docker Compose
SQLAlchemy
Pydantic



How to Run

Make sure Docker Desktop is installed.

docker-compose up --build


FastAPI will be available at:

http://localhost:8000


Swagger UI:

http://localhost:8000/docs




Project Structure
app/
  main.py
  database.py
  models.py
  utils.py
  cache.py
  analytics.py
  routers/
    shorten.py
    redirect.py




