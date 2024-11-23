import sqlite3

db_name = input("Введіть ім'я для бази даних: ") + ".db"

with open("part_data_1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

columns = lines[0].strip().split("\t")
data = [line.strip().split("\t") for line in lines[1:]]
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

try:
    cursor.execute(f"""
        CREATE TABLE table_no_constraints (
            {", ".join([f"{col} TEXT" for col in columns])}
        );
    """)

    cursor.execute(f"""
        CREATE TABLE table_unique_col2 (
            {columns[0]} TEXT,
            {columns[1]} TEXT UNIQUE,
            {", ".join([f"{col} TEXT" for col in columns[2:]])}
        );
    """)

    cursor.execute(f"""
        CREATE TABLE table_not_null_col3 (
            {", ".join([f"{columns[i]} TEXT{' NOT NULL' if i == 2 else ''}" for i in range(len(columns))])}
        );
    """)

    print("Таблиці успішно створені!")
except sqlite3.Error as e:
    print(f"Помилка: {e}")

conn.close()
