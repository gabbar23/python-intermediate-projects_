from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 30
reps=0
timer_main=None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer_main)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*10
    short_break=SHORT_BREAK_MIN*5
    long_break=LONG_BREAK_MIN*1

    if reps%8==0:
        countdown(long_break)
        timer.config(text="LONG BREAK",fg =PINK,font=(FONT_NAME,40,"bold"))


    elif reps%2==0:
        countdown(short_break)
        timer.config(text="BREAK",fg =RED,font=(FONT_NAME,40,"bold"))

    elif reps>8:
        reps=0

    else:
        countdown(work_sec)
        timer.config(text="WORK",fg =GREEN,font=(FONT_NAME,40,"bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec<10:
        count_sec = f"0{count_sec}"

    if count_sec==0:
        count_sec="00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer_main
        timer_main=window.after(1000,countdown,count-1)

    else:
        count_timer()
        marks=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

#WINDOW
window=Tk()
window.title("Pomodoro")
window.minsize(400,400)
window.config(bg=YELLOW,padx=100,pady=100)

#IMAGE
canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,111,image=photo)
timer_text=canvas.create_text(100,135,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1, column=2)

#LABEL-TIMER
timer=Label(text="Timer",font=((FONT_NAME,40,"bold")))
timer.config(fg=GREEN,bg=YELLOW)

timer.grid(row=0, column=2)


#BUTTON-START
start=Button(text="Start",command=count_timer)
start.grid(row=2,column=0)


#BUTTON-RESET
start=Button(text="Reset",command=reset_timer)
start.grid(row=2,column=3)

#check MARK

check = Label(font=(10), fg=GREEN, bg=YELLOW)
check.config(bg=YELLOW)
check.grid(row=3, column=2)

window.mainloop()