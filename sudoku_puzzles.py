import requests
from bs4 import BeautifulSoup
import csv

def extract_product_info(product):
    """Extract name, price, and rating from one product block."""
    title = product.h3.a['title']
    price = product.select_one('.price_color').text.replace('£', '')
    rating = product.select_one('p')['class'][1]  # e.g., "Three"
    
    return {
        'title': title,
        'price': price,
        'rating': rating
    }

def scrape_products(pages_to_scrape=1):
    """Scrape products from the specified number of pages."""
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    products = []

    for page in range(1, pages_to_scrape + 1):
        print(f"Scraping page {page}...")
        response = requests.get(base_url.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select('.product_pod')

        for item in items:
            product_data = extract_product_info(item)
            products.append(product_data)

    return products

def save_to_csv(data, filename='products.csv'):
    """Save the extracted product data to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"\n✅ Data saved successfully to {filename}")

def main():
    print("📦 Product Scraper - Books to Scrape Edition")
    try:
        pages = int(input("Enter the number of pages to scrape (1–50): "))
        if not 1 <= pages <= 50:
            print("⚠️ Please enter a number between 1 and 50.")
            return
    except ValueError:
        print("⚠️ Invalid input. Please enter a numeric value.")
        return

    product_list = scrape_products(pages)
    save_to_csv(product_list)

if __name__ == "__main__":
    main()
