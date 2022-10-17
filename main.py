import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
PYTHON = 90
LUNCH = 90
IELTS = 60
BREAKFAST = 30
UI_DESIGN = 60
LEASURE_TIME = 90
DINNER = 90
SMC_CRYPTO = 60
BOUNTY = 120
TECHNICAL = 60
SHORT_BREAK_MIN = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00.00")
    title_label.config(text="Start", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    python_sec = PYTHON * 60
    lunch_sec = LUNCH * 60
    ielts_sec = IELTS * 60
    breakfast_sec = BREAKFAST * 60
    ui_design_sec = UI_DESIGN * 60
    leasure_time_sec = LEASURE_TIME * 60
    dinner_sec = DINNER * 60
    smc_sec = SMC_CRYPTO * 60
    bounty_sec = BOUNTY * 60
    technical_sec = TECHNICAL * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    # if it's the 8th rep:
    if reps % 3 == 0 and reps == 3:
        count_down(breakfast_sec)
        title_label.config(text="Breakfast", fg=RED)

    elif reps % 5 == 0 and reps == 5:
        count_down(ielts_sec)
        title_label.config(text="Ielts reading ", fg=RED)

    elif reps % 7 == 0 or reps % 13 == 0 or reps % 17 == 0 or reps % 23 == 0:
        count_down(python_sec)
        title_label.config(text="python", fg=RED)

    elif reps % 9 == 0 and reps == 9:
        count_down(lunch_sec)
        title_label.config(text="Make lunch", fg=RED)

    elif reps % 11 == 0 and reps == 11:
        count_down(ui_design_sec)
        title_label.config(text="UI Design", fg=RED)

    elif reps % 15 == 0:
        count_down(leasure_time_sec)
        title_label.config(text="Leasure_Time ", fg=RED)

    elif reps % 19 == 0:
        count_down(dinner_sec)
        title_label.config(text="Make Dinner", fg=RED)

    elif reps % 21 == 0:
        count_down(smc_sec)
        title_label.config(text="Crypto SMC", fg=RED)

    elif reps % 25 == 0:
        count_down(bounty_sec)
        title_label.config(text="Airdrops", fg=RED)


    # if it's the 2nd,4th,6th,8th,10th,12th,14th,16th,18th,20th,22th,24th,26th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    #if it's the 1st rep:
    else:
        count_down(technical_sec)
        title_label.config(text="Analyze", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks +="✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pandaicon.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="red", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()