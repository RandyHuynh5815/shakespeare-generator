from bs4 import BeautifulSoup
import requests
import os
from typing import List

LINK = "http://shakespeare.mit.edu"

# Hints:
# Documentation for BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def scraped_links(link: str) -> List[str]:
    # TODO: Get retrieve contents of the page and create soup
    scrape_links = []
    # TODO: Get all the links we needed from our main source and return them, we only need the links [2:-7]
    for link in list():
        scrape_links.append(link)
    return scrape_links

def extract_contents(scrape_links: List[str]) -> None:
    for l in scrape_links:
        # TODO: Make the link that we are going to scrape from
        link = None
        # TODO: Gather the contents from that link
        response = None
        if (response.ok):
            # TODO: Create soup for each link that we scraped
            blocks = []
            file_name = f"data/{l}.txt"
            f = open(file_name, 'x')
            with open(file_name, 'a') as f: # For each file made
                pass # TODO: Write the text onto the opened file

def main() -> None:
    links = scraped_links(LINK)
    print("We are going to scrape", len(links), "links.")
    os.mkdir('data')
    extract_contents(links)
    print("Data now loaded. Now create thy markov chains.")
        
        

if __name__ == "__main__":
    if not os.path.exists((os.getcwd()+"/data")):
        main()
    else:
        print("Data already created, no need to make them again.")
