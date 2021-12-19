import tkinter
from tkinter.constants import END
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    password_list = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    
    try:
        with open("data.json", "r") as file:
            data = json.load(file)        
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="FILE NOT FOUND", message="No data file found")
    else:
        search_website = website_input.get()
        if search_website not in data:
            tkinter.messagebox.showerror(title="Website not found", message=f"No details for the {search_website} exists.")
        else:
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            tkinter.messagebox.showinfo(title="Website details", message=f"Email: {email}\nPassword: {password}")

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        tkinter.messagebox.showwarning(title="Fields empty", message="OOPS! some fields are empty")
        return
    
    message = f"These are the details entered:\nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs it ok to save?"
    is_ok = tkinter.messagebox.askokcancel(title=website_input.get(), message=message)
    
    if not is_ok:
        return
    
    data = {
        website_input.get():{
            "email": email_input.get(),
            "password": password_input.get()
        }
    }
    
    try:
        with open("data.json", 'r') as file:
            file_data = json.load(file)
            file_data.update(data)
    except FileNotFoundError:    
        with open("data.json", "w") as file:    
            json.dump(data, file, indent=4)
    else:
        with open("data.json", "w") as file:
            json.dump(file_data, file, indent=4)     
        
    # clearing all text boxes
    website_input.delete(0, 'end')
    password_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = tkinter.Canvas(width=200, height=200)
tomato_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text= "Password:")
password_label.grid(column=0, row=3)


# inputs
website_input = tkinter.Entry(width=20)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = tkinter.Entry(width=40)
email_input.insert(0, "mohit@demo.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

# buttons
generate_password = tkinter.Button(text="Generate Password", command=generate)
generate_password.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

search_button = tkinter.Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()