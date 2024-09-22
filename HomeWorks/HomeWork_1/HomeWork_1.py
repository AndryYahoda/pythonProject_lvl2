input_text = input("Введіть рядок: ")


def no_space(text):
    # first option
    new_text = text.replace(" ", "")
    return new_text

    # second option
    # text = text.split()
    # text = ''.join(text)
    # return text


def reversed_input(text):
    text = ''.join(reversed(text))
    return text


text_without_spaces = no_space(input_text)
print("Це текст без пробілів:", text_without_spaces)
reversed_text = reversed_input(text_without_spaces)
print("Це перевернутий текст:", reversed_text)


if text_without_spaces == reversed_text:
    print("Це паліндром")
else:
    print("Це не паліндром")
