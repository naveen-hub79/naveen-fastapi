from datetime import datetime
from pydantic import BaseModel, EmailStr
class BasePost(BaseModel):
  title: str
  content: str
  published: bool = True

class PostCreate(BasePost):
  pass

class Post(BasePost):
  id: int
  created_at: datetime

  class Config:
    orm_mode = True

class UserCreate(BaseModel):
  email: EmailStr
  password: str

class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime
  class Config:
    orm_mode = True

