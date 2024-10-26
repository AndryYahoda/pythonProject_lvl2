def count_brackets(string: str) -> dict:
    """
    Рахує кількість відкритих та закритих дужок різних типів у рядку.
    :param string: Рядок, в якому потрібно порахувати дужки.
    :return: Словник з кількістю кожного типу дужок.
    """
    result = {
        'round_open': 0, 'round_close': 0,
        'square_open': 0, 'square_close': 0,
        'curly_open': 0, 'curly_close': 0
    }

    for char in string:
        if char == '(':
            result['round_open'] += 1
        elif char == ')':
            result['round_close'] += 1
        elif char == '[':
            result['square_open'] += 1
        elif char == ']':
            result['square_close'] += 1
        elif char == '{':
            result['curly_open'] += 1
        elif char == '}':
            result['curly_close'] += 1

    return result


input_data = "[[](}{([)[[](}{([)[[](}{([)"
result = count_brackets(input_data)
print(result)
