def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0 or isinstance(x, bool)]  # Створюємо список , який містить усі елементи зі
    # списку lst, що не дорівнюють нулю або є буловими значеннями
    zeros = [x for x in lst if x == 0 and not isinstance(x, bool)]  # Створюємо список, який містить лише нулі зі
    # списку lst за умови, що ці елементи не є буловими значеннями
    return non_zeros + zeros  # Повертаємо новий список, що складається з елементів списку non_zeros, за яким слідує
    # список нулів zeros.


list = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]
result = move_zeros(list)
print(result)
