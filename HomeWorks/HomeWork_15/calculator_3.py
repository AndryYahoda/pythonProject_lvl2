import json
from calculator_module import add, subtract, multiply, divide, power, sqrt, factorial


class Calculator:
    """
    A simple calculator class that keeps a history of calculations.
    """
    def __init__(self):
        """
        Initializes a new Calculator instance with an empty history dictionary
        to store calculation records.
        """
        self.history = {}

    def perform_operation(self, operation, a, b=None):
        """
        Performs a specified operation and saves it to the history.
        :param operation: The operation to perform (e.g., "add", "sqrt").
        :param a: The first number.
        :param b: The second number for two-operand operations (optional).
        :return: The result of the operation.
        """
        if operation == "add":
            result = add(a, b)
            self.history[f"{a}+{b}"] = result
        elif operation == "subtract":
            result = subtract(a, b)
            self.history[f"{a}-{b}"] = result
        elif operation == "multiply":
            result = multiply(a, b)
            self.history[f"{a}*{b}"] = result
        elif operation == "divide":
            result = divide(a, b)
            self.history[f"{a}/{b}"] = result
        elif operation == "power":
            result = power(a, b)
            self.history[f"{a}^{b}"] = result
        elif operation == "sqrt":
            result = sqrt(a)
            self.history[f"sqrt({a})"] = result
        elif operation == "factorial":
            result = factorial(a)
            self.history[f"{a}!"] = result
        else:
            raise ValueError("Невірна операція")

        return result


class CalculatorLogger:
    """
    A class for logging calculator history to a JSON file.
    """

    def __init__(self, filename="results.json"):
        """
        Initializes the CalculatorLogger with a specified filename.
        :param filename: The name of the file where history will be saved.
        """
        self.filename = filename

    def save_history(self, history):
        """
        Saves the calculator history to a JSON file.
        :param history: The dictionary of history records to be saved.
        """
        with open(self.filename, "w") as file:
            json.dump(history, file)

    def load_history(self):
        """
        Loads the calculator history from a JSON file.
        :return: The dictionary of loaded history records.
        """
        with open(self.filename, "r") as file:
            return json.load(file)


calculator = Calculator()
logger = CalculatorLogger()

calculator.perform_operation("add", 4, 17)
calculator.perform_operation("subtract", 10, 5)
calculator.perform_operation("multiply", 3, 7)
calculator.perform_operation("divide", 14, 2)
calculator.perform_operation("power", 2, 3)
calculator.perform_operation("sqrt", 16, None)
calculator.perform_operation("factorial", 5)

logger.save_history(calculator.history)
loaded_history = logger.load_history()

results = list(loaded_history.values())[:5]
print("Сума перших 5 результатів:", sum(results))
