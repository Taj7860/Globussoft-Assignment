from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def hello(name: str = "Guest"):
    return {f"Welcome to Fast API: {name}"}