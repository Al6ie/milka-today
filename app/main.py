import uvicorn
import logging
from fastapi import FastAPI

from routers import users
from routers import main_page

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

app = FastAPI()

app.include_router(users.router, tags=["Users"])
app.include_router(main_page.router, tags=["Main Page"])

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)