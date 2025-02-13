import pandas as pd
from datetime import datetime
import os
from flask import Flask, render_template

app = Flask(__name__)

# Function to load existing data or create a new one
def load_data():
    filename = "order_data.xlsx"
    if os.path.exists(filename):
        return pd.read_excel(filename)
    else:
        return pd.DataFrame(columns=["day", "quantity", "cost_jpn", "cost_vnd", "revenue", "profit"])

# Function to format currency
def format_currency(value):
    return f"{value:,}".replace(",", ".")  # Convert to thousand separator using dot

# Function to generate coin pricing table for iOS
def generate_coin_pricing_ios():
    data = {
        "Gói Coin": [130, 300, 550, 750, 1040, 2130, 3250, 5700, 12800],
        "Giá bán (VND)": [36500, 81500, 142500, 187500, 248500, 478500, 708500, 1135000, 2350000]
    }
    df = pd.DataFrame(data)
    df["Giá bán (VND)"] = df["Giá bán (VND)"].apply(format_currency)  # Apply formatting
    return df

# Function to generate coin pricing table for Android
def generate_coin_pricing_android():
    data = {
        "Gói Coin": [130, 300, 550, 750, 1040, 2130, 3250, 5700, 12800],
        "Giá bán (VND)": [36500, 81500, 142500, 187500, 248500, 478500, 708500, 1135000, 2350000]
    }
    df = pd.DataFrame(data)
    df["Giá bán (VND)"] = df["Giá bán (VND)"].apply(format_currency)  # Apply formatting
    return df

@app.route('/')
def index():
    df_ios = generate_coin_pricing_ios()
    df_android = generate_coin_pricing_android()
    background_image = "static/images/football.jpg"  # Updated path to the new image
    anime_character_image = "static/images/ronaldo.jpg"  # Path to the anime character image
    
    return render_template('index.html', 
                           tables=[df_ios.to_html(classes='table table-bordered table-hover text-center fs-3', index=False, border=0),
                                   df_android.to_html(classes='table table-bordered table-hover text-center fs-3', index=False, border=0)],
                           title="Bảng Giá Nạp Coin",
                           background_image=background_image,
                           anime_character_image=anime_character_image)

if __name__ == "__main__":
    app.run(debug=True)
