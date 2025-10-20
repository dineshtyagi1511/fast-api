from fastapi import FastAPI
import json 

app = FastAPI()

def load_data():
    with open("patients.json","r")as f :
        data = json.load(f)

    return data



@app.get("/")
def hello():
    return {"message":"Patient Management system api "}

@app.get("/about")
def about():
    return {"message":"a fully functional API "}

@app.get("/view")
def view():
    data_ = load_data()
    return data_