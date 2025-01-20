from fastapi import FastAPI
app = FastAPI()

@app.get("/") # defines root for the URL 
def read_root(): 
    return {"Hello": "World"} # returns a JSON response with the dictionary

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# To run the server, use the following command:
## uvicorn --reload --port 8000 main:app
# http://localhost:8000/127.0.0.1%3A8000 HTTP/1.1