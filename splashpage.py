from tkinter import *
from tkinter import ttk
import time
from PIL import ImageTk, Image

# from loginpage import *

# def step():
        
    # my_pbar.start(50)
root = Tk()
root.title("Splash Page")

splsh = PhotoImage(file="C:/Users/USER/Desktop/Registration Form/pkc2.png")
img = Label(root, image= splsh, width=20,height=10)
img.place(x=0, y=0, relwidth=1, relheight=1)

my_pbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
my_pbar.pack(pady=20, padx=10)

    
lbl = Label(text="")
lbl.pack()

for y in range(21):
    lbl.config(text=my_pbar["value"])
    my_pbar['value'] += 5
    root.update_idletasks()
    time.sleep(0.5)
    if my_pbar["value"] == 100:
        root.destroy()
        import loginpage
        
        

# btn = Button(root, text="progress", command=step)
# btn.pack(pady=20)


root.mainloop()