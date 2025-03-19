import requests
import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

# ----------------- Constants ----------------- #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_up = "🔺"
today_opening_price = 0
yesterday_closing_price = 0
stock_change = 0
news = []
my_email = os.getenv("EMAIL")
my_password =  os.getenv("PASSWORD")
send_to_email = os.getenv("CLOUD")



# ----------------- Get Stocks ----------------- #
def calculate_percentage_difference(yesterday_closing_price, day_before_yesterday_closing_price):
    return round(abs(yesterday_closing_price - day_before_yesterday_closing_price) / day_before_yesterday_closing_price * 100)

def stock_price():
    global stock_up, today_opening_price, yesterday_closing_price, stock_change
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": os.getenv("ALPHA_AVANTAGE_API_KEY")
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()
    data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
    today_data = data_list[0]
    today_opening_price = round(float(today_data["1. open"]))
    yesterday_data = data_list[1]
    yesterday_closing_price = round(float(yesterday_data["4. close"]))
    
    if yesterday_closing_price > today_opening_price:
        stock_up = "🔻"
    else:
        stock_up = "🔺"
    stock_change = calculate_percentage_difference(yesterday_closing_price, today_opening_price)   

    return f"{STOCK_NAME}: {stock_up}{stock_change}%"

print(stock_price())

# ----------------- Get News ----------------- #
def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": os.getenv("NEWS_API_ORG_API_KEY")
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()
    news = data["articles"][:3]
    return news


# ----------------- Send Email ----------------- #
def send_email(quote):
    print("Sending email")
    with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=send_to_email, msg=f"Subject:Stock News for {COMPANY_NAME}\n\n{quote}")
    
if stock_change >= 1:
   
    news = get_news()

    for article in news:
        title = article["title"]
        description = article["description"]
        link = article["url"]   
        quote = f"{STOCK_NAME}: {stock_up}{stock_change}%\nHeadline: {title}\nBrief: {description}\nLink: {link}" 
        send_email(quote)
        print("Email sent")
else:
    print("Stock change is less than 5%")

