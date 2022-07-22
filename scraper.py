from bs4 import BeautifulSoup
import requests

# Example of Expired Job URL Hardcoded variable
URL = "https://www.indeed.com/viewjob?jk=0be852a756d74baf&hl=en"

# Setting a HTTP GET request to this URL
result = requests.get(URL)

# Parses HTML of Web Page
soup = BeautifulSoup(result.content, "html.parser")

# Finds the role="alert" specific to expired jobs
results = soup.find(role="alert")


print(results.prettify())

job_elements = results.find_all("div", class_="icl-Alert-headline")
