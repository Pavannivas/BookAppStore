import uvicorn
from fastapi import FastAPI
import Operations


app = FastAPI()

app.include_router(Operations.router)


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)