fruits = ["apple", "banana", "kiwi", "pear", "plum", "watermelon", "melon"]
odd_fruits = list(filter(lambda x: fruits.index(x) % 2 == 0, fruits))
print(odd_fruits)
