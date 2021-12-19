import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()

window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
tomato_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.pack()






window.mainloop()