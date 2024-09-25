# Third task
list_1 = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

different_element = set([a for a in list_1 if a not in list_2] + [a for a in list_2 if a not in list_1])
print(different_element)