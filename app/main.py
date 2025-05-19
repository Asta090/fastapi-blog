from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine,SessionDep
from sqlmodel import Session, SQLModel

from app.routers import blog,user,authentication


app = FastAPI()

app.add_middleware(  
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



