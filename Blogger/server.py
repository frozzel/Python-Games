from flask import Flask, render_template, request
import requests
import datetime
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()



app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template('index.html', posts=res.json())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    def send_email(name, email, phone, message):
        my_email = os.getenv("EMAIL")
        my_password = os.getenv("PASSWORD")
        with smtplib.SMTP('smtp.gmail.com', 587) as conn:
            conn.starttls()
            conn.login(user=my_email, password=my_password)
            conn.sendmail(from_addr=email, to_addrs=my_email,
                          msg=f"Subject:New message from {name}\n\nYou got a new message from Blogger Site:\n From: {name}\n Email: {email}\nPhone: {phone}\nMessage:\n{message}")
            
            
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        # Here you would typically send the message to an email or store it in a database
        phone = data.get('phone')
        # Send email
        send_email(name, email, phone, message)
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

@app.route('/<int:post_id>')
def post_detail(post_id):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', title=post['title'], subtitle=post['subtitle'], body=post['body'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)