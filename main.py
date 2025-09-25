from tkinter import *
from random import *
from PIL import Image, ImageTk
import time
import sys
stop = 0
def exit():
    sys.exit()
def close():
    root.destroy()

def stoop():
    global stop
    stop = 1

def click():
    global stop
    if stop == 0:
        window = Tk()
        window.title("close me!")
        window.geometry(f"250x200+{randint(0, 1200)}+{randint(0, 700)}")
        window.resizable(False, False)
        window.config(background='black')
        text = Label(window, text="close me( ͡° ͜ʖ ͡°)╭∩╮", font=("Sans-comic", 17), fg = "#00C800", background='black')
        text.place(x=35, y= 80)
        
        
        window.after(500, click) 

root = Tk()
root.title("menu")
root.geometry(f"400x400+600+200")
root.resizable(False, False)
root.config(background='black')
label = Label(text="CLOSE WINDOWS", font=("Sans-comic", 25), fg = "#00C800", background='black')
label.place(x=50, y= 10)
button = Button(text='Start', font=("Sans-comic", 25), fg = "#00C800", background='black', command=click)
button.place(x=150, y= 100)
button_2 = Button(text='Stop', font=("Sans-comic", 25), fg = "#00C800", background='black', command=stoop)
button_2.place(x=150, y= 200)
button_3 = Button(text='Exit', font=("Sans-comic", 25), fg = "#00C800", background='black', command=exit)
button_3.place(x=155, y= 300)




root.mainloop()

