import random

random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1, 100) for _ in range(10)]


def lists_compare(list1, list2):
    even_count_list1 = sum(1 for num in list1 if num % 2 == 0)

    odd_count_list2 = sum(1 for num in list2 if num % 2 != 0)

    return even_count_list1 > odd_count_list2


print("Перший список:", random_list1)
print("Другий список:", random_list2)

result = lists_compare(random_list1, random_list2)
print("Результат:", result)
