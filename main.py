from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")       #Decorator
def view():
    return "Hi"

@app.get("/about")       #Decorator
def view():
    return "This is our about page."