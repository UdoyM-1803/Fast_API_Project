from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('expenses.json','r') as f:
        data = json.load(p)
    return data

@app.get("/hello")       #Decorator
def hello():
    return "Hi"

@app.get("/about")       
def about():
    return "This is our about page."

@app.get("/view")           # To read our expenses
def view_expenses():
    return "This is our about page."