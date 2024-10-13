import random


def count_even_odd(list1, list2: int) -> list:
    """
    Функція для підрахунку кількості парних чисел у першому списку та непарних чисел у другому списку.
    :param list1: Перший список цілих чисел.
    :param list2: Другий список цілих чисел.
    :return: Список з двох елементів:
            1. Перший елемент: кількість парних чисел у list1.
            2. Другий елемент: кількість непарних чисел у list2.
    """
    even_list = [num for num in list1 if num % 2 == 0]
    odd_list = [num for num in list2 if num % 2 != 0]
    result = [len(even_list), len(odd_list)]
    return result


random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1, 100) for _ in range(10)]

print("Перший список:", random_list1)
print("Другий список:", random_list2)

result = count_even_odd(random_list1, random_list2)

if result[0] == result[1]:
    print("Результат: Equal")
else:
    print("Результат: ", result[0] > result[1])


