from tkinter import *

# TODO 0 Define a Window
# TODO 1 Create four labels
# TODO 2 Create one button
# TODO 3 Create one Entry point
# TODO 4 Use grid positioning system

FONT = ("Courier", 25, "normal")

# 0
window = Tk()
window.title("Miles to KM Converter")
window.minsize(height=600, width=600)
window.config(padx=100, pady=100)

# 1.1
label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)

# 1.2
label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)

# 1.3
label3 = Label(text="Km", font=FONT)
label3.grid(column=2, row=1)

# 1.4
label4 = Label(text="", font=FONT)
label4.grid(column=1, row=1)

# 3
user_data = Entry(width=25, font=FONT)
user_data.grid(column=1, row=0)

# 2
# 2.button function
def on_click():
    calculation = int(user_data.get()) * 1.60934
    label4.config(text=str(calculation))

# 2.create a button
button = Button(text="Calculate", command=on_click)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

# Keep the Window open
window.mainloop()

