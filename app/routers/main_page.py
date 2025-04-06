from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
def reg_user_get():
    return FileResponse("templates/html/main_page/index.html")