import requests 
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/viewjob?jk=0be852a756d74baf&hl=en"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(role="alert")

print(results.prettify())

job_elements = results.find_all("div", class_="icl-Alert-headline")

