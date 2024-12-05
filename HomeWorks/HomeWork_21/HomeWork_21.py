class List:
    @staticmethod
    def remove_elements(lst, values_to_remove):
        return [item for item in lst if item not in values_to_remove]


list_1 = [1, 1, 2, 3, 1, 2, 3, 4]
val = [1, 3]
result = List.remove_elements(list_1, val)
print(result)
