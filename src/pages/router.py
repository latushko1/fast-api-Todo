from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.todo.routers import get_main_page

pages_router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@pages_router.get("/base")
def get_base_page(request: Request, todos=Depends(get_main_page)):
    return templates.TemplateResponse("base.html", {"request": request, "todos": todos["data"]})

@pages_router.get("/base/add")
def get_base_page(request: Request, todos=Depends(get_main_page)):
    return templates.TemplateResponse("add.html", {"request": request, "todos": todos["data"]})