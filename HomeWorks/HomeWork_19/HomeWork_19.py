import sqlite3

db_path = "Chinook_Sqlite.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Customer LIMIT 3;")
customers = cursor.fetchall()
print("Перші 3 записи з таблиці Customer:")
for customer in customers:
    print(customer)

cursor.execute("SELECT SUM(Total) AS TotalSum FROM Invoice;")
total_sum = cursor.fetchone()[0]
print("\nЗагальна сума поля Total у таблиці Invoice:", total_sum)

cursor.execute("SELECT * FROM Invoice WHERE BillingCity = 'Paris';")
invoices_paris = cursor.fetchall()
print("\nЗаписи з таблиці Invoice для міста Paris:")
for invoice in invoices_paris:
    print(invoice)

cursor.execute("SELECT MIN(InvoiceDate) AS OldestDate, * FROM Invoice;")
oldest_invoice = cursor.fetchone()
print("\nЗапис із найстарішою датою з таблиці Invoice:", oldest_invoice)

cursor.execute("SELECT MAX(InvoiceDate) AS NewestDate, * FROM Invoice;")
newest_invoice = cursor.fetchone()
print("\nЗапис із найсвіжішою датою з таблиці Invoice:", newest_invoice)

conn.close()

# Також добавив для коміту