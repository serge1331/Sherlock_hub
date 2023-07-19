from fastapi import   Depends, FastAPI
from .collect import collect

app = FastAPI()

app.include_router(collect.router)
