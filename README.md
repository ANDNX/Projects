# Ecommerce Web Scraper and Frontend

This project consists of two main components:
1. A web scraper that collects product data from Amazon
2. A Flask-based frontend to display the scraped data in a modern ecommerce interface

## Features

- Web scraping of Amazon product data (name, price, rating, reviews)
- Modern, responsive frontend design
- Product cards with hover effects
- Star rating display
- Clean and intuitive user interface

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. First, run the scraper to collect product data:
```bash
python import_requests.py
```

2. Start the Flask application:
```bash
python frontend.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
.
├── frontend.py          # Flask application
├── import_requests.py   # Web scraper
├── requirements.txt     # Project dependencies
├── templates/          # HTML templates
│   └── index.html     # Main template
└── README.md          # Project documentation
```

## Dependencies

- Flask
- Pandas
- Requests
- BeautifulSoup4

## Website
![Screenshot 2025-04-15 215558](https://github.com/user-attachments/assets/1b3cc21c-f12c-483d-9cd1-7e60ec16c934)
