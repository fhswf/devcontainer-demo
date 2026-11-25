import sys
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hallo():
    return {"nachricht": "Hallo aus dem Dev Container", "python": sys.version}
