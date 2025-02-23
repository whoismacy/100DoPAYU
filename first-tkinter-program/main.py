from tkinter import *

window = Tk()
window.title("My first GUI program.")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20) # Adding padding to the program.

# Button event listener
def button_clicked():
    print("I got clicked")
    my_label.config(text=get_input.get())

def button_touched():
    print("I got touched.")

# Creating a Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Creating another Button
button1 = Button(text="Touch Me", command=button_touched)
button1.grid(column=2, row=0)

# Creating a label
my_label = Label(text="I am a label.", font=("Courier", 24, "italic"))
my_label.grid(column=0, row=0)

# An Entry Component
get_input = Entry(width=30)
get_input.grid(column=3, row=2)

# Keeps the window open for the user, should be at the bottom of the code.
window.mainloop()
