import math

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    sh_br_sec = SHORT_BREAK_MIN * 60
    ln_br_sec = LONG_BREAK_MIN * 60
    work_min = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(ln_br_sec)
        label.config(text="Long Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
    if reps % 2 == 0:
        count_down(sh_br_sec)
        label.config(text="Short Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
    if reps % 2 != 0:
        count_down(work_min)
        label.config(text="Work Time", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min, count_second = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_second:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)

# PhotoImage
tomato_img = PhotoImage(file="tomato.png")

# Label
label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), foreground=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Creating the start timer button
button = Button(text="Start", command=start_timer, padx=3, pady=3, bg="white", highlightthickness=0)
button.grid(column=0, row=2)

button1 = Button(text="Reset", command=reset_timer, padx=3, pady=3, bg="white", highlightthickness=0)
button1.grid(column=2, row=2)

# Checkmark Label
checkmark = Label(text="✔", fg=GREEN, background=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
