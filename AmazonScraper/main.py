import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B075CYMYK6/ref=sr_1_8?crid=3HP3DBJOHR9E4&dib=eyJ2IjoiMSJ9.ykp3bhzHbWzQ1ZgOfxti9pRnmAaF4wiyDYqhTW65GVmnyE14xTeutXBbjBR9j_GQzMNiczvK-8m5tTtlJu6X8FHLXd6ww7Qbjvkhrxpc1SRs4a7H0hi2gfGle2daztTePWjeKZ0V48HufROAT9BOPcETAqEAcKGnwG1HziSAPoe0z_06UuUBCRAl_qcdVvuhn49lP2pHApZi2ghc0OHorN2ci9wpHPvsDL0zj3lvNcPoNGK8c1FCRttbBdavbR_NvhU23uz9DYTXeprv5eWYKA1PsdsqfLvrdHgX441qg841qHUpMdUik3vGn5DJPfieTKFLNeh_xsAw0JrZyNJ5V6q8C1JNgqDr2Sg73aLi-1g.OWM8QgfLQD-CqTHYDzIIHemsVxM6ebIOpY3R3Q3ZD5w&dib_tag=se&keywords=instant%2Bpot&qid=1743523267&s=home-garden&sprefix=inst%2Cgarden%2C213&sr=1-8&ufe=app_do%3Aamzn1.fos.9fe8cbfa-bf43-43d1-a707-3f4e65a4b666&th=1"

# Write your code below this line 👇

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(URL, headers=header)
instant_pot = response.text

soup = BeautifulSoup(instant_pot, 'html.parser')

current__price = float(soup.find(name='span', class_='a-offscreen').getText().split("$")[1])
print(current__price)

# send email if price drops below 100

if current__price < 100:
    my_email = os.getenv("EMAIL")
    my_password = os.getenv("PASSWORD")
    send_to_email = os.getenv("CLOUD")

    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=send_to_email,
                      msg=f"Subject: Instant Pot Price Drop!\n\nThe price of the Instant Pot has dropped to ${current__price}.\n\nBuy it now at {URL}")
        print("Email Sent")
else:
    print("Price is still high")