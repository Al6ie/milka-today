from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

# from app.main import logger
from core.models import Person

router = APIRouter()

#Страница с регистрацией
@router.get("/reg")
def reg_user_get():
    return FileResponse("templates/registration.html")

#Получение регистрационных данных
@router.post("/reg")
def reg_user_post(person: Person):
        return {"message": f"Привет, {person.name}"}

#Переход к пользователю
@router.get("users/{id}")
def get_user(response: Response, id: int):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect user id"}
    return {"user_id":id}
