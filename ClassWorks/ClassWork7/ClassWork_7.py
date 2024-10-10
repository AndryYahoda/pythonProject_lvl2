# Task 1

# dict = {0: 10, 1: 20}
#
# new_key = 2
# new_value = 30
#
# dict[new_key] = new_value
#
# print(dict)

# Task 2

# def merge_dicts(dic1, dic2, dic3):
#     """
#
#     :param dic1: перший словник
#     :param dic2: другий словник
#     :param dic3: третій словник
#     :return: Об'єднаний словник
#     """
#     merged_dict = {}
#
#     merged_dict.update(dic1)
#     merged_dict.update(dic2)
#     merged_dict.update(dic3)
#
#     return merged_dict
#
#
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# result = merge_dicts(dic1, dic2, dic3)
# print(result)

# Task 3

# def check_key_in_dict(d, key):
#     """
#     Функція перевіряє, чи є зазначений ключ у словнику.
#     :param d: словник, в якому здійснюється перевірка
#     :param key: ключ, який необхідно перевірити
#     :return: True, якщо ключ присутній у словнику, і False, якщо ні.
#     """
#     return key in d
#
#
# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# key_to_check = 5
# is_key_present = check_key_in_dict(dict, key_to_check)
#
# print(f"Ключ {key_to_check} {'присутній' if is_key_present else 'не присутній'} у словнику.")

# Task 4

# def print_square_dict():
#     """
#     Функція створює і виводить словник, де ключі — числа від 1 до 15,
#     а значення — квадрати цих чисел.
#     :return:
#     """
#     square_dict = {}
#
#     for num in range(1, 16):
#         square_dict[num] = num ** 2
#
#     print(square_dict)
#
#
# print_square_dict()

# Task 5

# def sum_dict_values(d):
#     """
#     Функція обчислює суму всіх значень у словнику.
#     :param d: словник, значення якого необхідно просумувати
#     :return: Сума значень словника
#     """
#     return sum(d.values())
#
#
# dict_1 = {
#     'rtx 4090 Palit GR': 70000,
#     'GeForce 1650 Super GIGABYTE': 7000.50,
#     'rtx 3060Ti Asus': 16700,
#     'Radeon 7900XTX Saphire': 50000,
#     'Rtx 3050 PNY': 8000,
#     'rtx 4080 Palit Gaming Pro': 56000,
#     'Radeon 6600 MSI': 13000,
#     'Radeon 6650 XFX': 14200
# }
#
# total_sum = sum_dict_values(dict_1)
#
# print(f"Сума всіх значень у словнику: {total_sum}")

# Task 6

# def remove_dict_key(d, key):
#     """
#     Функція видаляє елемент зі словника за заданим ключем.
#     :param d: словник, з якого необхідно видалити елемент
#     :param key: ключ, який необхідно видалити
#     :return: Оновлений словник без видаленого ключа
#     """
#     if key in d:
#         del d[key]
#     else:
#         print(f"Ключ '{key}' не знайдений у словнику.")
#
#     return d
#
#
# dict_1 = {
#     'rtx 4090 Palit GR': 70000,
#     'GeForce 1650 Super GIGABYTE': 7000.50,
#     'rtx 3060Ti Asus': 16700,
#     'Radeon 7900XTX Saphire': 50000,
#     'Rtx 3050 PNY': 8000,
#     'rtx 4080 Palit Gaming Pro': 56000,
#     'Radeon 6600 MSI': 13000,
#     'Radeon 6650 XFX': 14200
# }
#
# key_to_remove = 'Radeon 6600 MSI'
#
# updated_dict = remove_dict_key(dict_1, key_to_remove)
#
# print("Оновлений словник:", updated_dict)

# Task 8

# def create_dict_from_lists(keys, values):
#     """
#     Функція створює словник на основі двох списків: ключів та значень.
#     :param keys: список з ключами
#     :param values: список з відповідними значеннями
#     :return: Словник, створений на основі ключів та значень
#     """
#     return dict(zip(keys, values))
#
#
# keys = ['red', 'green', 'blue']
# values = ['#FF0000', '#008000', '#0000FF']
#
# color_dict = create_dict_from_lists(keys, values)
#
# print(color_dict)

# Task 10

# from itertools import product
#
#
# def create_combinations(d):
#     """
#     Функція створює і відображає всі комбінації літер, вибираючи кожну літеру
#     з різних ключів у словнику.
#     :param d: словник, де значення є списками літер
#     :return: Список комбінацій літер
#     """
#     letter_lists = d.values()
#
#     combinations = [''.join(comb) for comb in product(*letter_lists)]
#
#     print(' '.join(combinations))
#
#     return combinations
#
#
# data = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f']}
#
# create_combinations(data)


