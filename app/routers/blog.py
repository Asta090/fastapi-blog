from fastapi import APIRouter,status, Depends, HTTPException
from typing import List
from .. import schemas, models, oauth2
from ..database import SessionDep
from sqlmodel import select
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)


@router.get("/",response_model=List[schemas.ShowBlog])
def read_blogs(
    session: SessionDep,  # Move this first since it has no default value
    current_user: models.User = Depends(oauth2.get_current_user)  # Move this second since it has a default value
   ):
    blogs = session.query(models.Blog).all()
    return blogs



@router.get("/{blog_id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def read_blog(blog_id: int, session: SessionDep
    , current_user: models.User = Depends(oauth2.get_current_user)):
    # Get blog post by ID
    blog = session.get(models.Blog, blog_id)
    if not blog:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
 
    return blog

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,session : SessionDep,
    current_user: models.User = Depends(oauth2.get_current_user)):
  db_blog=models.Blog(title=request.title,body=request.body,user_id=1)
  session.add(db_blog)
  session.commit()
  session.refresh(db_blog)
  return db_blog  


@router.put("/{blog_id}", status_code=status.HTTP_200_OK)
def update_blog(blog_id: int, request: schemas.Blog, session: SessionDep,
    current_user: models.User = Depends(oauth2.get_current_user)):
    db_blog = session.get(models.Blog, blog_id)
    if not db_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                          detail=f"Blog with id {blog_id} not found")
    
    # Update only the fields defined in your model
    db_blog.title = request.title
    db_blog.body = request.body
    
    session.commit()
    session.refresh(db_blog)
    return db_blog


@router.delete("/{blog_id}")
def delete_blog(blog_id: int, session: SessionDep,
    current_user: models.User = Depends(oauth2.get_current_user)):
    db_blog = session.get(models.Blog, blog_id)
    if not db_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    
    session.delete(db_blog)
    session.commit()
    return {"message": "Blog deleted"}