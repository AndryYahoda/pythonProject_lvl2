import json
from calculator_module import add, subtract, multiply, divide, power, sqrt, factorial


def perform_operations():
    """
    Performs a series of mathematical operations and saves the results in a JSON file.

    Operations include addition, subtraction, multiplication, division, exponentiation,
    square root calculations, and factorial. This dictionary is then
    saved to 'results.json' by calling the save_results_to_file function.
    """
    operations = [
        ("4+17", add(4, 17)),
        ("15-7", subtract(10, 5)),
        ("6*3", multiply(3, 7)),
        ("8/2", divide(14, 2)),
        ("5**2", power(2, 3)),
        ("sqrt(16)", sqrt(16)),
        ("sqrt(25)", sqrt(25)),
        ("5!", factorial(5))
    ]
    results = {op[0]: op[1] for op in operations}
    save_results_to_file(results)


def save_results_to_file(results):
    """
    Saves the given results dictionary to a file named 'results.json' in JSON format.
    :param results: The dictionary of results to be saved.
    """
    with open("results.json", "w") as file:
        json.dump(results, file)


def load_results_and_calculate_sum():
    """
    Opens the 'results.json' file, reads its contents, and calculates the sum
    of the first five values.
    """
    with open("results.json", "r") as file:
        data = json.load(file)
    first_five_sum = sum(value for i, value in enumerate(data.values()) if i < 5)
    print("Сума перших 5 результатів:", first_five_sum)


perform_operations()

load_results_and_calculate_sum()
