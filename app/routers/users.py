from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

# from app.main import logger
from core.models import Person

router = APIRouter()

@router.get("/reg")
def reg_user_get():
    return FileResponse("templates/html/registration/registration.html")

@router.post("/reg")
def reg_user_post(person: Person):
        # logger.info(f'POST - {person}')
        return {"message": f"Привет, {person.name}"}

@router.get("users/{id}")
def get_user(response: Response, id: int):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect user id"}
    return {"user_id":id}
