
'''
This file contains the Scraper class, which is responsible for scraping social media platforms to get information about scientists.
'''
import logging as logging
from scientist import Scientist
import requests
from bs4 import BeautifulSoup


class Scraper:
    def get_scientists(self):
        '''
        Retrieves a list of scientists from Danish universities from social media platforms.
        Returns:
        - A list of Scientist objects representing the scientists.
        '''
        # For demonstration purposes, we're scraping the University of Copenhagen's Institute of Cellular and Molecular Medicine
        url = "https://icmm.ku.dk/english/staff/?pure=en/organisations/by-uuid(2c041a11-83ef-4c4e-b852-1e1b3386b6f8)/persons.html"

        # Initializing the logger
        logger = logging.getLogger(__name__)

        # Logging the start of the scraping process
        logger.info("Starting scraping for University")

        response = requests.get(url)
        scientists = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for person in soup.select(".person"):
                name = person.select_one(".name").text.strip()
                title = person.select_one(".title").text.strip()
                # For each scientist, create a Scientist object and add it to the list
                scientists.append(Scientist(name, title))
                logger.info(f"Scraped scientist: {name} with title: {title}")

        return scientists

    def get_research(self, scientist):
        '''
        Retrieves the research of a scientist from social media platforms.
        Parameters:
        - scientist: A Scientist object representing the scientist.
        Returns:
        - A string representing the research of the scientist.
        '''
        # Placeholder code to scrape social media platforms and retrieve research
        research = ""
        # Add code to retrieve research for the given scientist
        return research
