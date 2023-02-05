from domain.email import *



def insert_schedule(payload):
    insert_email_schedule(payload)
    return None

def send_email():
    print('start email job')
    recipients = get_email_recipients()
    job = get_email_schedule()
    for x in job:
        # send email
        update_email_schedule(x['id'])
        print("update email job")
    return None    