import tkinter as tk

window = tk.Tk()


#mijn code 

container = tk.Label(
    
    window,
    text="hello tkinter",
    bg="lime",
    fg="grey",
)

container.pack(
    ipadx = 20,
    ipady= 10,

)
window.geometry("300x300")
window.config(
    bg = "black",
    
)



#mijn code  einde 



window.mainloop()