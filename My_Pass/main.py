from tkinter import *
import random
from tkinter import messagebox
import re
from password_generator import generate_password
from validate import validate_email, validate_website, validate_password
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password_local():
    password_input.delete(0, END)
    password = generate_password()
    # password = ""
    # for _ in range(0, 12):
    #     password += chr(random.randint(33, 126))
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if not validate_website(website) or website == "https://" or website == "" or website == "http://":
        messagebox.showerror(title="Error", message="Invalid website")
        return
    if not validate_email(email):
        messagebox.showerror(title="Error", message="Invalid email")
        return
    if not validate_password(password): 
        messagebox.showerror(title="Error", message="Invalid password")
        return
 
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open(".env", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        website_input.delete(0, END)
        password_input.delete(0, END)
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

website_input = Entry(width=35, fg=BLACK, bg=WHITE, highlightthickness=0 )
website_input.grid(column=1, row=1, columnspan=2)
website_input.insert(0, "https://")
website_input.focus()

email_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, justify="right")
email_label.grid(column=0, row=2, sticky="E")

email_input = Entry(width=35, fg=BLACK, bg=WHITE, highlightthickness=0)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "frozzel@me.com")

password_label = Label(text="Password:", fg=BLACK, bg=WHITE)
password_label.grid(column=0, row=3, sticky="E")

password_input = Entry(width=19, fg=BLACK, bg=WHITE, highlightthickness=0)
password_input.grid(column=1, row=3)

# ---------------------------- BUTTONS ------------------------------- #

password_button = Button(text="Generate Password", width=12,  fg=BLACK, bg=WHITE, highlightbackground=WHITE, command=generate_password_local)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, highlightbackground=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()