def count_words_by_case(file: str) -> dict:
    """
    Обчислює кількість слів, які починаються з великої та маленької літери у файлі.
    :param file: Шлях до текстового файлу, який потрібно прочитати.
    :return: Словник з двома ключами:
    """

    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().split()

    result = {
        'capitalized words': sum(1 for word in text if word[0].isupper()),
        'lowercase words': sum(1 for word in text if word[0].islower())
    }

    return result


result = count_words_by_case('input_1.txt')
print(result)

