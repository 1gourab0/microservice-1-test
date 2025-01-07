from fastapi import FastAPI

app = FastAPI()

@app.get("/compute")
async def compute(number: int):
    result = number ** 2  # Simple computation (square the number)
    return {"result": result}
