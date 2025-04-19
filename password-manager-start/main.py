from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#Constants
FONT = ("Courier",18,"normal")

#Password Generator
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


#Add info
def add():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }
    if len(website_info) <= 0 or len(email_info) <= 0 or len(password_info) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data:
                #Reading old data
                d_data = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data,data,indent=4)

        else:
            d_data.update(new_data)

            with open("data.json", "w") as data:
                json.dump(d_data,data,indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

#find password
def find_password():
    website_info = website_input.get()
    try:
        with open("data.json") as data:
            d_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
        if website_info in d_data:
            email =d_data[website_info]["email"]
            password = d_data[website_info]["password"]
            messagebox.showinfo(title=website_info,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website_info} exists.")


#UI setup
window = Tk()
window.config(pady=50,padx=50)
window.title("Password Manager")
photo = PhotoImage(file="logo.png")

canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2,column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3,column=0)

#Inputs
website_input = Entry(width=21)
website_input.grid(row=1,column=1)
website_input.focus()
email_input = Entry(width=38)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"anudeepreddy332@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3,column=1)

#Buttons
generate_password = Button(text="Generate Password",command=gen_password)
generate_password.grid(row=3,column=2)
add_button = Button(text="Add",width=33,command=add)
add_button.grid(row=4,column=1,columnspan=2)
search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)












window.mainloop()