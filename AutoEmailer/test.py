import smtplib
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()


# my_email = os.getenv("EMAIL")
# my_password =  os.getenv("PASSWORD")
# send_to_email = os.getenv("CLOUD")

# with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
#     conn.starttls()
#     conn.login(user=my_email, password=my_password)
#     conn.sendmail(from_addr=my_email, to_addrs=send_to_email, 
#                 msg="Subject:TEST WITH PYTHON\n\nWhen you start to do the things that you truly love, it wouldn't matter whether it is Monday or Friday; you would be so excited to wake up each morning to work on your passions.")


now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
date = f"{day}/{month}/{year}"
print(date)