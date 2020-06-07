# This module sends an email notification for new jobs
# Creator: Ahmad Kammonah - Date: May 13th, 2020 - Copyright: Kammonah Industries 2020

import smtplib      # Package used to send emails using the "Simple Mail Transfer Protocol"
import datetime     # Package used to get time and date. Used for logging purposes


# Function name sendmail accepts a list of new jobs as a parameter
def sendmail(__new_jobs):
    sender = "example@outlook.com"                      # TODO: Email you're sending from
    password = "********"                               # TODO: password of the email
    receiver = ["example@dal.ca"]                       # TODO: Add mailing list here

# writes the subject and checks if more than one job add an 's' for plural
    subject = str(len(__new_jobs)) + " New Job" + ("" if len(__new_jobs) == 1 else "s") + " Posted on myCareer"

# This loops through all new jobs and writes the body of the email in a nice way.
    body = ""
    for job in __new_jobs:
        body = body + \
               ">ID: {}\n".format(str(job[0])) + \
               ">Job Title: {}\n".format(job[1]) + \
               ">Company: {}\n".format(job[2]) + \
               ">Location: {}\n".format(job[3]) + \
               ">Deadline: {}\n\n".format(job[4])

# Adds final a sentence for fun :D !!
    body = body + str("\n\n\nCopyright: 2020, Ahmad Kammonah")

# Puts the subject and body in one variable named 'message' because this is how smtp accepts it.
    message = 'Subject: {}\n\n{}'.format(subject, body)

# Starts an smpt login request using the email and password provided earlier
    smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtp.starttls()
    smtp.login(sender, password)

# Sends the message and quits
    smtp.sendmail(sender, receiver, message)
    smtp.quit()

# Logs a successful process
    now = "The program sent an Email at " + str(datetime.datetime.now())
    print(now)
