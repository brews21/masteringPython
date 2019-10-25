import json, logging, boto3, os, sys, requests, psycopg2



# postgress cmds to create the table
# DROP TABLE IF EXISTS common.mikeyb cascade;
# CREATE TABLE common.mikeyb (first_name varchar (50), last_name varchar (50), age integer);
# INSERT INTO common.mikeyb (first_name, last_name, age) VALUES ('dave', 'jones', 100);
# SELECT * FROM common.mikeyb;
# ALTER TABLE common.mikeyb DROP COLUMN id;

hostname = 'localhost'

conn = psycopg2.connect(dbname='test', user='postgres', password='password', host=hostname)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
# cur.execute("DROP TABLE IF EXISTS common.mikeyb cascade; CREATE TABLE common.mikeyb (id serial PRIMARY KEY, first_name varchar[50], last_name varchar[50], age integer);")

# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("dave", "jones", 100))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("fred", "jones", 33))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("harry", "jones", 44))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("dave", "sam", 23))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("harry", "sam", 634))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("fred", "sam", 432))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("train", "nine", 10530))
# cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",("train", "ten", 325))

# cur.execute("SELECT * FROM common.mikeyb;")

# Make the changes to the database persistent
# conn.commit()

cur.execute("SELECT * FROM common.mikeyb WHERE first_name='mike';")
data = cur.fetchall()

print(data)

for x in data:
    lst = list(x)
    lst[0] = 'mikeyb'
    lst[-1] = '999'
    x = tuple(lst)
    print(x)
    cur.execute(f'INSERT INTO common.mikeyb VALUES {x}')
    conn.commit()

# Close communication with the database
cur.close()
conn.close()
