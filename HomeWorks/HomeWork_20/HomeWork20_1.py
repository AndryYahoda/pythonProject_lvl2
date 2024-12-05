import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Customer (
    CustomerID INTEGER PRIMARY KEY,
    Company TEXT,
    Fax TEXT,
    Continent TEXT
);
''')

cursor.executemany('''
INSERT INTO Customer (CustomerID, Company, Fax, Continent)
VALUES (?, ?, ?, ?);
''', [
    (1, 'BigTech Inc.', '123-456', 'North America'),
    (2, 'EcoGreen Solutions', None, 'Europe'),
    (3, None, None, 'Asia'),
    (4, 'Future Innovations', '789-012', 'North America'),
    (5, None, None, 'Europe'),
    (6, 'LongNameCompanyWithGreatAmbitions', None, 'Asia'),
    (7, None, '456-789', 'South America'),
    (8, 'FastTrade LLC', '321-654', 'Africa')
])

cursor.execute('''
SELECT *
FROM Customer
WHERE LENGTH(Company) = (
    SELECT MAX(LENGTH(Company))
    FROM Customer
    WHERE Company IS NOT NULL
);
''')
for row in cursor.fetchall():
    print(row)

conn.close()
