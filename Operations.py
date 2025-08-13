from typing import Optional
import fastapi
from fastapi import HTTPException
from pydantic import BaseModel
from ReadSave import readBookStore,writeToBookStore

router = fastapi.APIRouter()

booksData = readBookStore()

class createBookStoreData(BaseModel):
    title: str
    author:  str
    category: str

class updateBookStoreData(BaseModel):
    title: str
    author:  Optional[str] = None
    category: Optional[str] = None


@router.get('/')
async def welcome():
    return {'Response':'Welcome to data store'}

@router.get('/{getBook}')
async def getBookData(getBook:int):
    if getBook < 0 or getBook >= len(booksData):
        raise HTTPException(status_code=404,detail='Data Not Found')
    return booksData[getBook]

@router.get('/{getAllBooks}/')
async def getAllBooks():
    return booksData

@router.post('/{createData}/')
async def createData(createBookData:createBookStoreData):

    for book in booksData:
        if (
            book['title'].lower() == createBookData.title.lower() and
            book['author'].lower() == createBookData.author.lower() and
            book['category'].lower() == createBookData.category.lower()
        ):
            return {'response':'data already exists'}

    booksData.append(createBookData.dict())
    writeToBookStore(booksData)
    return {'Response': createBookData}

@router.put('/update/')
async def updateData(updateBookData:updateBookStoreData):
    for book in booksData:
        if book['title'].lower() == updateBookData.title.lower():
            if updateBookData.author is not None:
                book['author'] = updateBookData.author
            if updateBookData.category is not None:
                book['category'] = updateBookData.category
            writeToBookStore(booksData)
            return book

    raise HTTPException(status_code=404, detail='data not found')

@router.delete('/delete/{deleteData}')
async def deleteData(deleteData:str):
    for index, data in enumerate(booksData):
        if deleteData.lower() == data['title'].lower() :
            delData = booksData.pop(index)
            writeToBookStore(booksData)
            return {'Response':'deleted successfully','deletedData':delData}
    raise HTTPException(status_code=400,detail='data not found')
