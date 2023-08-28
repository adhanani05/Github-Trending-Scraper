import requests
from bs4 import BeautifulSoup
import csv


file_name = "github_trending_today.csv"
f = csv.writer(open(file_name, "w", newline=""))
f.writerow(['Developer', 'Repo Name', 'Number of Stars'])


source = requests.get("https://github.com/trending")
source.raise_for_status()


soup = BeautifulSoup(source.text, "html.parser")


repos = soup.find("div", class_="Box").find_all("article", class_="Box-row")

for repo in repos:
    
    repo_info = repo.find("a", class_="Link").text.split("/")
    title = repo_info[0].strip()
    name = repo_info[1].strip()
    stars_all_time = repo.find("a", class_="Link Link--muted d-inline-block mr-3").text.strip()
    #stars_today_placeholder = repo.find("span", class_="d-inline-block float-sm-right").text.split(" ")
    #stars_today = stars_today_placeholder[8].strip()
    
    print("Title:", title)
    print("Developer:", name)
    print("Stars all time:", stars_all_time)
    #print("Stars today:", stars_today)
    
    f.writerow([name, title, stars_all_time])

