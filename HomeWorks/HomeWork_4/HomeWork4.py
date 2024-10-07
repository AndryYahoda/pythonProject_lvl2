def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0 or isinstance(x, bool)]
    zeros = [x for x in lst if x == 0 and not isinstance(x, bool)]
    return non_zeros + zeros


list = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]
result = move_zeros(list)
print(result)
