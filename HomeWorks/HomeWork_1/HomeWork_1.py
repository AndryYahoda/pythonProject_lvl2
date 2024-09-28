def replace(new_text):
    new_text = new_text.replace(" ", "").lower()
    return new_text


input_text = input("Введіть рядок: ")
text_without_spaces = replace(input_text)
print("Це текст без пробілів:", text_without_spaces)

if text_without_spaces == text_without_spaces[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")
