import uvicorn
from typing import List
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .backend.data import AppData, ReviewProcess, User, Album
from .backend.usecases import review_process, search

appdata = AppData([], [])
api = FastAPI()
templates: Jinja2Templates = Jinja2Templates(
    "C:\\Users\\Julian\\Desktop\\Mucke\\src\\frontend\\templates"
)


@api.get("/login", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html", context={"name_taken": False}
    )


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


@api.post("/homepage", response_class=HTMLResponse)
async def login(request: Request, name: str = Form(...)):
    if name in [user.name for user in appdata.users]:
        return templates.TemplateResponse(
            request=request, name="login.html", context={"name_taken": True}
        )

    else:
        appdata.users.append(User(name, []))
        return templates.TemplateResponse(
            request=request,
            name="homepage.html",
            context={"username": name, "header": name},
        )


@api.get("/start-review", response_class=HTMLResponse)
async def start_review(request: Request, user: str):
    return templates.TemplateResponse(
        request=request,
        name="startReview.html",
        context={"username": user},
    )


@api.post("/start-review-process", response_class=HTMLResponse)
async def start_review_process(
    request: Request,
    user: str = Form(...),
    album: str = Form(...),
    artist: str = Form(...),
):
    host: User = search.search_users(appdata, user)[0]
    id = review_process.start_review_process(appdata, host, Album(album, artist))
    review_proc = search.search_review_processes(appdata, id)

    return templates.TemplateResponse(
        request=request, name="review.html", context={"review_process": review_proc}
    )


api.mount("/frontend", api)
api.mount(
    "/",
    StaticFiles(
        directory="C:\\Users\\Julian\\Desktop\\Mucke\\src\\frontend", html=True
    ),
)
