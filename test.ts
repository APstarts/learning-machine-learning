let name: string = "";
let age: number = 0;
function calculator(x:number, y:number, operator:string):number {
    if (operator === "substraction") {
        return x - y
    } else if (operator === "multiply") {
        return x * y
    } else {
        return x + y
    }
}

let result = calculator(4,5,"substraction")
console.log(`Result of substraction: ${result}`)