import sqlite3

connection = sqlite3.connect('email_schedule.db')


with open('sql/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO email_recipient (id, email_address) VALUES (?, ?)",
            (1, 'bagas.dewangkara@gmail.com')
            )
connection.commit()
connection.close()