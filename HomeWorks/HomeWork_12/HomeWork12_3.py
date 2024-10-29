filter_short_words = lambda words: list(filter(lambda word: len(word) <= sum(map(len, words)) / len(words), words))
words = ["apple", "banana", "kiwi", "pear", "plum", "watermelon", "melon"]
print(filter_short_words(words))
