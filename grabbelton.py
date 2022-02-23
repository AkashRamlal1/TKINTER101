from argparse import RawDescriptionHelpFormatter
from cgitb import text
import tkinter as tk
import random
from tkinter.messagebox import showerror, showwarning, showinfo
from turtle import bgcolor, title

window = tk.Tk()




#hier maak ik een button aan
knop = tk.Button()

prijzen  = ['speelgoed auto','rode stuiterbal','sleutelhanger','snoepje','stress ball', 'puzzel','speciale prijs','fluitje','stickers','potloden']
gewonnen = []   
# mijn prijzen

def grabbel():
    
    print('het werkt')
    global prijzen,gewonnen, container
    
    
    gepakt = random.choice(prijzen)
   
    
    
    container.update(bg = 'red')
    
    window.update()


container = tk.Label(
    
    window,

    text = prijzen
)





knop.config( text='grabbel', command= grabbel)  
container.pack(ipadx = 20,
    ipady= 10,)
knop.pack(ipadx= 20, ipady= 20) #bepaald grootte knop

#maak funcite 


print(prijzen)




window.mainloop()