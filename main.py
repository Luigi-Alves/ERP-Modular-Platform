from fastapi import FastAPI


app = FastAPI()




@app.get("/")
def home():
    return {"menssagem": "Hello World"}