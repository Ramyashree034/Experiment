from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="String to Characters")

class TextIn(BaseModel):
    text: str

@app.post("/chars", response_model=List[str])
def string_to_chars(payload: TextIn) -> List[str]:
    s = payload.text
    if len(s.strip()) == 0:
        return ["INVALID STRING"]
    return list(s)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def home():
    return FileResponse("index.html")
