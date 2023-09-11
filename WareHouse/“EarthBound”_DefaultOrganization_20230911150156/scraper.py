'''
This file contains the Scraper class that is responsible for scraping scientists' social media and analyzing their research for commercial potential.
'''
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        # Replace with actual university names
        self.universities = ["Denmarks Technical University",
                             "DTU", "Denmark's Technical University"]

    def scrape_scientists(self):
        for university in self.universities:
            scientists = self.get_scientists(university)
            for scientist in scientists:
                research = self.get_research(scientist)
                commercial_potential = self.analyze_research(research)
                if commercial_potential:
                    self.save_lead(scientist, commercial_potential)

    def get_scientists(self, university):
        '''
        Retrieves a list of scientists from social media based on the given university.
        Args:
            university (str): The name of the university.
        Returns:
            list: A list of scientist names.
        '''
        scientists = []
        url = f"https://example.com/{university}/scientists"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            scientist_elements = soup.find_all("div", class_="scientist")
            for scientist_element in scientist_elements:
                scientist_name = scientist_element.find("h2").text
                scientists.append(scientist_name)
        return scientists

    def get_research(self, scientist):
        '''
        Retrieves the research information for a given scientist.
        Args:
            scientist (str): The name of the scientist.
        Returns:
            list: A list of research titles.
        '''
        research = []
        url = f"https://example.com/scientists/{scientist}/research"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            research_elements = soup.find_all("div", class_="research")
            for research_element in research_elements:
                research_title = research_element.find("h3").text
                research.append(research_title)
        return research

    def analyze_research(self, research):
        '''
        Analyzes the research titles for commercial potential.
        Args:
            research (list): A list of research titles.
        Returns:
            bool: True if there is commercial potential, False otherwise.
        '''
        commercial_potential = False
        for research_title in research:
            if "commercial" in research_title.lower():
                commercial_potential = True
                break
        return commercial_potential

    def save_lead(self, scientist, commercial_potential):
        '''
        Saves the lead in the venture capital firm's database.
        Args:
            scientist (str): The name of the scientist.
            commercial_potential (bool): The commercial potential of the research.
        '''
        with open("leads.txt", "a") as file:
            file.write(
                f"Scientist: {scientist}, Commercial Potential: {commercial_potential}\n")
