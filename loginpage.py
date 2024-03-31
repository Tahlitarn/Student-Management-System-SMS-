from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")
b_top = customtkinter.CTk()
b_top.title("LOGIN")

# b_top.config(background="grey")
app_width = 320
app_height = 300
screen_width = b_top.winfo_screenwidth()
screen_height = b_top.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
b_top.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# b_top.attributes('-alpha', 0.5)
# wm_attributes('-transparentcolor', 'gray')
# frame = Frame(b_top,width=50, border=10, borderwidth=10)
# frame.pack(pady=10)

# xg = ImageTk.PhotoImage(file="C:/Users/USER/Desktop/Registration Form/pkc2.png")



# adding TITLE to the top of the screen
fram= LabelFrame(b_top, text="ADMIN LOGIN", font=("Arial black", 10))
fram.pack(pady=20)

lblText= customtkinter.CTkLabel(fram, text="ADMIN LOGIN", font=("Arial black",13),corner_radius=30,fg_color='blue', bg_color="yellow")
lblText.grid(row=0, column=0, columnspan=2, pady= 30)

# adding labels and text field to the form

lblUserName = customtkinter.CTkLabel(fram, text="USER NAME",font=("Arial black", 10), fg_color='blue', bg_color="yellow", corner_radius=8 )
lblUserName.grid(row=1, column=0, padx=2,pady=2)
txtUserName = customtkinter.CTkEntry(fram,font=("Arial black", 10), width= 170,corner_radius=10,fg_color='blue',bg_color="yellow")
txtUserName.focus_set()
txtUserName.grid(row=1, column=1, padx=2,pady=2)


lblPassword = customtkinter.CTkLabel(fram, text="PASSWORD",font=("Arial black", 10), fg_color='blue',bg_color="yellow", corner_radius=8 )
lblPassword.grid(row=2, column=0, padx=2,pady=2)

txtPassword = customtkinter.CTkEntry(fram,font=("Arial black", 10),show="*", width= 170,corner_radius=10,fg_color='blue', bg_color="yellow")
txtPassword.grid(row =2, column=1, padx=2, pady=2)

# creating command buttons
Uname= "ADMIN"
Pword= "admin12345"

def login():
    if txtUserName.get().upper() == "ADMIN" and txtPassword.get().lower()== "admin12345":
        print ("valid user")
        b_top.destroy()
        # import mainpage
        
    elif txtUserName.get() != Uname or txtPassword != Pword:
        print('invalid user')
        txtUserName.delete(0,END)
        txtPassword.delete(0,END)
        txtUserName.focus_set()

btnLogin= customtkinter.CTkButton(fram, text="LOGIN",width=90, height=30, font=("Arial black", 12),fg_color='blue',bg_color="gray", hover_color="green", corner_radius=10, command=login)
btnLogin.grid(row = 3, column=0, padx=5,pady=5)

# txtUserName.bind("<btnLogin>",login)
# txtPassword.bind("<btnLogin>",login)
# btnLogin.grid(row=3, column=0, pady=5)

btnExit= customtkinter.CTkButton(fram, text="EXIT",width=90, height=30, font=("Arial black", 12),fg_color='blue',bg_color="gray", hover_color="red", corner_radius= 10, command=quit)
btnExit.grid(row=3, column=1)

b_top.mainloop()