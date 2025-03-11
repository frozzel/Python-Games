from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, justify="right")
email_label.grid(column=0, row=2, sticky="E")

email_input = Entry(width=35, fg=BLACK, bg=WHITE, highlightthickness=0)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", fg=BLACK, bg=WHITE)
password_label.grid(column=0, row=3, sticky="E")

password_input = Entry(width=19, fg=BLACK, bg=WHITE, highlightthickness=0)
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=12,  fg=BLACK, bg=WHITE, highlightbackground=WHITE)
password_button.grid(column=2, row=3)

# ---------------------------- BUTTONS ------------------------------- #

add_button = Button(text="Add", width=32, highlightbackground=WHITE)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()