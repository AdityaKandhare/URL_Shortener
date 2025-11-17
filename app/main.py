from fastapi import FastAPI
from app.routers import shorten, redirect
from app.database import Base, engine


app = FastAPI(title="URL Shortener")

Base.metadata.create_all(bind=engine)

app.include_router(shorten.router)
app.include_router(redirect.router)
