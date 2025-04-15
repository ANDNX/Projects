from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read the CSV file
    try:
        df = pd.read_csv('amazon_products.csv')
        products = df.to_dict('records')
        return render_template('index.html', products=products)
    except FileNotFoundError:
        return "No products data available. Please run the scraper first."

if __name__ == '__main__':
    app.run(debug=True)
