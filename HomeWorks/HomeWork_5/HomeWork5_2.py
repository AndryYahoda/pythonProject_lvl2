def recursive_gcd(a, b):
    """
    Функція для рекурсивного знаходження спільного дільника двох чисел
    :param a: Перше ціле число.
    :param b: Друге ціле число.
    :return: Список з двох елементів [a, b], де одне з чисел є залишком.
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return recursive_gcd(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return recursive_gcd(a, b)
    else:
        return [a, b]


a = 50
b = 125
print(recursive_gcd(a, b))
