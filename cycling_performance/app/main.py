from fastapi import FastAPI
from contextlib import asynccontextmanager
import sqlite3
from app.routes.user import router

app = FastAPI()

app.include_router(router, prefix="", tags=["user"])
# app.include_router(user.router, prefix="/caracteristic", tags=["caracteristic"])
# app.include_router(user.router, prefix="/test", tags=["test"])