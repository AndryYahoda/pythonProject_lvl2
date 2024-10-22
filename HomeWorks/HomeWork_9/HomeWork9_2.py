import json


def read_data_from_json(file_name):
    """
    Зчитує дані з JSON файлу.
    :param file_name: Назва файлу, з якого потрібно зчитати дані.
    :return: Дані, зчитані з JSON файлу у вигляді словника.
    """

    with open(file_name, 'r') as file:
        return json.load(file)


def write_data_to_json(file_name, data):
    """
    Записує дані до JSON файлу.
    :param file_name: Назва файлу, до якого потрібно записати дані.
    :param data: Дані, зчитані з JSON файлу у вигляді словника.
    :return: Функція не повертає значення, вона лише записує дані до файлу.
    """

    with open(file_name, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def update_factory_data(factory):
    """
     Оновлює дані про кількість працівників у департаментах компанії.
    :param None: Функція не приймає жодних параметрів.
    :return: Функція не повертає значення, вона лише оновлює дані та виводить їх на екран.
    """

    factory['IT department'] += 5
    factory['Marketing department'] = 12
    del factory['Law department']

    return factory


def employees_counter(factory):
    total_employees = sum(factory.values())
    print("Кількість працівників у різних відділах:")
    for department, count in factory.items():
        print(f"{department}: {count}")

    print(f"\nЗагальна кількість співробітників у компанії: {total_employees}")


factory_data = {
    'IT department': 20,
    'Sales department': 15,
    'Production department': 30,
    'Law department': 5,
    'Construction department': 10
}

changed_factory = update_factory_data(factory_data)
write_data_to_json('factory_data.json', changed_factory)
new_factory = read_data_from_json('factory_data.json')
employees_counter(new_factory)


