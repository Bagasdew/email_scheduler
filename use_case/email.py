from domain.email import *
import uuid



def insert_schedule(payload):
    if validate_payload(payload) == False:
        raise ValueError('payload not valid')
    payload['id'] = str(uuid.uuid4())
    insert_email_schedule(payload)
    return None

def send_email():
    print('start email job')
    recipients = get_email_recipients()
    job = get_email_schedule()
    for x in job:
        # send email - I tried using SMTP but it doesn't work for now
        update_email_schedule(x['id'])
        print("update email job")
    return None 

def validate_payload(payload):
    if payload['scheduled_at'] == '':
        return False
    if payload['subject'] == '':
        return False
    if 'id' in payload:
        return False
    return True