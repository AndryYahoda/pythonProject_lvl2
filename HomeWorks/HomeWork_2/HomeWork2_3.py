# Third task
list_1 = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

different_element = list(set(list_1) ^ set(list_2))
print(different_element)
