
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_scientists(self):
        current_url = self.base_url
        all_scientists = []
        while current_url:
            response = requests.get(current_url)
            if response.status_code != 200:
                print(
                    f"Failed to retrieve page {current_url}. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            all_scientists.extend(self.extract_scientists_from_page(soup))

            # Check for the next page link
            next_button = soup.find("button", class_="a-link--next")
            current_url = next_button['href'] if next_button else None

        return all_scientists

    def extract_scientists_from_page(self, soup):
        scientist_rows = soup.find_all("tr", class_="o-person-list__table-tr")
        scientists = []

        for row in scientist_rows:
            name_tag = row.find("a", class_="o-person-list__link")
            if not name_tag:
                continue

            name = " ".join([span.text for span in name_tag.find_all(
                "span") if not span.has_attr("class")])
            profile_link = name_tag['href']
            image_tag = name_tag.find("img")
            image_url = image_tag['src'] if image_tag else None
            role = row.find_all("td")[1].find("span").text if row.find_all("td")[
                1].find("span") else None
            email_tag = row.find("a", href=lambda x: x and "mailto:" in x)
            email = email_tag['href'].replace(
                "mailto:", "") if email_tag else None
            phone_number_tag = row.find_all("td")[3].find("span")
            phone_number = phone_number_tag.text if phone_number_tag else None
            location = " ".join(
                [span.text for span in row.find_all("td")[4].find_all("span")])

            scientist_data = {
                "name": name,
                "profile_link": profile_link,
                "image_url": image_url,
                "role": role,
                "email": email,
                "phone_number": phone_number,
                "location": location
            }
            scientists.append(scientist_data)
