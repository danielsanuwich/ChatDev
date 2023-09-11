'''
This is the main file of the web application. It contains the main function that starts the application and handles user interactions.
'''
import tkinter as tk
from scraper import Scraper
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientist Scraper")
        self.geometry("400x300")
        self.scraper = Scraper()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Scientist Scraper")
        self.label.pack(pady=10)
        self.button = tk.Button(self, text="Start Scraper", command=self.start_scraper)
        self.button.pack(pady=10)
    def start_scraper(self):
        self.scraper.scrape_scientists()
        self.label.config(text="Scraper finished")
if __name__ == "__main__":
    app = Application()
    app.mainloop()