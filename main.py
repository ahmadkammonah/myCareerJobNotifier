# This project scraps myCareer Website for new Jobs and notifies my friends through What's App.
# Creator: Ahmad Kammonah - Date: May 13th, 2020 - Copyright: Kammonah Industries 2020

import csv  # Package used to easily convert list into csv format (Excel Sheet format)
import requests  # Package used to request a website
import datetime  # Package used to get time and date. Used for logging purposes
from project import EmailSender
from bs4 import BeautifulSoup  # Package used to easily handle html (language used to write websites)

# The following TO DO list are required by the website for authentication purposes.
# However, the header might not be needed, but you can experiment.

# TODO: ADD Headers which can be found in network tab in inspect element
headers = {
    'User-Agent': '*******'
}

# TODO: ADD Login Data here. Can be found in Network tab in inspect element
login_data = {
    'action': '*****',
    'ldapId': '*******',
    'password': '*******',
    'Login': 'Login'
}

# TODO: ADD POST request keys which can be found in network tab in inspect element
jobs_page_data = {
    'action': '*******',
    'performNewSearch': 'true',
    'cpFilterType': 'none',
    'rand': '93693',
}

# TODO: Add login urls and other required pages' urls here
login_url = "https://mycareer.dal.ca/login/student.htm"
jobs_url = "https://mycareer.dal.ca/myAccount/ecs/jobs.htm"

# Initializing some required variables
all_jobs = []  # This is All Jobs extracted from website
job_title = []  # List of job titles

# Opens a request session and goes to requested page (JOB POSTING PAGE)
with requests.Session() as s:
    s.post(login_url, data=login_data, headers=headers)  # reuests to go to myCareer website
    r = s.post(jobs_url, data=jobs_page_data, headers=headers)  # requests the postings page
    soup = BeautifulSoup(r.content, 'lxml')  # passes the content of postings page to Beautiful Soup Package

    # Find table using ID attribute
    table = soup.find('table', attrs={'id': 'postingsTable'})  # Uses beautiful soup to find the postings table
    table_rows = table.find_all('tr')  # Finds all rows in that table (tr means row in html)

    # Finds each row in table and strips useful data, Job titles have to found separately using Title name
    for tr in table_rows:
        td = tr.find_all('td')  # for each row (tr) find column (td)
        row = [i.text for i in td]  # for each column find the cell and get its text value
        row = [i.strip() for i in row]  # Strip function just removes any space around the text
        all_jobs.append(row)  # add the row (which represents a job) to all_jobs list

        for td in tr.find_all('td'):  # This loop does the same thing but gets only job titles because-
            for span in td.find_all('span'):  # -for some reason they didn't look good in all_jobs list
                job_title.append(span.get('title'))

# Cleans up
job_title = list(filter(None, job_title))  # removes none values (empty cells)
job_title = list(filter("New Job".__ne__, job_title))  # removes the word "New Job" from some of the cells
all_jobs = all_jobs[1:]  # removes the first row since it is the table header not an actual job
x = 0
for i in all_jobs:  # this loop just cleans up and removes fields i think are useless
    i = i[2:9]
    i.pop(4)
    i.pop(3)
    i[1] = job_title[x]
    all_jobs[x] = i
    x += 1

# Opens file reader to read existing/old Jobs in Jobs.csv file
with open("jobs.csv", "r") as fileReader:
    rd = csv.reader(fileReader)
    oldJobs = list(rd)

# Checks if there are any new jobs not in the file and Sorts by ID
newJobs = [x for x in all_jobs if x not in oldJobs]
newJobs = sorted(newJobs, key=lambda i: i[0])

# Writes new Jobs to the same jobs.csv file
with open("jobs.csv", "a") as fileWriter:
    wr = csv.writer(fileWriter)
    wr.writerows(newJobs)

# Sends an email notification if newJobs > 0
if len(newJobs) > 0:
    EmailSender.sendmail(newJobs)

# Logs a successful process
now = "The program run successfully at " + str(datetime.datetime.now())
print(now)
