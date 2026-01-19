import requests
from bs4 import BeautifulSoup
import csv

# The Problem: Gathering data manually takes too long.
# The Solution: Scrape quotes and authors into a CSV file.

URL = "http://quotes.toscrape.com"

def scrape_quotes():
    print(f"Connecting to {URL}...")
    
    try:
        response = requests.get(URL)
        # Check if the website accepted our request (Status 200 = OK)
        if response.status_code != 200:
            print(f"Error: Failed to load page. Status code: {response.status_code}")
            return

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote blocks (specific to this website structure)
        quotes = soup.find_all('div', class_='quote')
        
        data = []
        
        print(f"Found {len(quotes)} quotes. Extracting data...")

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            data.append([author, text])

        # Save to CSV (Excel compatible)
        save_to_csv(data)

    except Exception as e:
        print(f"An error occurred: {e}")

def save_to_csv(data):
    filename = 'quotes_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Author', 'Quote']) # Header
        writer.writerows(data)
    
    print(f"Success! Data saved to '{filename}'")

if __name__ == "__main__":
    scrape_quotes()