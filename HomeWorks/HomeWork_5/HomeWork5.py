def recursive_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= 2 * b:
        return recursive_gcd(a - 2 * b, b)
    elif b >= 2 * a:
        return recursive_gcd(a, b - 2 * a)
    else:
        return recursive_gcd(a - b, b) if a > b else recursive_gcd(a, b - a)


a = 56
b = 16
print("Найбільший спільний дільник:", recursive_gcd(a, b))