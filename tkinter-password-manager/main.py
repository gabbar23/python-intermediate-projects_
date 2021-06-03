from tkinter import *
from tkinter import messagebox
from alphabets import letters, symbols, numbers
import random
import pyperclip

WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Aerial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    entry_pass.delete(0, END)
    password = []
    for n in range(0, 7):
        password += random.choice(letters)
    for n in range(0, 3):
        password += random.choice(symbols)
    for n in range(0, 4):
        password += random.choice(numbers)

    random.shuffle(password)

    final = ''
    for n in password:
        final += n

    entry_pass.insert(END, final)
    pyperclip.copy(final)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=entry_website.get()
    password=entry_pass.get()

    if len(website)==0 or len(password) == 0:
        messagebox.showerror(message="Please Fill out all fields")
        print(len(website) , len(password))
    else:
        is_ok=messagebox.askokcancel(title="Confirm",
                               message=f"Please Confirm the Information \n Website : {entry_website.get()} \n Email : {entry_email.get()} \n Password : {entry_pass.get()} ")

        if is_ok:
            with open('account-information.txt', 'a') as file:
                file.write(f"{entry_website.get()} | {entry_email.get()} | {entry_pass.get()} \n")
            entry_website.delete(0, END)
            entry_pass.delete(0, END)
            messagebox._show(title="Saved",message="Account Added!")


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=WHITE)

# Image
canvas = Canvas(width=200, height=189, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=logo)
canvas.grid(row=1, column=1)

#                            # Label-Title
# title_label=Label(text="PASSWORD MANAGER",font=(FONT_NAME,25,"bold"),fg=RED,bg=WHITE)
# title_label.grid(row=0,column=1)

# label-website
web_label = Label(text="Website", font=(FONT_NAME, 12, "bold"), fg="black", bg=WHITE)
web_label.grid(row=2, column=0)

# label-Email/username
web_label = Label(text="Email/Username", font=(FONT_NAME, 12, "bold"), fg="black", bg=WHITE)
web_label.grid(row=3, column=0)

# label-Password
web_label = Label(text="Password", font=(FONT_NAME, 12, "bold"), fg="black", bg=WHITE)
web_label.grid(row=4, column=0)

# entry-website
entry_website = Entry(width=50)
entry_website.focus()
entry_website.grid(row=2, column=1, columnspan=2)

# entry-Email
entry_email = Entry(width=50)
entry_email.insert(END, "amansaini842@gmail.com")
entry_email.grid(row=3, column=1, columnspan=2)

# entry-password
entry_pass = Entry(width=30)
entry_pass.grid(row=4, column=1)

# button-Password
button = Button(text="Generate Password", command=password_gen)
button.grid(row=4, column=2)

# button-ADD
add = Button(text="ADD", width=45, command=save_password)
add.grid(row=5, column=1, columnspan=2)

window.mainloop()
