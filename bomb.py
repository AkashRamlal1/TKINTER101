import tkinter as tk
import time
from tkinter.tix import Tree 

color = ['black','red','blue','green','purple','yellow','black']

window = tk.Tk()

x = 100
y = 100
window.geometry("{}x{}".format(x , y))
counter = 12
color_num = 0
for i in range (6):
    
    
    window.update()
    x = x + 100
    y = y  + 100 
    color_num = color_num + 1
    window.after(1000, window.geometry("{}x{}".format(x , y)))
    
    counter = counter - 2
    window.config( bg= color[color_num])
    print(counter)
    print(i)

    
print('BOOM')
window.destroy()
window.mainloop()
