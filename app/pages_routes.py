from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home_page(request:Request):
    return templates.TemplateResponse(name = "home.html", request = request)


# @router.get("/about", response_class=HTMLResponse)
# async def home_page(request:Request):
#     return templates.TemplateResponse(name = "about.html", request = request)


# @router.get("/contact", response_class=HTMLResponse)
# async def home_page(request:Request):
#     return templates.TemplateResponse(name = "contact.html", request = request)
