import sqlite3
conn = sqlite3.connect('example.db', isolation_level=None) 
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL,birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')

print(sqlite3.sqlite_version)

schema_name = conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
print(schema_name)

table_info = conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()

print(table_info)

#insert_command = conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')
#print(insert_command)

cat_name = 'Zophie_meow'
cat_bday = '2021-01-24'
fur_color = 'black'
cat_weight = 5.6
# conn.execute(f'INSERT INTO cats VALUES ("{cat_name}", "{cat_bday}","{fur_color}", {cat_weight})')

#cats_list = ["cat1","cat2","cat3"]

#for single_cat  in cats_list:
  #  conn.execute(f'INSERT INTO cats VALUES ("{single_cat}", "{cat_bday}","{fur_color}", {cat_weight})')#


cat_records = conn.execute('SELECT * FROM cats').fetchall()
print(cat_records)

print("\n=========printing cat_records individually=========")
for cat in cat_records:
    print (cat)

print("\n=========printing store=========")
store = conn.execute('SELECT rowid, name FROM cats').fetchall()
print(store)

print("\n=========printing store individualy=========")
for cat1 in store:
    print(cat1)

print("\n=========printing Looping over Query Results=========")
for row in conn.execute('SELECT * FROM cats'):
    print('Row data:', row)
    print(row[0], 'is one of my favorite cats.')

conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()

print("\n=========Filtering Retrieved Data=========")

conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
DataRetrive = conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()
print (DataRetrive)

print("\n=========Filtering Retrieved Data Type 2 ROW vier=========")

conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
DataRetrive = conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()
for row1 in DataRetrive:
    print (row1)

print("\n=========Filtering Retrieved Data Type 3=========")    #Asking  about pprint
import pprint
matching_cats = conn.execute ('SELECT * FROM cats WHERE fur = "black" OR birthdate >="2024-01-01"').fetchall()
pprint.pprint(matching_cats)

Data1 = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"').fetchall()
for row2 in Data1:   #ASKING DATA STORE IN ROW 2 HOW?
    print(row2)
print("\n=========Filtering Retrieved Data Type 4=========")
Data2 = conn.execute('SELECT rowid, name FROM cats WHERE name GLOB "*m*"').fetchall()
for row3 in Data2:
    print(row3)