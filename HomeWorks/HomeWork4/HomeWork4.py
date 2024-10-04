# import random

# input_list = [random.choice([0, random.randint(0, 5)]) for _ in range(5)]


def move_zeros_to_end(lst):
    non_zeros = [x for x in lst if x != 0]

    zero_count = lst.count(0)

    return non_zeros + [0] * zero_count


# Для рандому
# print("Список:", input_list)
# result = move_zeros_to_end(input_list)
# print("Список після переміщення нулів:", result)

# Ваш приклад
# input_list = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]
# result = move_zeros_to_end(input_list)
# print("Список після переміщення нулів:", result)
