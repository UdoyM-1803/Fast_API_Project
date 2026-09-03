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


@app.get("/sort")           # To sort the data     
def view_sorted_expenses(sorted_by: str, order: str):
    data = load_data()

    sorted_data = list(data.values())
    def get_value(expense):
        return expense[sorted_by]

    if order == 'asc':
        sorted_data.sort(key= get_value)
    elif order == 'desc':
        sorted_data.sort(key= get_value, reverse=True)
    else:
        return "Order not Matched"

    # ----------------Alternative--------------------
    # sorted_data.sort(key= lambda x: x[sorted_by])
    # -------------------------X----------------------
    return sorted_data