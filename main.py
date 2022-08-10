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
REPS = 0
my_timer = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS

    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    check_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", foreground=RED)
    elif REPS % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", foreground=GREEN)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", foreground=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        for _ in range(math.floor(REPS / 2)):
            check_mark += "✔"
        check_label.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=2, row=1)

check_label = Label(background=YELLOW, foreground=GREEN)
check_label.grid(column=2, row=4)

start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()
