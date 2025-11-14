def calculator(x: int,y: int, operator: str):
    if operator == "substract":
        return x - y
    elif operator == "divide":
        return x / y
    else:
        return x + y