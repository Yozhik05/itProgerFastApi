from fastapi import FastAPI ,HTTPException,Path
from typing import Optional, List, Dict,Annotated
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
	id:int
	name:str
	age:int

class Post(BaseModel):
	id:int
	title:str
	body:str
	author:User

class PostCreate(BaseModel):
	title:str
	body:str
	author_id:int

users = [
	{"id":1,"name":"John","age":34},
	{"id":2,"name":"Alex","age":12},
	{"id":3,"name":"Bob","age":45},
]

posts = [{"id":1,"title":"news 1","body":"Text 1","author" :users[1]},
		 {"id":2,"title":"news 2","body":"Text 2","author" :users[0]},
		 {"id":3,"title":"news 3","body":"Text 3","author" :users[2]},
		 ]




@app.get("/items")
async def items() ->list[Post]:
	return [Post(**post) for post in posts]

@app.post("/items/add")
async def add_item(post:PostCreate) ->Post:
	author = next((user for user in users if user["id"] == post.author_id),None)
	if not author:
		raise HTTPException(status_code=404,detail="User not found")
	
	new_post_id = len(posts)+1

	new_post = {"id":new_post_id,"title":post.title,"body":post.body,"author":author}
	posts.append(new_post)

	return Post(**new_post)



@app.get("/items/{id}")
async def items(id :Annotated[int,Path(..., title="Здесь указывается id поста",ge=1,lt=100)]) ->Post:
	for post in posts:
		if post["id"] == id:
			return Post(**post)
		
	raise HTTPException(status_code=404,detail="Post not found")


@app.get("/search/")
async def search(post_id: Optional[int]=None)->Dict[str,Optional[Post]]:
	if post_id:
		for post in  posts:
			if post["id"] == post_id:
				return {"data":Post(**post)}
		raise HTTPException(status_code=404,detail="post not found")
	else:
		return {"data": None}