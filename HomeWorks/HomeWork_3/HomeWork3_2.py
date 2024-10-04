import random

random_list = [random.randint(1, 100) for _ in range(10)]


def three_largest_elements(lst):
    print('Три максимальних числа зі списку: ', sorted(lst, reverse=True)[:3])


print("Список:", random_list)
three_largest_elements(random_list)
