# Task 1
# def generate_zero_one_list(n):
#     if n <= 0:
#         return []
#
#     result = [0, 1] * n
#     return result
#
#
# n = 5
# generated_list = generate_zero_one_list(n)
# print(generated_list)

# Task 2

# import random
#
#
# def generate_list():
#     total_elements = 20
#
#     num_ones = random.randint(total_elements // 2 + 1, total_elements)
#     num_zeros = total_elements - num_ones
#
#     result = [1] * num_ones + [0] * num_zeros
#
#     random.shuffle(result)
#
#     return result
#
#
# generated_list = generate_list()
# print(generated_list)

# Task 3

# import random
#
#
# def count_even_odd_random_list(size):
#     random_list = [random.randint(1, 100) for _ in range(size)]
#
#     even_count = 0
#     odd_count = 0
#
#     for num in random_list:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#
#     print(f"Згенерований список: {random_list}")
#
#     if even_count > odd_count:
#         return "Більше чисел, які діляться на 2 без остачі."
#     elif odd_count > even_count:
#         return "Більше чисел, які діляться на 2 з остачею."
#     else:
#         return "Кількість чисел, які діляться на 2 без остачі і з остачею, однакова."
#
#
# size = 10
# result = count_even_odd_random_list(size)
# print(result)

# Task 4

# from collections import Counter
#
#
# def count_letters(text):
#     text = text.lower()
#
#     letter_count = Counter(text)
#
#     result = [f"{char} - {count}" for char, count in letter_count.items() if char.isalpha()]
#
#     return result
#
#
# text = 'Hi! My name is Andrii.'
# result = count_letters(text)
# print(result)

# Task 5

# def encrypt_phone_number(phone_number):
#     encrypted_number = ''
#
#     for char in phone_number:
#         if char.isdigit():
#             encrypted_digit = (int(char) + 9) % 10
#             encrypted_number += str(encrypted_digit)
#         else:
#             encrypted_number += char
#
#     return encrypted_number
#
#
# phone_number = '380959386740'
# encrypted_phone_number = encrypt_phone_number(phone_number)
# print(encrypted_phone_number)

# Task 6


