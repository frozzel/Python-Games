import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random
load_dotenv()

my_email = os.getenv("EMAIL")
my_password =  os.getenv("PASSWORD")

def send_email(name, email, letter):
    with  smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(from_addr=my_email, to_addrs=email, 
                    msg=f"Subject:Happy Birthday!\n\n{letter.replace('[NAME]', name)}")
        
def get_letter():
    letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open(f"letter_templates/{random.choice(letter_templates)}") as file:
        letter = file.read()
        return letter
    
def get_birthdays():
    with open("birthdays.csv") as file:
        birthdays = file.readlines()
        return birthdays
    
def get_birthday_dict(birthdays):
    birthday_dict = {}
    for birthday in birthdays:
        data = birthday.split(",")
        birthday_dict[(int(data[3]), int(data[4]))] = data
    return birthday_dict

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthdays = get_birthdays()
birthday_dict = get_birthday_dict(birthdays)

if (today_month, today_day) in birthday_dict:
    data = birthday_dict[(today_month, today_day)]
    name = data[0]
    email = data[1]
    letter = get_letter()
    send_email(name, email, letter)
    print("Email Sent")
else:
    print("No birthday today")
    