# Scientist Scraper User Manual

## Introduction

The Scientist Scraper is a web application designed to follow scientists on social media from all Danish universities and analyze their research for commercial potential. The goal is to increase dealflow and leads for our venture capital firm. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the application.

## Installation

To install the Scientist Scraper, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the repository from GitHub or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the directory where you have cloned or extracted the source code.

4. Create a virtual environment to isolate the dependencies of the application. Run the following command:

   ```bash
   python -m venv venv
   ```

5. Activate the virtual environment. Run the following command:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

6. Install the required dependencies. Run the following command:

   ```bash
   pip install -r requirements.txt
   ```

7. The installation is now complete.

## Usage

To use the Scientist Scraper, follow these steps:

1. Make sure you have activated the virtual environment as mentioned in the installation steps.

2. Open a terminal or command prompt and navigate to the directory where you have cloned or extracted the source code.

3. Run the following command to start the web application:

   ```bash
   python main.py
   ```

4. The web application will start and a window will appear.

5. In the application window, you will see a label with the text "Welcome to Scientist Scraper" and a button labeled "Start Scraper".

6. Click the "Start Scraper" button to initiate the scraping process.

7. The application will scrape scientists' social media profiles from all Danish universities and analyze their research for commercial potential.

8. Once the scraping process is finished, the label in the application window will be updated to "Scraper finished".

9. The leads with commercial potential will be saved in a file named "leads.txt" in the same directory as the source code.

10. You can view the leads by opening the "leads.txt" file.

11. You can close the application window to stop the web application.

## Conclusion

The Scientist Scraper is a powerful tool for following scientists on social media from all Danish universities and analyzing their research for commercial potential. By using this web application, you can increase dealflow and leads for your venture capital firm. Follow the installation and usage instructions provided in this user manual to get started with the Scientist Scraper.