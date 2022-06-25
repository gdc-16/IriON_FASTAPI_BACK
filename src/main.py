import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import router
from src.core import get_settings


app = FastAPI(
    title=get_settings().PROJECT_TITLE,
    version=get_settings().PROJECT_VERSION,
    description=get_settings().PROJECT_DESCRIPTION,
)

app.include_router(router=router, prefix="/api")
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=get_settings().ALLOW_ORIGINS,
    allow_credentials=get_settings().ALLOW_CREDENTIALS,
    allow_methods=get_settings().ALLOW_METHODS,
    allow_headers=get_settings().ALLOW_HEADERS,   
)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
