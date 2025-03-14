import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random
load_dotenv()

my_email = os.getenv("EMAIL")
my_password =  os.getenv("PASSWORD")
send_to_email = os.getenv("CLOUD")

def send_email(quote):
    with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=send_to_email, 
                    msg=f"Subject:Quote of The Day!\n\n{quote}")
        
def get_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = quotes[random.randint(0, len(quotes) - 1)]
        return quote

now = dt.datetime.now()
week_day = now.weekday()
print(week_day)

if week_day == 0:
    quote = get_quote()
    print(quote)
    # send_email(quote)
    print("Email Sent")