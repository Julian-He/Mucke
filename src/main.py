from typing import List
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.data import User

users: List[User] = []
api = FastAPI()
templates: Jinja2Templates = Jinja2Templates("frontend/templates")

@api.get("/library", response_class=HTMLResponse)
async def library(request: Request):
    html_content = """
    <div class="container-md" id="mainContent">      
        <ul>
            <li>Album1</li>
            <li>Album2</li>
        <ul>
    </div>
    """
    return HTMLResponse(html_content)

@api.post("/login", response_class=HTMLResponse)
async def login(request: Request, name: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="homepage.html",
        context={"header": name}
    )
        

api.mount("/frontend", api)
api.mount("/", StaticFiles(directory="frontend", html=True))