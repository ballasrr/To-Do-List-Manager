from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse  # если хочешь вернуть HTML
from typing import Annotated
from app.routers.users import router as users_router
from app.routers.item import router as items_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)



if __name__ == "__main__":
    import uvicorn
    import webbrowser
    import threading
    import time
    # Открываем браузер через секунду после старта сервера
    def open_browser():
        time.sleep(1)
        webbrowser.open("http://127.0.0.1:8000/docs")

    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)