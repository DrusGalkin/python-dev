import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/', summary='Главный роут', tags=['Роуты'])
def root():
    return {'message': 'Hello Worlder'}


if __name__ == "__main__":
    uvicorn.run("main:aa", reload=True)