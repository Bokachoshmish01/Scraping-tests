from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import  ChromeDriverManager
import pandas as pd
a=0
joblist=[]
for p in range(1,10):

    url=f"Link....{p}"

    chrome_options=Options()
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get(url)

    postings = driver.find_element("id", "jobList")
    posting = postings.find_element("xpath", "//div[@class='boxed']/div")
    jobs = posting.find_elements("xpath", "//div[@class='col-sm-12']")
    print(len(jobs))

    title = jobs[1].find_elements("xpath", "//div[@class='job-title-text']/a")
    company = jobs[2].find_elements("xpath", "//div[@class='comp-name-text']")
    location = jobs[3].find_elements("xpath", "//div[@class='locon-text-d']")
    education = jobs[4].find_elements("xpath", "//div[@class='edu-text-d']/ul/li")
    exp = jobs[5].find_elements("xpath", "//div[@class='exp-text-d']")

    for x in range(1, 50):    
        if x>=len(title):
            print("End of page !")
            break
        
        job_dictionary={
            "title":title[x].text,
            "Company Name": company[x].text,
            "Location": location[x].text ,
            "Education": education[x].text if 0 <= x < len(education) else "Not Mentioned",
            "Experience": exp[x].text
        }
        joblist.append(job_dictionary)
        print(job_dictionary)
    driver.close()
    print("page ended ",a)
    a=a+1
frame=pd.DataFrame(joblist)
frame.to_csv("Garment Jobs.csv",index=False)
