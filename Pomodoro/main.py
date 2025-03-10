from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 
    count_down(5 * 60)

def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(count_down)
    check_marks_label.config(text="")
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
count = 5

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count == 0:
        canvas.itemconfig(timer_text, text="Times Up!")    
        return
    else:
        window.after(1000, count_down, count - 1) 

# ---------------------------- UI SETUP ------------------------------- #



########## TIMER  Label ##########
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)


########## CHECK MARKS Label ##########
check_marks_label = Label(text="✔", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_marks_label.grid(column=1, row=3)

########## START Button ##########
    
start_button = Button(text="Start", command=start_timer, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

############ RESET Button ############

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)





window.mainloop()