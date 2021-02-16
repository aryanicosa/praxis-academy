from bs4 import BeautifulSoup
import requests
import time

BASE_URL = input("Ketik alamat web : ") # url to scrap
STORY_LINK = []

for i in range(10): # lakukan 10 kali request
    response = requests.get(f"{BASE_URL}news?p={i}")
    soup = BeautifulSoup(response.content, "html.parser")
    stories = soup.find_all("a", attrs={"class":"storylink"})
    links = [x["href"] for x in stories if "http" in x["href"]]
    STORY_LINK += links
    time.sleep(0.25) # jeda per 1 loop
    
print(len(STORY_LINK))

for url in STORY_LINK[:3]:
    print(url)