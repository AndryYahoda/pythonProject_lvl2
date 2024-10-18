def count_vowels_consonants(filename: str) -> dict:
    """
    Підраховує кількість голосних та приголосних у файлі.
    :param filename: Ім'я або шлях до файлу, який потрібно обробити.
    :return: Словник з кількістю голосних та приголосних.
    """
    vowels = "AEIOUaeiouАЕЄИІЇОУЮЯаеєиіїоуюя"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyzБВГҐДЖЗЙКЛМНОПРСТФХЦЧШЩбвгґджзйклмнопрстфхцчшщ"

    result = {'vowels': 0, 'consonants': 0}

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    for char in text:
        if char in vowels:
            result['vowels'] += 1
        elif char in consonants:
            result['consonants'] += 1

    return result


result = count_vowels_consonants('input_8.txt')
print(result)

