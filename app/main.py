from fastapi import FastAPI

app = FastAPI(
    title="To-Do List Manager",
    version="1.0.0",
    description="Простой CRUD для задач"
)

@app.get("/")
def root():
    return {"message": "Сервер запущен! Swagger: http://127.0.0.1:8000/docs"}