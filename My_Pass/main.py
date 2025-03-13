from tkinter import *
import random
from tkinter import messagebox
import re
from password_generator import generate_password
from validate import validate_email, validate_website, validate_password
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"
RED = "#d84038"
GREEN = "#6A9C89"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password_local():
    password_input.delete(0, END)
    password = generate_password()
    # password = ""
    # for _ in range(0, 12):
    #     password += chr(random.randint(33, 126))
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- Search PASSWORD ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for the {website} exists")
    finally:
        try:
            pyperclip.copy(password)
        except UnboundLocalError:
            pass
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.insert(0, "https://")
            website_input.focus()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if not validate_website(website) or website == "https://" or website == "" or website == "http://":
        messagebox.showerror(title="Error", message="Invalid website")
        return
    if not validate_email(email):
        messagebox.showerror(title="Error", message="Invalid email")
        return
    if not validate_password(password): 
        messagebox.showerror(title="Error", message="Invalid password")
        return
 
    # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all the fields")
        
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                   
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END) 
                 
        else:  
            data.update(new_data)
            with open("data.json", "w") as data_file:  
                json.dump(data, data_file, indent=4) 
                
        finally:    
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.insert(0, "https://")
            website_input.focus()
                
        
    
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

# ---------------------------- CANVAS ------------------------------- #

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# ---------------------------- LABELS ------------------------------- #
website_label = Label(text="Website:", fg=BLACK, bg=WHITE,)
website_label.grid(column=0, row=1, sticky="E" )

website_input = Entry(width=21, fg=GREEN, bg=WHITE, highlightthickness=0 )
website_input.grid(column=1, row=1,)
website_input.insert(0, "https://")
website_input.focus()

email_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, justify="right")
email_label.grid(column=0, row=3, sticky="E")

email_input = Entry(width=37, fg=GREEN, bg=WHITE, highlightthickness=0)
email_input.grid(column=1, row=3, columnspan=2)
email_input.insert(0, "frozzel@me.com")

password_label = Label(text="Password:", fg=BLACK, bg=WHITE)
password_label.grid(column=0, row=2, sticky="E")

password_input = Entry(width=21, fg=GREEN, bg=WHITE, highlightthickness=0)
password_input.grid(column=1, row=2)

# ---------------------------- BUTTONS ------------------------------- #

password_button = Button(text="Generate Password", width=12,  fg=RED, highlightbackground=WHITE, command=generate_password_local)
password_button.grid(column=2, row=2)

add_button = Button(text="Add", width=32, fg=GREEN, highlightbackground=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=12, fg=RED, highlightbackground=WHITE, command=search)
search_button.grid(column=2, row=1)


window.mainloop()