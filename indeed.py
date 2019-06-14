# importing libraries
from job import Job
from bs4 import BeautifulSoup
from writer import writeJobsToFile
import requests

# indeed.ca job search software engineer in Vancouver BC
indeedUrl = "https://www.indeed.ca"
url = "https://www.indeed.ca/jobs?q=software+engineer&l=Vancouver%2C+BC"
try:
    page = requests.get(url)
except Exception as e:
    print(e)
soup = BeautifulSoup(page.text, 'html.parser')
jobs = []


def extract_jobs_from_result(soup):
    count = 0
    for div in soup.findAll('div', attrs={"class": ['row', 'result']}):
        job = Job()
        # find title of job
        a = div.find('a', attrs={"data-tn-element": "jobTitle"})
        job.setTitle(a["title"])
        # find link of job
        job.setLink(indeedUrl + a["href"])
        # find date of job
        date = div.find('span', attrs={"class": "date"})
        if(date != None):
            job.setDate(date.string)
        # find company of job
        company = div.find('a', attrs={"data-tn-element": "companyName"})
        if(company != None):
            job.setCompany(company.string)
        # find location of job
        location = div.find('div', attrs={"class": "location"})
        if(location != None):
            job.setLocation(location.string)
        # add job to list
        jobs.append(job)
        count += 1
    return(count)


print(str(extract_jobs_from_result(soup)) + "jobs found.")
writeJobsToFile(jobs)
# increment jobs based on how many findall divs found on this page, total results divide by how many page then we know how many pages
