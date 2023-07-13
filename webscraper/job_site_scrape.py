from bs4 import BeautifulSoup
import requests
import time
#An input to allow users to search for key search terms in the job name
print("Add a job filter of specific words to find:")
spec = input(">")
#I added .upper to the input and changed the h2 header to .upper to ensure that the input and title match exactly
specs = spec.upper()
print("Filtering ", specs)

def find_jobs():
    html_text = requests.get("https://www.reed.co.uk/jobs/junior-devops-jobs-in-london").text
    soup = BeautifulSoup(html_text, "lxml")
    job_box = soup.find_all("article", class_= "card job-card_jobCard__B4kku")
    #A for loop to cycle throguh the jobs in the page
    for jobs in (job_box):
        #Create a filter to search for specific terms in the job titles example "Junior"
        job_name = jobs.find("h2", class_ = "job-card_jobResultHeading__title__orCi1").text.upper()
        if specs in job_name:
           
            company_name_date_posted = jobs.find("div", class_ = "job-card_jobResultHeading__postedBy__CSbuP").text
            pay = jobs.find("li", class_ = "job-card_jobMetadata__item__ESnn5 list-group-item" ).text
            base_url = jobs.div.h2.a["href"]    
            url = "https://reed.co.uk"+base_url

            print("Role:", job_name)
            print("Date posted & Company:", company_name_date_posted)
            print("Salary:", pay)
            print("URL:", url )
            print("-----------------------")

find_jobs()
        
