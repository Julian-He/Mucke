from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, htmx_init


api = FastAPI()

@api.get("/library", response_class=HTMLResponse)
async def library():
    html_content = """
    <div class="container-md" id="mainContent">      
        <ul>
            <li>Album1</li>
            <li>Album2</li>
        <ul>
    </div>
    """
    return HTMLResponse(html_content)


api.mount("/frontend", api)
api.mount("/", StaticFiles(directory="src/frontend", html=True))