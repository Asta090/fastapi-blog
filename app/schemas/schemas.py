from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
  title: str
  body: str

class Blog(BlogBase):
  class Config:
    orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str


# For creating a user
class User(UserBase):
    password: str


# For showing user without blogs
class UserDisplay(UserBase):
    class Config:
        orm_mode = True

# For showing blog with creator but without nested blogs
class ShowBlog(BlogBase):
    creator: UserDisplay

    class Config:
        orm_mode = True


# For showing user with their blogs
class ShowUser(UserBase):
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

class login(BaseModel):
    Username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
