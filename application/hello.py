import requests
from bs4 import BeautifulSoup

all_jobs = []


def scrape_page(url):
    response = requests.get(url)
    print(f"scrapping page {url} ...")
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        region = job.find("span", class_="region company")
        companys = job.find_all("span", class_="company")

        if region != None:
            region = region.text

        if len(companys) == 3:
            company, position, _ = companys
        else:
            company, position = companys

        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)


def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))


total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")


for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x + 1}"
    scrape_page(url)

for job in all_jobs:
    print(job)

print(len(all_jobs))
