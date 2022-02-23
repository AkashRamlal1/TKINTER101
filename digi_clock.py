
import tkinter as tk
import time
import sys


window = tk.Tk()
window.title('digital clock made by akash')


#mijn code 

lbl = tk.Label(window, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'black')
print(type(lbl))

def tijd():
    current_time = tk.StringVar()
    current_time = time.strftime("%H : %M : %S")
    lbl.config(text = current_time)
    lbl.after(1000, tijd)



lbl.pack()
tijd()


 

#mijn code  einde 



window.mainloop()