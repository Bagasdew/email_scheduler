from flask import Flask, request, jsonify
import datetime
import json
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from use_case.email import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/save_emails', methods=['POST'])
def save_emails():
    payload = json.loads(request.data)
    insert_schedule(payload)
    return "success"

def get_scheduled_email(conn):
    current_time = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute('Select * from email_schedule where status = 0 and scheduled_at <= ?',current_time)
    rows = cur.fetchall()
    for x in rows :
        print(x)

    return None
 

scheduler = BackgroundScheduler()
scheduler.add_job(func=send_email, trigger="interval", seconds=10)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run()