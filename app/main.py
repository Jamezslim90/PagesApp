from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.pages_routes import  *
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include routers

app.include_router(router)
