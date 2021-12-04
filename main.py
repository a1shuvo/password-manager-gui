from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "shuvo@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
