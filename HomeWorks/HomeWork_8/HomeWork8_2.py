from collections import Counter


def find_most_common_shortest_word(file: str) -> str:
    """
    Знаходить найкоротше слово, яке зустрічається найчастіше у текстовому файлі.
    :param file: Шлях до текстового файлу, з якого потрібно прочитати текст.
    :return: Найкоротше слово, яке зустрічається найбільше разів.
    """
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    normalized_words = [word.lower() for word in words]
    word_count = Counter(normalized_words)
    max_count = max(word_count.values())
    most_common_words = [word for word, count in word_count.items() if count == max_count]
    shortest_word = min(most_common_words, key=len)
    return shortest_word


def replace_word_in_text(file, target_word: str) -> str:
    """
    Замінює всі входження цільового слова у текстовому файлі на його версію з великими літерами.
    :param file: Шлях до текстового файлу, в якому потрібно виконати заміну.
    :param target_word: Слово, яке потрібно замінити на його версію з великими літерами.
    :return: Модифікований текст, в якому всі входження цільового слова замінені на його версію з великими літерами.
    """

    with open(file, 'r', encoding='utf-8') as file:
        text = file.read()

    upper_target_word = target_word.upper()
    modified_text = text.replace(target_word, upper_target_word)
    return modified_text


file_path = 'input_1.txt'
most_common_shortest_word = find_most_common_shortest_word(file_path)
result_text = replace_word_in_text(file_path, most_common_shortest_word)
print(most_common_shortest_word)
print('----------------------------------------------------------------------')
print(result_text)
