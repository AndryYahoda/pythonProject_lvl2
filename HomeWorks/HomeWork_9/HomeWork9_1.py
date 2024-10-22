factory = {
    'IT department': 20,
    'Sales department': 15,
    'Production department': 30,
    'Law department': 5,
    'Construction department': 10
}

factory['IT department'] += 5
factory['Marketing department'] = 12
del factory['Law department']
total_employees = sum(factory.values())

print("Кількість працівників у різних відділах:")
for department, count in factory.items():
    print(f"{department}: {count}")

print(f"\nЗагальна кількість співробітників у компанії: {total_employees}")