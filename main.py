from fastapi import FastAPI ,HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
	id:int
	title:str
	body:str

posts = [{"id":1,"title":"news 1","body":"Text 1"},
		 {"id":2,"title":"news 2","body":"Text 2"},
		 {"id":3,"title":"news 3","body":"Text 3"},]




@app.get("/items")
async def items() ->list[Post]:
	return [Post(**post) for post in posts]

@app.get("/items/{id}")
async def items(id :int) ->Post:
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