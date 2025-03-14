import smtplib  
from dotenv import load_dotenv
import os
load_dotenv()

my_email = os.getenv("EMAIL")
my_password =  os.getenv("PASSWORD")
send_to_email = os.getenv("CLOUD")

def send_email(quote):
    with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=send_to_email, 
                    msg=f"{quote}")
        print("Email Sent")
        
        