def count_brackets(string: str) -> tuple:
    """
    Рахує кількість відкритих та закритих дужок різних типів у рядку та перевіряє, чи всі дужки збалансовані.
    :param string: Рядок, в якому потрібно порахувати дужки та перевірити їхню збалансованість.
    :return: Словник з кількістю кожного типу дужок.
    """
    result = {
        'round_open': 0, 'round_close': 0,
        'square_open': 0, 'square_close': 0,
        'curly_open': 0, 'curly_close': 0
    }
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char == '(':
            result['round_open'] += 1
            stack.append(char)
        elif char == ')':
            result['round_close'] += 1
            if not stack or stack.pop() != pairs[char]:
                return result, False
        elif char == '[':
            result['square_open'] += 1
            stack.append(char)
        elif char == ']':
            result['square_close'] += 1
            if not stack or stack.pop() != pairs[char]:
                return result, False
        elif char == '{':
            result['curly_open'] += 1
            stack.append(char)
        elif char == '}':
            result['curly_close'] += 1
            if not stack or stack.pop() != pairs[char]:
                return result, False

    return result, not stack


input_data = "hello(asdasd)sdgsdfsd[sdgsd]asdasdwa{qweasdasd}"
result, balanced = count_brackets(input_data)
print(result)
print("Balanced:", balanced)
