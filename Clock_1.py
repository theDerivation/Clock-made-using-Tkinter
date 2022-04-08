from tkinter import *
import time 

yeet = Tk()
yeet.title("CLOCK")

yeet.geometry("400x100")
label= Label(yeet, text="", font=("Helvetica", 48), fg= "black", bg="#2ab599")
label.pack(pady=20)

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second =time.strftime("%S")
    label.config(text= hour + ":" + minute  + ":" + second + " PM")
    label.after(1000, clock)
    return hour,minute,second

hour, minute, second = clock() 





























yeet.mainloop()