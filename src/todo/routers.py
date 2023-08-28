from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND
from starlette.templating import Jinja2Templates

from database import SessionLocal, get_session
from src.todo.models import TodoItem
from src.todo.schemas import TodoCreate

router_todo = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

templates = Jinja2Templates(directory="templates")


@router_todo.get("/page")
def get_main_page(request: Request, session: Session = Depends(get_session)):
    result = session.query(TodoItem).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "todos": result})


@router_todo.get("/update/{todo_id}", response_model=TodoCreate)
def update_todo(todo_id: int, session: Session = Depends(get_session)):
    todo_item = session.query(TodoItem).filter_by(id=todo_id).first()
    todo_item.is_active = not todo_item.is_active
    session.commit()

    url = router_todo.url_path_for("get_main_page")
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@router_todo.post("/add")
def add_todos(title: str = Form(...), session: Session = Depends(get_session)):
    new_todo = TodoItem(text=title)
    session.add(new_todo)
    session.commit()

    url = router_todo.url_path_for("get_main_page")
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@router_todo.get("/delete/{todo_id}")
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo_item = session.query(TodoItem).filter_by(id=todo_id).first()
    session.delete(todo_item)
    session.commit()

    url = router_todo.url_path_for("get_main_page")
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)

