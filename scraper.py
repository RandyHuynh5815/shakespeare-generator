from bs4 import BeautifulSoup
import requests
import time
import os
from typing import List

LINK = "http://shakespeare.mit.edu"

def scraped_links(link: str) -> List[str]:
    home = requests.get(link)
    soup = BeautifulSoup(home.content, 'html.parser')
    scrape_links = []
    for link in soup.find_all('a')[2:-7]:
        scrape_links.append(link.get('href').split("/")[0])
    return scrape_links

def extract_contents(scrape_links: List[str]) -> None:
    for l in scrape_links:
        link = LINK + "/" + l + "/full.html"
        response = requests.get(link)
        if (response.ok):
            soup = BeautifulSoup(response.content, 'html.parser')
            blocks = soup.find_all('blockquote')
            file_name = f"data/{l}.txt"
            f = open(file_name, 'x')
            with open(file_name, 'a') as f:
                for b in blocks:
                    f.write(b.get_text())
        
        

if __name__ == "__main__":
    links = scraped_links(LINK)
    print(len(links))
    #os.mkdir('data')
    #extract_contents(links)
