def three_largest_elements(lst: list):
    """
    Функція для знаходження трьох найбільших унікальних елементів у списку.
    :param lst: Список чисел.
    :return: Список з трьох найбільших унікальних елементів, відсортованих за спаданням.
    Якщо елементів менше трьох, повертаються всі наявні унікальні елементи.
    """
    unique_lst = list(set(lst))
    sorted_lst = sorted(unique_lst, reverse=True)[:3]
    return sorted_lst


lst = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
print("Список:", lst)

max_1, max_2, max_3 = three_largest_elements(lst)
print('max_1 =', max_1)
print('max_2 =', max_2)
print('max_3 =', max_3)
