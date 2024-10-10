def recursive_gcd(a, b):
    #  Знаходимо рекурсивно найбільший спільний дільник двох натуральних чисел.
    if a == 0 or b == 0:
        return [a, b]  # Повертаємо a, b
    elif a >= 2 * b:
        a = a - 2 * b
        return recursive_gcd(a, b)  # Викликаємо рекурсивну функцію з новими значеннями a, b
    elif b >= 2 * a:
        b = b - 2 * a
        return recursive_gcd(a, b)  # Викликаємо рекурсивну функцію з новими значеннями a, b
    else:
        return [a, b]  # Повертаємо a, b


a = 50
b = 125
print(recursive_gcd(a, b))
