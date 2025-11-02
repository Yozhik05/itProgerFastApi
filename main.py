from fastapi import FastAPI ,HTTPException


app = FastAPI()

@app.get("/")
async def home()->dict[str,str]:
	return {"message": "Hello World"}


@app.get("/contacts")
async def contacts() ->int:
	return 34

posts = [{"id":1,"title":"news 1","body":"Text 1"},
		 {"id":2,"title":"news 2","body":"Text 2"},
		 {"id":3,"title":"news 3","body":"Text 3"},]


@app.get("/items")
async def items() ->list:
	return posts

@app.get("/items/{id}")
async def items(id :int) ->dict:
	for post in posts:
		if post["id"] == id:
			return post
		
	raise HTTPException(status_code=404,detail="Post not found")