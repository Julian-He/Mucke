from uuid import UUID
from typing import List
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.data import AlbumReview, AppData, ReviewProcess, User, Album
from backend.usecases import review_process, search, review

appdata = AppData([], [])
api = FastAPI()
templates: Jinja2Templates = Jinja2Templates("./frontend/templates")


@api.get("/login", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html", context={"name_taken": False}
    )


@api.post("/library", response_class=HTMLResponse)
async def library(request: Request, user: str = Form(...)):
    person = search.search_users(appdata, user)[0]
    reviews = search.all_reviews_of_user(appdata, person)

    return templates.TemplateResponse(
        request=request,
        name="library.html",
        context={"userName": user, "reviews": reviews},
    )


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


@api.post("/start-review", response_class=HTMLResponse)
async def start_review(request: Request, user: str = Form(...)):
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
        request=request,
        name="reviewProcess.html",
        context={"review_process": review_proc, "username": user},
    )


@api.post("/search-users", response_class=HTMLResponse)
async def search_users(request: Request, name: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="userList.html",
        context={"users": search.search_users(appdata, name)},
    )


@api.post("/add-user-to-review", response_class=HTMLResponse)
async def add_user_to_review(
    request: Request, processID: str = Form(...), userName: str = Form(...)
):
    review_process.add_user(
        appdata, UUID(processID), search.search_users(appdata, userName)[0]
    )
    return templates.TemplateResponse(
        request=request,
        name="reviewProcess.html",
        context={
            "review_process": search.search_review_processes(appdata, UUID(processID)),
            "username": userName,
        },
    )


@api.post("/reviews", response_class=HTMLResponse)
async def reviews(request: Request, user: str = Form(...)):
    person: User = search.search_users(appdata, user)[0]
    return templates.TemplateResponse(
        request=request,
        name="reviews.html",
        context={
            "userName": user,
            "processes": [
                process
                for process in appdata.review_processes
                if person in process.participants
            ],
        },
    )


@api.post("/review/{review_id}", response_class=HTMLResponse)
async def view_review(request: Request, review_id: str, user: str = Form(...)):
    process = search.search_review_processes(appdata, UUID(review_id))
    person: User = search.search_users(appdata, user)[0]
    if process is not None:
        have_already_suggested: List[User] = [
            review.suggested_by for review in process.reviews
        ]
    else:
        have_already_suggested: List[User] = []

    if person in have_already_suggested:
        return templates.TemplateResponse(
            request=request,
            name="reviewProcess.html",
            context={"review_process": process, "username": user},
        )
    else:
        return templates.TemplateResponse(
            request=request,
            name="joinReview.html",
            context={
                "username": user,
                "process_id": review_id,
            },
        )


@api.post("/join-review-process", response_class=HTMLResponse)
async def join_review_process(
    request: Request,
    user: str = Form(...),
    process_id: str = Form(...),
    album: str = Form(...),
    artist: str = Form(...),
):
    process = search.search_review_processes(appdata, UUID(process_id))
    person: User = search.search_users(appdata, user)[0]
    release: Album = Album(album, artist)

    review_process.join_review(appdata, UUID(process_id), person, release)

    return templates.TemplateResponse(
        request=request,
        name="reviewProcess.html",
        context={"review_process": process, "username": user},
    )


@api.post("/album-review/{id}", response_class=HTMLResponse)
def review_album(
    request: Request,
    id: str,
    user: str = Form(...),
    processID: str = Form(...),
):
    person: User = search.search_users(appdata, user)[0]
    process = search.search_review_processes(appdata, UUID(processID))
    if process is not None:
        review = search.search_album_review(process, UUID(id))
    else:
        review = None

    return templates.TemplateResponse(
        request=request,
        name="albumReview.html",
        context={"username": user, "review_process": process, "review": review},
    )


@api.post("/submit-review", response_class=HTMLResponse)
def submit_review(
    request: Request,
    processID: str = Form(...),
    reviewID: str = Form(...),
    user: str = Form(...),
    rating: str = Form(...),
    writtenReview: str = Form(...),
):
    person = search.search_users(appdata, user)[0]
    review.submit(
        appdata, UUID(processID), UUID(reviewID), person, int(rating), writtenReview
    )

    process = search.search_review_processes(appdata, UUID(processID))
    if process is not None:
        rev = search.search_album_review(process, UUID(reviewID))
    else:
        rev = None

    return templates.TemplateResponse(
        request=request,
        name="albumReview.html",
        context={"review_process": process, "username": user, "review": rev},
    )


api.mount("/frontend", api)
api.mount(
    "/",
    StaticFiles(directory="./frontend", html=True),
)
