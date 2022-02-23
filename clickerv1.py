import tkinter as tk

counter = 0
window = tk.Tk()





button_up = tk.Button(text= 'up')

counter_label = tk.Label(
    window,
    text= counter
)

button_down = tk.Button(text= 'down')

def up_button():
    global counter, counter_label,window
    counter = counter + 1
    counter_label.config(text= counter)
    
    

def down_button():
    global counter, counter_label,window
    counter = counter - 1
    counter_label.config(text= counter)
    


    window.config(bg="grey",)
   
def color(counter):
    if counter < 0:
        window.update()
        counter_label.config(bg="red")
        

    elif counter > 0:
        
        counter_label.config(bg='green')
        window.update()

window.config(

 bg = color(counter)   
)

button_up.config(command= up_button)
button_down.config(command= down_button)




button_up.pack(
    ipady=25,
    ipadx=100,
    
)

counter_label.pack(ipady=25,
    ipadx=100,)

button_down.pack(ipady=25,
    ipadx=100,)


window.mainloop()