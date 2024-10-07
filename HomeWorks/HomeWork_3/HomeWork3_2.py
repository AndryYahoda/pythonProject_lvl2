def three_largest_elements(lst):
    unique_lst = list(set(lst))
    sorted_lst = sorted(unique_lst, reverse=True)[:3]
    return sorted_lst


lst = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
print("Список:", lst)

max_1, max_2, max_3 = three_largest_elements(lst)
print('max_1 =', max_1)
print('max_2 =', max_2)
print('max_3 =', max_3)


