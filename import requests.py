import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def amazon_scraper(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize lists to store product information
        product_names = []
        prices = []
        ratings = []
        review_counts = []
        
        # Find all product containers
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        for product in products:
            # Extract product name
            name = product.find('span', {'class': 'a-text-normal'})
            name = name.text.strip() if name else 'N/A'
            product_names.append(name)
            
            # Extract price
            price = product.find('span', {'class': 'a-price-whole'})
            price = price.text.strip() if price else 'N/A'
            prices.append(price)
            
            # Extract rating
            rating = product.find('span', {'class': 'a-icon-alt'})
            rating = rating.text.split()[0] if rating else 'N/A'
            ratings.append(rating)
            
            # Extract review count
            review = product.find('span', {'class': 'a-size-base'})
            review = review.text.strip() if review else 'N/A'
            review_counts.append(review)
        
        # Create a DataFrame with the scraped data
        data = {
            'Product Name': product_names,
            'Price': prices,
            'Rating': ratings,
            'Review Count': review_counts
        }
        df = pd.DataFrame(data)
        
        # Save to CSV
        df.to_csv('amazon_products.csv', index=False)
        print("Data successfully scraped and saved to 'amazon_products.csv'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with your Amazon search URL
    amazon_url = "https://www.amazon.com/s?k=laptop"  # Example search for laptops
    
    # Add delay to avoid getting blocked
    time.sleep(2)
    amazon_scraper(amazon_url)
