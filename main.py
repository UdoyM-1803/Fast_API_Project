from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Annotated, Optional
import json

app = FastAPI()

class Expense(BaseModel):
    id: Annotated[str, Field(..., description="ID of the expenses", example="E001")]
    name: Annotated[str, Field(..., description="Name of the expenses", example="Lunch")]
    amount: Annotated[int, Field(..., description="Amount of the expenses", example="500")]
    category: Annotated[str, Field(..., description="Category of the expenses", example="Food")]
    date: Annotated[str, Field(..., description="Date of the expenses", example="2026-08-01")]
    description: Annotated[str, Field(..., description="Description of the expenses", example="Lunch at the restaurant")]

class ExpenseUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    amount: Annotated[Optional[int], Field(default=None)]
    category: Annotated[Optional[str], Field(default=None)]
    date: Annotated[Optional[str], Field(default=None)]
    description: Annotated[Optional[str], Field(default=None)]

def load_data():                    # Loaded data from expenses.json
    with open('expenses.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('expenses.json','w') as f:
            json.dump(data,f)
    

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


@app.post("/create")
def create_expense(expense: Expense): 
    data = load_data()
    if expense.id in data:
        raise HTTPException(status_code=400, detail="Expense ID already exists")
    data[expense.id] = expense.model_dump(exclude=['id'])
    save_data(data)


@app.put("/edit/{expense_id}")
def update_expense(expense_id: str, expense: ExpenseUpdate): 
    data = load_data()
    if expense_id not in data:
        raise HTTPException(status_code=400, detail="Expense not found")
    data[expense_id].update(expense.model_dump(exclude_unset=True))
    save_data(data)

@app.delete("/delete/{expense_id}")
def delete_expense(expense_id: str): 
    data = load_data()
    if expense_id not in data:
        raise HTTPException(status_code=400, detail="Expense not found")
    del data[expense_id]
    save_data(data)

