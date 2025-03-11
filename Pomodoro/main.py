from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_marks_label.config(text="")
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(): 
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    REPS += 1
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
count = 5

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks= ""
        for _ in range(math.floor(REPS/2)):
            marks += "✔"
        check_marks_label.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #



########## TIMER  Label ##########
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)


########## CHECK MARKS Label ##########
check_marks_label = Label(text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_marks_label.grid(column=1, row=3)

########## START Button ##########
    
start_button = Button(text="Start", command=start_timer, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

############ RESET Button ############

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)





window.mainloop()