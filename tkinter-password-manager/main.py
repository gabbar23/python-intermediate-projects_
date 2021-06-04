from tkinter import *
from tkinter import messagebox
from alphabets import letters, symbols, numbers
import random
import pyperclip
import json

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


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_lower = entry_website.get()
    website = website_lower.capitalize()
    try:
        with open('account-information.json', 'r') as file:
            data = json.load(file)
            search_dict = [value for (key, value) in data.items() if website == key]
            email = search_dict[0]["Email"]
            password = search_dict[0]["Password"]


    except IndexError:
        messagebox.showerror(message="No such account Found !")
    except FileNotFoundError:
        messagebox.showerror(message="No such account Found !")


    else:
        messagebox._show(title=website, message=f"Email : {email} \n Password : {password}")
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_lower = entry_website.get()
    website=website_lower.capitalize()
    password = entry_pass.get()
    email = entry_email.get()

    new_data = {website: {"Email": email,
                          "Password": password

                          }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="Please Fill out all fields")
        print(len(website), len(password))

    else:
        try:
            with open('account-information.json', 'r') as file:
                data = json.load(file)
                print(data)

        except FileNotFoundError:
            with open("account-information.json", "w") as file:
                json.dump(new_data, file, indent=4)

        except:
            with open("account-information.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open('account-information.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:

            entry_website.delete(0, END)
            entry_pass.delete(0, END)
            messagebox._show(title="Saved", message="Account Added!")


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
entry_website = Entry(width=30)
entry_website.focus()
entry_website.grid(row=2, column=1)

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

# button-Search
add = Button(text="Search", width=14, command=search_password)
add.grid(row=2, column=2, columnspan=2)

window.mainloop()
