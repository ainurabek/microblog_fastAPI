from typing import List

from fastapi import FastAPI, Query, Path, Body
from schemas import Books, Author, AuthorOut

app = FastAPI()

@app.post('/book_create',)
def book_create(item:Books, author:Author, quantity:int= Body(...)):
    return {'book':item, 'author':author, 'quantity':quantity}

@app.post('/author_create', response_model=AuthorOut, response_model_exclude_unset=True)
def author_create(author:Author=Body(..., embed=True)):
    return AuthorOut(**author.dict(), id=3)

@app.get('/book')
def get_book(q: List[str]=Query('test', max_length=5, min_length=2, description="Search book")):
    return q

@app.get('/book/{pk}')
def get_single_book(pk:int =Path(..., gt=1, le=20), pages:int=Query(None, gt=10, le=500)): #значения д.б больще 1го
    return {'pk':pk, 'pages':pages}