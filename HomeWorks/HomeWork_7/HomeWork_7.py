def count_characters(filename):
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
