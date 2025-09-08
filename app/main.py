from fastapi import FastAPI, status, Depends, HTTPException
from post_router import router as post_router
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import auth
app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {"message" : "API is up"}

app.include_router(post_router, prefix="/api/posts")
app.include_router(auth_router)
