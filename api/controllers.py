from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request


app = FastAPI()
templates = Jinja2Templates(directory="templates")

def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request
        }
    )
