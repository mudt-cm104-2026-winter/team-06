"""Movie Ratings: our team project for CM-104.

Users enter a movie title, a rating from 1 to 5 and their name.
The app keeps the ratings and shows them in a table.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the ratings are kept
- templates/   the HTML page
- static/      the stylesheet
"""

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Movie Ratings")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):
    """The start page: the form and all entries."""
    return templates.TemplateResponse(
        request, "index.html", {"entries": storage.all_entries()}
    )


@app.post("/add")
def add(title: str = Form(...), rating: int = Form(...), person: str = Form(...)):
    """The form on the start page sends its fields here."""
    storage.add_entry(title=title.strip(), rating=rating, person=person.strip())
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)
