def no_space(text):
    # first option
    new_text = text.replace(" ", "")
    return new_text

    # second option
    # text = text.split()
    # text = ''.join(text)
    # return text


input_text = input("Введіть рядок: ")
text_without_spaces = no_space(input_text)
print("Це текст без пробілів:", text_without_spaces)

reversed_text = ''.join(reversed(text_without_spaces))
print("Це перевернутий текст:", reversed_text)

if text_without_spaces == reversed_text:
    print("Це паліндром")
else:
    print("Це не паліндром")
