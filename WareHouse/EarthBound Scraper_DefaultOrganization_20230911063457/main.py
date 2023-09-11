'''
This is the main file of the paperscraper software. It contains the main function that is responsible for running the application.
'''
from scraper import Scraper
from analyzer import Analyzer
from gui import GUI
def main():
    # Create instances of the scraper, analyzer, and GUI classes
    scraper = Scraper()
    analyzer = Analyzer()
    gui = GUI()
    # Get the list of scientists from the scraper
    scientists = scraper.get_scientists()
    # Analyze the research of each scientist
    for scientist in scientists:
        research = scraper.get_research(scientist)
        commercial_potential = analyzer.analyze_research(research)
        scientist.set_commercial_potential(commercial_potential)
    # Display the results in the GUI
    gui.display_results(scientists)
if __name__ == "__main__":
    main()