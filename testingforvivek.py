def calculator(x: int,y: int, operator: str):
    if operator == "substract":
        return x - y
    elif operator == "divide":
        return x / y
    elif operator == "multiply":
        return x * y
    else:
        return x + y
    
def record_creator(name: str, surname:str, age: int):
    return name + surname + str(age)
