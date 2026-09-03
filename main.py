from fastapi import FastAPI
import json

app = FastAPI()

def load_data():                    # Loaded data from expenses.json
    with open('expenses.json','r') as f:
        data = json.load(f)
    return data

@app.get("/hello")       #Decorator
def hello():
    return "Hi"

@app.get("/about")       
def about():
    return "This is our about page."

@app.get("/view")           # To read our expenses
def view_expenses():
    data = load_data()
    return data