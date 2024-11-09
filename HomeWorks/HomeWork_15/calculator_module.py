import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка! Ділення на нуль."


def power(a, b):
    return a ** b


def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Помилка! Негативне число."


def factorial(a):
    if a >= 0 and int(a) == a:
        return math.factorial(int(a))
    else:
        return "Помилка! Факторіал визначений тільки для невід'ємних цілих чисел."
