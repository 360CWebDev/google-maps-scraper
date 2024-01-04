#from src import Gmaps
#import requests

#import os
#url = os.environ
#print(url)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query/{queryString}")
async def read_item(queryString):
    return {"query": queryString}

#queries = [
#   "web developers in austin texas"
#]

#Gmaps.places(queries, max=5)
