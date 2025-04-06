from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def start_main_page():
    html_content = "<h2>Hello world. App - 'milka-today'<h2>"
    return HTMLResponse(content=html_content)