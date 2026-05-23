from fastapi import FastAPI, HTTPException

app_2 = FastAPI()


@app_2.get("/")
def welcome():
    return {
        "message": "Welcome to Calculator API"
    }


# Calculator API
@app_2.get("/calculate")
def calculate(a: float, b: float, operation: str):

    if operation == "add":
        result = a + b

    elif operation == "sub":
        result = a - b

    elif operation == "mul":
        result = a * b

    elif operation == "div":
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = a / b

    # Power operation
    elif operation == "power":
        result = a ** b

    # Modulus operation
    elif operation == "mod":
        result = a % b

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation"
        )

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }