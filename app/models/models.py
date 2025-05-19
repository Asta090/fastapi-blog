
from sqlmodel import Field, Session, SQLModel, Relationship
from typing import Optional,List

class Blog(SQLModel, table=True):
    __tablename__ = "blogs"
    id: int | None = Field(default=None, primary_key=True)
    title :str = Field(index=True)
    body :str = Field(index=True)
    user_id: int = Field(default=None, foreign_key="users.id")
    creator: "User" = Relationship(back_populates="blogs")

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(index=True)
    blogs: List["Blog"] = Relationship(back_populates="creator")
