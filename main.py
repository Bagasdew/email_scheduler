from flask import Flask, request, jsonify
import datetime
import json
import time
import atexit
from http import client

from apscheduler.schedulers.background import BackgroundScheduler

from use_case.email import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/save_emails', methods=['POST'])
def save_emails():
    payload = json.loads(request.data)
    try:
        insert_schedule(payload)
    except Exception as e:
        return 'invalid payload : '+str(e),400
    return '',201


scheduler = BackgroundScheduler()
scheduler.add_job(func=send_email, trigger="interval", seconds=10)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run()