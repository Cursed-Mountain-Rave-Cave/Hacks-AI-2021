from typing import Optional

from fastapi import FastAPI

from .routers import hello_router, certificates_router

app = FastAPI()

app.include_router(hello_router)
app.include_router(certificates_router)
