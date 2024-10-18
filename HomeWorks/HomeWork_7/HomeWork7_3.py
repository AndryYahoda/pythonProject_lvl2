from collections import Counter


def compare_and_find_popular(filename: str) -> None:
    """
    Порівнює кількість голосних і приголосних у файлі та знаходить найпопулярніші символи.
    :param filename: Ім'я або шлях до файлу, який потрібно обробити.
    :return: Результат функції виводиться на екран і записується у файл.
    """

    vowels = "AEIOUaeiouАЕЄИІЇОУЮЯаеєиіїоуюя"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyzБВГҐДЖЗЙКЛМНОПРСТФХЦЧШЩбвгґджзйклмнопрстфхцчшщ"
    vowels_list = []
    consonants_list = []

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

        for char in text:
            if char in vowels:
                vowels_list.append(char)
            elif char in consonants:
                consonants_list.append(char)

    if len(consonants_list) > len(vowels_list):
        most_common_consonant = Counter(consonants_list).most_common(1)[0][0]
        output_text = f"Найпопулярніша приголосна: {most_common_consonant}\n"
    elif len(vowels_list) > len(consonants_list):
        most_common_vowels = Counter(vowels_list).most_common(3)
        output_text = "Три найпопулярніші голосні:\n" + '\n'.join(
            [f"{vowel} з частотою {frequency}" for vowel, frequency in most_common_vowels])
    else:
        output_text = "Голосних і приголосних однакова кількість!\n"

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(output_text)

    print(output_text)


compare_and_find_popular('input_8.txt')
