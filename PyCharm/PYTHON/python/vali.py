from tkinter import *

window = Tk()

window.title("sadhik")
window.geometry('600x400')
window.config(bg="#333")

# fix at side
window.attributes("-topmost", 1)

# widget
label = Label(window, text="Python")
label.pack()

# text box
t1 = Entry(window)
t1.pack()

btn = Button(window, text="Click")
btn.pack()


def message():
    lb2 = Label(window, text="Hello")
    lb2.pack()


btn2 = Button(window, text="Click Me", command=message)
btn2.pack()

window.mainloop()