from tkinter import *
from tkinter import messagebox
from math import *
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    alpha_list = list(string.ascii_letters) + list(string.digits) + list(string.punctuation) #remember that you can do choice(list_here) to pick something random .
    password = ""
    for each in range(0,20):
        password += alpha_list[random.randint(0, len(alpha_list) - 1)]
    print(f"password is {password}")
    pyperclip.copy(password)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_profile():
    web = website_entry.get()
    name = username_entry.get()
    password = password_entry.get()
    if (len(web) > 0) & (len(name) > 0) & (len(password) > 0):
        ok_or_not = messagebox.askokcancel(title=website_entry, message=f"There are the details entered: \nEmail:  {name}\nPassword:  {password}Is it ok to save?")
        if ok_or_not:
            with open(file="data.txt", mode="a") as data:
                data.writelines(f"{web} | {name} | {password} \n")
            notification_label.config(text="password copied to clipboard")
            clear_curr_profile()
            messagebox.showinfo(title="added", message=f"Info has been saved!")
    elif (len(web) == 0) or (len(name) == 0) or (len(password) == 0):
        messagebox.showinfo(title="Error", message="Fill in all fields!")
        notification_label.config(text="fill in all fields")


def clear_curr_profile():
    website_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady=30)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=2, row=1, columnspan=2, sticky=W)

#FIXME LABELS
Website_Label = Label(text="Website: ")
Website_Label.grid(column=1, row=2)
Username_Label = Label(text="Email/Username: ")
Username_Label.grid(column=1, row=3)
Pass_Label = Label(text="Password:")
Pass_Label.grid(column=1, row=4)
notification_label = Label(text="Press \'Add\' when ready")
notification_label.grid(column=2, row=6)

#FIXME ENTRYS
website_entry = Entry(width=50)
website_entry.grid(column=2, row=2, columnspan=2, sticky=W)
username_entry = Entry(width=50)
username_entry.grid(column=2, row=3, columnspan=2, sticky=W)
password_entry = Entry(width=31)
password_entry.grid(column=2, row=4,)

website_entry.focus()
# username_entry.insert(0, "enochskwong@gmail.com") #inserts a default value at start
username_entry.insert(END, "@gmail.com") #goes to the end by itself.

#FIXME BUTTONS
password_button = Button(text="Generate Password", command=password_generator, width=15)
password_button.grid(column=3, row=4, sticky=W,)
delete_button = Button(text="Clear", width=15, command=clear_curr_profile)
delete_button.grid(column=3, row=5, sticky=W)
add_button = Button(text="Add", width=26, command=save_profile)
add_button.grid(column=2, row=5, columnspan=2, sticky=W)


































window.mainloop()


#creates a files like this

# Amazon | enochskwong@gmail.com | enochpass

#after the enter button. use the entry delete button, delete(0, END)
