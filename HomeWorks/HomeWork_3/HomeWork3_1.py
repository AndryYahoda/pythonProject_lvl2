import random

random_list = [random.randint(1, 100) for _ in range(10)]


def largest_even_element(lst):
    even_numbers = [number for number in lst if number % 2 == 0]  # Перевіряємо числа на ділення на 2

    if even_numbers:  # Якщо число ділится на 2 - повертаємо найбільше
        return max(even_numbers)  # Повертаємо число
    else:
        print('Парних чисел нема')  # Робимо прінт, якщо парних чисел нема


print("Список:", random_list)
result = largest_even_element(random_list)
print("Найбільший парний елемент:", result)
