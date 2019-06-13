import csv
from datetime import date


def writeJobsToFile(jobs):
    today = date.today()
    dstr = today.strftime("%d-%m-%Y")
    with open('jobs-' + dstr + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Job Title', 'Company', 'Time', 'Location', 'Link'])
        for job in jobs:
            writer.writerow(
                [job.title, job.company, job.date, job.location, job.link])
