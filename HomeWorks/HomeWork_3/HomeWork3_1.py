import random

random_list = [random.randint(1, 100) for _ in range(10)]


def largest_even_element(lst):
    """
     Функція для знаходження найбільшого парного елемента у списку.
    :param lst: Список цілих чисел.
    :return: Найбільше парне число в списку
    """
    even_numbers = [number for number in lst if number % 2 == 0]

    if even_numbers:
        return max(even_numbers)
    else:
        print('Парних чисел нема')


print("Список:", random_list)
result = largest_even_element(random_list)
print("Найбільший парний елемент:", result)
