import tkinter
from tkinter.constants import LEFT

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_input = tkinter.Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)

email_input = tkinter.Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

# buttons
generate_password = tkinter.Button(text="Generate Password")
generate_password.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=38)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

window.mainloop()