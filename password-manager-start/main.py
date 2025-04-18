from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    if len(website_info) <= 0 or len(email_info) <= 0 or len(password_info) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_okay = messagebox.askokcancel(title=website_info,message=f"These are the details entered: "
                                                          f"Email: {email_info} \nPassword: {password_info} \n"
                                                          f"Is it okay to save?")
        if is_okay:
            with open("data.txt", "a") as data:
                data.write(f"{website_info} | {email_info} | {password_info}\n")
            website_input.delete(0,END)
            password_input.delete(0, END)


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
website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"anudeepreddy332@gmail.com")
password_input = Entry(width=18)
password_input.grid(row=3,column=1)

#Buttons
generate_password = Button(text="Generate Password",command=gen_password)
generate_password.grid(row=3,column=2)
add_button = Button(text="Add",width=33,command=add)
add_button.grid(row=4,column=1,columnspan=2)













window.mainloop()