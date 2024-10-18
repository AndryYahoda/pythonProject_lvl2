def count_characters(filename: str) -> dict:
    """
    Підраховує кількість літер, цифр, пробілів та інших символів у файлі.
    :param filename: Ім'я або шлях до файлу, який потрібно обробити.
    :return: Словник, що містить підрахунки літер, цифр, пробілів та інших символів.
    """
    counts = {
        'letters': 0,
        'digits': 0,
        'whitespaces': 0,
        'other': 0
    }

    with open(filename, 'r') as file:
        text = file.read()

        for char in text:
            if char.isalpha():
                counts['letters'] += 1
            elif char.isdigit():
                counts['digits'] += 1
            elif char.isspace():
                counts['whitespaces'] += 1
            else:
                counts['other'] += 1

    return counts


filename = 'input_8.txt'
result = count_characters(filename)
print(result)
