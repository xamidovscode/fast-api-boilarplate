from fastapi import APIRouter
from app.api.endpoints import users, auth


base_v1_router = APIRouter()
base_v1_router.include_router(users.router, tags=["users"])
base_v1_router.include_router(auth.router, tags=["auth"])
