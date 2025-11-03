from pydantic import BaseModel

class UserBase(BaseModel):
	name:str
	age:int
	
class UserCreate(BaseModel):
	pass

class User(UserBase):
	id:int
	
    class Config:
        orm_mode = True

class PostBase(BaseModel):
	id:int
	body:str
	author_id:int

class PostCreate(PostBase):
	pass

class Past(PostBase):
	id:int
	
    class Config:
        orm_mode=True

    