import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on condition
cursor.execute("SELECT * FROM events where date='2023.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT band, date FROM events where date='2023.10.17'")
rows = cursor.fetchall()
print(rows)

# insert new rows
# new_rows=[('Hens', 'Hen City', '2023.10.17'),
#            ('Cats', 'Cat City', '2023.10.17')]
#
# cursor.executemany("INSERT into events VALUES(?,?,?)", new_rows)
# connection.commit()


# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

