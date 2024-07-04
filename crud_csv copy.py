import mysql.connector

# Membuat koneksi ke server MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()

# Membuat database baru
cursor.execute("CREATE DATABASE IF NOT EXISTS Wildan")
db.commit()

# Memilih database yang baru dibuat
cursor.execute("USE Wildan")

# Membuat tabel pertama
cursor.execute('''
CREATE TABLE IF NOT EXISTS table1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
''')

# Membuat tabel kedua
cursor.execute('''
CREATE TABLE IF NOT EXISTS table2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    price VARCHAR(255)
)
''')

# Menyisipkan data ke tabel pertama
cursor.executemany('''
INSERT INTO table1 (name, age) VALUES (%s, %s)
''', [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35),
    ('Daisy', 28)
])

# Menyisipkan data ke tabel kedua
cursor.executemany('''
INSERT INTO table2 (product_name, price) VALUES (%s, %s)
''', [
    ('Sepatu', 'Rp. 20.000'),
    ('Baju', 'Rp. 50.000'),
    ('Topi', 'Rp. 10.000'),
    ('Celana', 'Rp. 30.000')
])

# Menyimpan (commit) perubahan
db.commit()

# Menampilkan data dari tabel pertama
cursor.execute("SELECT * FROM table1")
rows1 = cursor.fetchall()
print("Data dari table1:")
for row in rows1:
    print(row)

# Menampilkan data dari tabel kedua
cursor.execute("SELECT * FROM table2")
rows2 = cursor.fetchall()
print("Data dari table2:")
for row in rows2:
    print(row)

# Menutup koneksi
cursor.close()
db.close()