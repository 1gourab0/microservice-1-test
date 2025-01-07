from fastapi import FastAPI
import time

app = FastAPI()


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@app.get("/compute")
async def compute(number: int):
    start_time = time.time()
    
    # Perform a heavy computation (e.g., calculating the Fibonacci number)
    result = fibonacci(number)

    end_time = time.time()
    computation_time = end_time - start_time

    return {"result": result, "computation_time": computation_time}
