from fastapi import FastAPI, HTTPException, Path
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

@app.get("/view/{expense_id}")           # To read our expenses
def view_specific_expense(expense_id: str = Path(..., description="ID of the expenses", example="E001")): 
    data = load_data()
    if expense_id in data:
        return data[expense_id]
    else:
        raise HTTPException(status_code=404, detail="Expense not found")