from typing import Union

from fastapi import FastAPI

import redis
r = redis.Redis(host="redis", port=6379)
app = FastAPI()

import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Do you know the Irish whiskey paddy and can you tell me some cocktail recipes with it?"}])
# print(completion.choices[0].message.content)




@app.get("/")
def read_root():
    return {"Hello": completion.choices[0].message.content}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"Number of hits:": r.get("hits")}