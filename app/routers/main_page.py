from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

router = APIRouter()

# Root
@router.get("/")
def reg_user_get():
    return FileResponse("templates/index.html")