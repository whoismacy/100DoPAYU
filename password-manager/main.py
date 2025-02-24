import json

from tkinter import *
from tkinter import messagebox

import pyperclip

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_generated = list()

# ---------------------------- SEARCH FUNCTION----------------------------------- #
def find_password():
    user_entry = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Search ERROR", message="No data file found.\nTry Saving a password first.")
    else:
        if data.get(user_entry, 0) != 0:
            description = f"e-mail: {data[user_entry]["email"]}\npassword: {data[user_entry]["password"]}"
            messagebox.showinfo(title="Requested Data", message=description)
        else:
            messagebox.showinfo(title="Non-Existent Password", message=f"It appears {user_entry} is not among saved passwords.\nEnsure you have the right spelling.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    password_entry.delete(0, END)
    for i in range(0, 6):
        password_generated.append(random.choice(letters))
    for i in range(0, 3):
        password_generated.append(random.choice(numbers))
        password_generated.append(random.choice(symbols))

    random.shuffle(password_generated)
    gen_password = ''.join(password_generated)
    password_entry.insert(index=0, string=gen_password)
    pyperclip.copy(gen_password)
    password_generated.clear()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    passwd = password_entry.get()

    new_data = {
        web:{
            "email": email,
            "password": passwd,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(passwd) == 0:
        messagebox.showerror(title="Oops", message="Ensure there are no empty fields")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json",mode="w") as upd_file:
                json.dump(data, upd_file, indent=4)
        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#PhotoImage
padlock_image = PhotoImage(file="logo.png")

# Creating the Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1, row=0)

# Label
f_label = Label(text="Website:", font=("Courier", 15, "normal"))
s_label = Label(text="Email/Username:", font=("Courier", 15, "normal"))
t_label = Label(text="Password:", font=("Courier", 15, "normal"))

f_label.grid(column=0, row=1)
s_label.grid(column=0, row=2)
t_label.grid(column=0, row=3)

# Button 1
generate_password = Button(text="Generate Password", command=generate_passwd, width=14)
generate_password.grid(column=2, row=3, sticky="w")

# Button 2
add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Button 3
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="w")

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(index=0, string="blueberryriver@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w", columnspan=1)

window.mainloop()
