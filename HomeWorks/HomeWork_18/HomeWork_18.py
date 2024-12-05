import sqlite3

db_name = input("Введіть ім'я для бази даних: ") + ".db"

with open("part_data_1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

columns = lines[0].strip().split("\t")  #
data = [line.strip().split("\t") for line in lines[1:]]


def determine_data_type(value):
    try:
        int(value)
        return "INTEGER"
    except ValueError:
        try:
            float(value)
            return "REAL"
        except ValueError:
            return "TEXT"


column_types = [determine_data_type(data[0][i]) for i in range(len(columns))]

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

try:
    cursor.execute(f"""
        CREATE TABLE table_no_constraints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {", ".join([f"{columns[i]} {column_types[i]}" for i in range(len(columns))])}
        );
    """)

    cursor.execute(f"""
        CREATE TABLE table_unique_col2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns[0]} {column_types[0]},
            {columns[1]} {column_types[1]} UNIQUE,
            {", ".join([f"{columns[i]} {column_types[i]}" for i in range(2, len(columns))])}
        );
    """)

    cursor.execute(f"""
        CREATE TABLE table_not_null_col3 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {", ".join([f"{columns[i]} {column_types[i]}{' NOT NULL' if i == 2 else ''}" for i in range(len(columns))])}
        );
    """)

    print("Таблиці успішно створені!")
except sqlite3.Error as e:
    print(f"Помилка: {e}")

conn.close()
