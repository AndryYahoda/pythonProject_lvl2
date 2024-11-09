import json
from calculator_module import add, subtract, multiply, divide, power, sqrt, factorial

results = {}

operations = [
    (add, 4, 17),
    (subtract, 10, 5),
    (multiply, 3, 7),
    (divide, 14, 2),
    (power, 2, 3),
    (sqrt, 16, None),
    (divide, 5, 0),
    (factorial, 5, None)
]

for operation in operations:
    func, a, b = operation
    if b is not None:
        result = func(a, b)
        results[f"{a}{func.__name__}{b}"] = result
    else:
        result = func(a)
        results[f"{func.__name__}{a}"] = result

with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

with open("results.json", "r", encoding="utf-8") as file:
    data = json.load(file)

sum_first_five = sum(list(data.values())[:5])
print("Сума перших 5 результатів:", sum_first_five)

