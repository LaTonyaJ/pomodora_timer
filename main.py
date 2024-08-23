from tkinter import *
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
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    w.after_cancel(time)
    canvas.itemconfig(timer_text, text=f'00:00')
    checks.config(text="")
    timer.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
work_in_sec = WORK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
#25,5,25,5,25,5,25,20

def start_timer():
    global reps
    reps += 1
    print("reps", reps)

    if reps % 2 > 0:
        #work
        count_down(work_in_sec)
        timer.config(text="Work", fg=GREEN)
        print('work')
    elif reps % 2 == 0 and reps != 8:
        #short_break
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
        print('short_break')
    elif reps == 8:        
        #long_break
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
        print('long_break')
    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if int(count_sec) < 10 and int(count_sec) > 0:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if reps <= 8:
        if count > 0:
            global time
            time = w.after(1000, count_down, count - 1)
        else:
            start_timer()
            if reps > 1 and reps % 2 > 0:
                checks["text"] += "✔️"


# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Pomodoro Timer")
# w.minsize(width=500,height=350)
w.config(padx=100,pady=50, bg=YELLOW)

img = PhotoImage(file="tomato.png")
canvas = Canvas(w, height=230,width=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(110,114, image=img)
timer_text = canvas.create_text(105,130,text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)

#Label
timer = Label(w, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(column=1,row=0)

checks = Label(w,bg=YELLOW, fg=GREEN)
checks.grid(column=1,row=3)

#Buttons
start = Button(w, text="Start", activeforeground=GREEN, borderwidth=0, bg=YELLOW, command=start_timer)
start.grid(column=0,row=2)

reset = Button(w, text="Reset", highlightthickness=0, activeforeground=GREEN, bg=YELLOW, command=reset_timer)
reset.grid(column=2,row=2)

w.mainloop()