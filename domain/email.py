import sqlite3
import datetime

def get_db_connection():
    conn = sqlite3.connect('email_schedule.db')
    conn.row_factory = sqlite3.Row
    return conn   

def get_email_recipients():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT email_address from email_recipient limit 1')
    rows = cur.fetchall()
    email_list = []
    for x in rows:
        email_list.append(x)
    return email_list[0]

def get_email_schedule():
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)
    query = 'Select * from email_schedule where status = 0 and scheduled_at <= "'+current_time+'"'
    print(query)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def insert_email_schedule(payload):
    conn = get_db_connection()
    conn.execute('INSERT INTO email_schedule (id,subject,body,scheduled_at,status) values (?,?,?,?,?)',(payload['id'],payload['subject'],payload['body'],payload['scheduled_at'],0))
    conn.commit()
    conn.close()
    return None

def update_email_schedule(id):
    conn = get_db_connection()
    query = 'UPDATE email_schedule set status = 1 where id = '+str(id)
    conn.execute(query)
    conn.commit()
    conn.close()
    return None
