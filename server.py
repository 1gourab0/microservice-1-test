from fastapi import FastAPI
import time

app = FastAPI()


def fibonacci(n: int) -> int:
    # This function computes the nth Fibonacci number using a naive recursive approach
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@app.get("/compute")
async def compute(number: int):
    start_time = time.time()
    
    # Perform a heavy computation (e.g., calculating the Fibonacci number)
    result = fibonacci(number)

    end_time = time.time()
    computation_time = end_time - start_time

    return {"result": result, "computation_time": computation_time}
