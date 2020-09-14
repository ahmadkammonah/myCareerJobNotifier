# Dalhousie University myCareer Job Notifier

myCareer is a Career website by Dalhousie University in Canada. This Python program uses your personal University Creditenials to access the site and scrap it for new jobs. It will then send an email to the desired list whenever a new Job is posted. 

## Usage

For a fully automated experience, it is perferred to use a free Linux server on Amazon Web Services (AWS) and create a cron job that runs the main.py Python Script at the desired frequency. 

Crontab Example:  */30 * * * * "path to main.py" >> "path to log file" 2>&1

Having a log file is optional but recommended.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
