from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# Module to make possible copy something to Clipboard
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password_generated = "".join(password_list)
    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops")
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():

    site = website_entry.get().capitalize()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            # if site in data: - Angela propose to do in this way
            email = data[site]['email']
            password = data[site]['Password']
            messagebox.showinfo(title=site, message=f"E-mail: {email}\nPassword: {password}")
    except KeyError:
        messagebox.showinfo(title=site, message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title=site, message="No Data File found!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="E-mail/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky='EW')
website_entry.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky='EW')

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
email_entry.insert(0, 'alextret@gmail.com')

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky='EW')

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
