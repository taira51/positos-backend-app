from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from api.routers import task

app = FastAPI()
app.include_router(task.router)

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO 本番では ["http://localhost:51719"] やドメイン指定が安全
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 文字コード設定
class Utf8Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        content_type = response.headers.get('content-type', '')
        if content_type.startswith('application/json') and 'charset' not in content_type:
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response