from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.todo.routers import router_todo
from src.pages.router import pages_router

app = FastAPI(
    title="todo App"
)

app.mount("/static", StaticFiles(directory="./static"), name="static")

app.include_router(router_todo)
app.include_router(pages_router)

