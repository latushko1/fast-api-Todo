from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from database import SessionLocal, get_session
from src.todo.models import TodoItem
from src.todo.schemas import TodoCreate

router_todo = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router_todo.get("")
def get_main_page(request: Request, session: Session = Depends(get_session)):
    # return session.query(TodoItem).all()
    try:
        result = session.query(TodoItem).all()
        return {
            "status": "success",
            "data": result,
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })