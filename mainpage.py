from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import sqlite3
import loginpage


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")
me = customtkinter.CTk()
me.title('MainPage')
app_width = 600
app_height = 630
screen_width = me.winfo_screenwidth()
screen_height = me.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
me.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# me.resizable(width=False, height=False)
# img=xg = PhotoImage(file="C:/Users/USER/Desktop/Registration Form/pkc2.png")
# imgs = Label(me, image=img, width=200,height=100)
# imgs.place(x=0, y=0, relwidth=1, relheight=1)

# __________________________________________creating database connection_____________________________________________________________________________

conn = sqlite3.connect('student management system.db')

# __________________________________________Menu configuration___________________________________________
my_menu = Menu(me,title='HOMEPAGE' )
me.config(menu=my_menu)

#creating def
def new_menu():
    hide_frame()
    new_menu_frame.pack(fill="both", expand=1)
    

# creating def to load frames into menus
def reg_frame():
    hide_frame()
    edit_register_frame.pack()

def edit():
    hide_frame()
    edit_edit_frame.pack()
    
def delete_frame():
    hide_frame()
    edit_delete_frame.pack(fill='both', expand=1)

def view_frame():
    hide_frame()
    result_view_frame.pack(fill='both', expand=1)

def upload_frame():
    hide_frame()
    result_upload_frame.pack(fill='both', expand=1)
    
def view_all_frame():
    hide_frame()
    result_view_all_frame.pack(fill='both', expand=1)

def course_reg():
    hide_frame()
    course_reg_frame.pack()

def course_edit():
    hide_frame()
    course_edit_frame.pack()

def search():
    pass
# hiding frames....
def hide_frame():
    edit_register_frame.pack_forget()
    edit_edit_frame.pack_forget()
    edit_delete_frame.pack_forget()
    result_view_all_frame.pack_forget()
    result_upload_frame.pack_forget()
    result_view_frame.pack_forget()
    new_menu_frame.pack_forget()
    course_reg_frame.pack_forget()
    course_edit_frame.pack_forget()
# creating a menu item.........................
#creating file menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="FILE", menu=file_menu)

# creating menu command inside file menu
file_menu.add_command(label='New', command=new_menu)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=me.quit)

# creating a edit menu
student_info_menu = Menu(my_menu)
# creating menu command inside edit menu
my_menu.add_cascade(label='STUDENT INFO.', menu=student_info_menu)
student_info_menu.add_command(label='Register', command=reg_frame)
student_info_menu.add_separator()
student_info_menu.add_command(label='Edit', command=edit)
student_info_menu.add_separator()
student_info_menu.add_command(label='Delete', command=delete_frame)

# creating subject registration menu
subject_reg_menu = Menu(my_menu)
my_menu.add_cascade(label="SUBJECT REGISTRATION", menu=subject_reg_menu)
# creating command
subject_reg_menu.add_command(label="Register", command=course_reg)
subject_reg_menu.add_separator()
subject_reg_menu.add_command(label="Edit", command=course_edit)

# creating menu for result

result_menu = Menu(my_menu)

# creating menu command inside result menu
my_menu.add_cascade(label='RESULT', menu=result_menu)
result_menu.add_command(label='Upload', command=upload_frame)
result_menu.add_separator()
result_menu.add_command(label='View', command=view_frame)
result_menu.add_separator()
result_menu.add_command(label='View All', command=view_all_frame)

# creating frames for new menu
new_menu_frame = Frame(me, bg="gray", highlightthickness=2)

# creating frames for student info menu.....
edit_register_frame = Frame(me, highlightthickness=2)
edit_edit_frame = Frame(me, width=200, height=20)
edit_delete_frame = Frame(me, width=200, height=50, bg="gray")

#creating frame inside course
course_reg_frame = Frame(me, width=200, height=50, bg="white", highlightthickness=2)
course_edit_frame = Frame(me, width=200, height=50, bg="white", highlightthickness=2)
# creating frames for result menu
result_upload_frame = Frame(me, width=200, height=80, bg="gray")
result_view_frame = Frame(me, width=200, height=80, bg="gray")
result_view_all_frame = Frame(me, width=200, height=80, bg="cyan")

#________________________creating objects inside the new frame_____________________________________________

def student():
    tbl_new_sub_frame.grid_forget()
    tbl_new_stud_frame.grid(row=2, column=0, columnspan=2)


def subject():
    tbl_new_stud_frame.grid_forget()
    tbl_new_sub_frame.grid(row=2, column=0, columnspan=2)

def sub_table():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #_______________SUBJECT REGISTRATION TABLE______________
    c.execute("""CREATE TABLE if not exists subjects(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text
        
        )""")
    
    #_____________________________________first term________________________________________________
    c.execute("""CREATE TABLE if not exists jss1_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    #__________________________________second term_______________________________________________________
    
    c.execute("""CREATE TABLE if not exists jss1_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    #_____________________________________third term_____________________________________________________
    
    c.execute("""CREATE TABLE if not exists jss1_third_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    #________________________________first term_________________________________
    c.execute("""CREATE TABLE if not exists jss2_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    #__________________________________second term___________________________________
    
    c.execute("""CREATE TABLE if not exists jss2_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    #_____________________________________third term________________________________________________
    c.execute("""CREATE TABLE if not exists jss2_third_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    #________________________________first term_________________________________
    c.execute("""CREATE TABLE if not exists jss3_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    #__________________________________second term___________________________________
    
    c.execute("""CREATE TABLE if not exists jss3_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
#      # commit connection
#     conn.commit()
#     print("Table created Successfully...")
#     conn.close()
#     messagebox.showinfo("table", "Table Created Successfully")


# def ssub_table():
#     conn = sqlite3.connect('student management system.db')

#     c = conn.cursor()
    
    
#_______________________________________________________________________________1ST  TERM TABLE for senior school______________________________________________________________________________________________
 
    c.execute("""CREATE TABLE if not exists ss1_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        
        )""")
    
    c.execute("""CREATE TABLE if not exists ss2_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    
    c.execute("""CREATE TABLE if not exists ss3_first_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        
        )""")
#_______________________________________________________________________________2ND  TERM TABLE for senior school______________________________________________________________________________________________

    c.execute("""CREATE TABLE if not exists ss1_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    c.execute("""CREATE TABLE if not exists ss2_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    c.execute("""CREATE TABLE if not exists ss3_second_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")



#_______________________________________________________________________________3RD  TERM TABLE for senior school______________________________________________________________________________________________
    
    c.execute("""CREATE TABLE if not exists ss1_third_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    c.execute("""CREATE TABLE if not exists ss2_third_term(
        full_name text,
        class_level text,
        class text,
        gender text,
        age integer,
        student_id text,
        subject1 text,
        subject2 text,
        subject3 text,
        subject4 text,
        subject5 text,
        subject6 text,
        subject7 text,
        subject8 text,
        subject9 text,
        subject10 text,
        subject11 text,
        subject12 text,
        subject13 text,
        subject14 text,
        subject15 text,
        subject16 text,
        subject17 text,
        subject18 text,
        subject19 text,
        subject20 text,
        test integer,
        exam integer,
        total integer,
        grade text,
        point integer
        )""")
    
    # commit connection
    conn.commit()
    print("Table created Successfully...")
    conn.close()
    messagebox.showinfo("table", "Table Created Successfully")

def s_name():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    c.execute("""CREATE TABLE student_registers(
        first_name text,
        last_name text,
        other_name text,
        date_of_birth integer,
        state_of_origin text,
        student_gender text,
        student_age interger,
        student_religion text,
        student_nationality text,
        date_of_admission integer,
        student_level text,
        student_class text
        )""")


    # commit connection
    conn.commit()
    conn.close()
    messagebox.showinfo("table", "Table Created Successfully")



new_general_frame = LabelFrame(new_menu_frame,text="CREATE TABLE",labelanchor="n", font=("arial black",10),fg="cyan",bg="gray",highlightthickness=2)
new_general_frame.pack(pady=2)

stud_tbl_btn = customtkinter.CTkButton(new_general_frame, text='STUDENT',width=90, height=30, font=("Arial black", 12),fg_color='cyan',bg_color="gray", hover_color="green", corner_radius=10, command=student)
stud_tbl_btn.grid(row=1, column=0, pady=5, padx=5)
subj_tbl_btn = customtkinter.CTkButton(new_general_frame, text='SUBJECT',width=90, height=30, font=("Arial black", 12),fg_color='cyan',bg_color="gray", hover_color="green", corner_radius=10, command=subject)
subj_tbl_btn.grid(row=1, column=1, pady=5, padx=5)

tbl_new_stud_frame= LabelFrame(new_general_frame,text="STUDENT TABLE", font=("Arial black", 7),labelanchor="n",fg="cyan",borderwidth=2)
tbl_new_stud_frame.grid_forget()
tbl_new_sub_frame= LabelFrame(new_general_frame,text="SUBJECT TABLE", font=("Arial black", 7), labelanchor="n",fg="cyan",borderwidth=2)
tbl_new_sub_frame.grid_forget()

btn_tbl_stud_name =customtkinter.CTkButton(tbl_new_stud_frame, text='CREATE TABLE',width=90, height=30, font=("Arial black", 12),fg_color='cyan',bg_color="gray", hover_color="green", corner_radius=10, command=s_name)
btn_tbl_stud_name.grid(row=0, column=0)

# subj_tbl_btn = customtkinter.CTkButton(tbl_new_sub_frame, text='JUNIOR SUBJECTS',width=90, height=30, font=("Arial black", 12),fg_color='cyan',bg_color="gray", hover_color="green", corner_radius=10, command=jsub_table)
# # subj_tbl_btn.grid(row=1, column=0, pady=5, padx=5)
subj_tbl_senior_btn = customtkinter.CTkButton(tbl_new_sub_frame, text='SUBJECTS',width=90, height=30, font=("Arial black", 12),fg_color='cyan',bg_color="gray", hover_color="green", corner_radius=10, command=sub_table)
subj_tbl_senior_btn.grid(row=1, column=1, pady=5, padx=5)

# creating objects inside edit register frame
#  creating frames to house the objects created
name_frame = Frame(edit_register_frame, bg="gray",highlightthickness=2)
name_frame.pack(pady=2)
other_frame = Frame(name_frame, bg="gray")
other_frame.grid(row=11, column=1)
preview_frame = Frame(edit_register_frame, bg="gray", borderwidth=5,highlightthickness=2)
preview_frame.pack(pady=3)
view_list = Listbox(edit_register_frame,width=70,background="gray",borderwidth=2,font=("arial black", 8), height=10)
view_list.pack()

confirm_frame = Frame(edit_register_frame, bg="gray", borderwidth=5,highlightthickness=2)
confirm_frame.pack(pady=5)


#_________________________________________main objects______________________________________________________________

lbl_Stud_reg = Label(name_frame, text="REGISTRATION PAGE", font=("arial black", 10),bg="gray", fg='cyan')
lbl_Stud_reg.grid(row=0, column=0, columnspan=2)
lbl_First_name = Label(name_frame, text="FIRST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_First_name.grid(row=1, column=0, pady=2)
lbl_last_name = Label(name_frame, text="LAST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_last_name.grid(row=2,column=0, pady=2)
lbl_other_name = Label(name_frame, text="OTHER NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_other_name.grid(row=3,column=0,pady=2)
lbl_date_of_birth = Label(name_frame, text="DATE OF BIRTH", font=("arial black", 10),bg='gray', fg='cyan')
lbl_date_of_birth.grid(row=4,column=0,pady=2)
lbl_state_of_origin = Label(name_frame, text="STATE OF ORIGIN", font=("arial black", 10),bg='gray', fg='cyan')
lbl_state_of_origin.grid(row=5,column=0,pady=2)
lbl_religion = Label(name_frame, text="RELIGION", font=("arial black", 10),bg='gray', fg='cyan')
lbl_religion.grid(row=8,column=0,pady=2)
lbl_nationality = Label(name_frame, text="NATIONALITY", font=("arial black", 10),bg='gray', fg='cyan')
lbl_nationality.grid(row=9,column=0,pady=2)
lbl_std_gender =Label(name_frame, text="GENDER", font=("arial black", 10),bg='gray', fg='cyan')
lbl_std_gender.grid(row=6,column=0,pady=2)
lbl_std_age =Label(name_frame, text="AGE", font=("arial black", 10),bg='gray', fg='cyan')
lbl_std_age.grid(row=7,column=0,pady=2)
lbl_date_reg =Label(name_frame, text="DATE OF REG", font=("arial black", 10),bg='gray', fg='cyan')
lbl_date_reg.grid(row=10,column=0,pady=2)
lbl_std_class = Label(name_frame, text="CLASS", font=("arial black", 10),bg='gray', fg='cyan')
lbl_std_class.grid(row=11,column=0,pady=2)

# creating text boxes inside edit menu frame
txt_first_name = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_first_name.focus_set()
txt_first_name.grid(row=1, column=1)
txt_last_name = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_last_name.grid(row=2, column=1)
txt_other_name = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_other_name.grid(row=3,column=1)
txt_d_o_b = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_d_o_b.grid(row=4,column=1)
txt_state_of_origin = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_state_of_origin.grid(row=5,column=1)
txt_religion = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_religion.grid(row=8,column=1)
txt_nationality = Entry(name_frame, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_nationality.grid(row=9,column=1)

# creating radiobutton inside edit menu frame
der = StringVar()
der.set("MALE")
my_frame = Frame(name_frame,bg='gray')
my_frame.grid(row=6,column=1)
# for text, mode in MODES:
Radiobutton(my_frame, text="MALE",font=("arial black", 10), variable=der, value="MALE").grid(row=0, column=0,padx=5)
Radiobutton(my_frame, text="FEMALE",font=("arial black", 10), variable=der, value="FEMALE").grid(row=0, column=1,padx=5)

# creating a list for combobox selection
school = [
    "Select School",
    "Junior School",
    "Senior School"
]
age = [
    "AGE",6,7,8,9,10,11,12,13,14,15,16,17,18,19
    
]
month = [
    "MONTH",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12"
]
year = [
    "YEAR",2009,2010,2011,2012,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,
    2026,2027,2028,2029,2030,2031,2032,2033,2034,2035
]
my_age = ttk.Combobox(name_frame,width=20, value= age)
my_age.current(0)
my_age.grid(row=7,column=1)

reg_date_frame= Frame(name_frame,bg='gray')
reg_date_frame.grid(row=10,column=1)
my_month = ttk.Combobox(reg_date_frame,width=20, value= month)
my_month.current(0)
my_month.grid(row=0,column=0, pady=5)

my_year = ttk.Combobox(reg_date_frame,width=20, value= year)
my_year.current(0)
my_year.grid(row=0,column=1, pady=5)

# creating list of class

Junior_school = [
    "JSS ONE",
    "JSS TWO",
    "JSS THREE"
]
Senior_School = [
    "SS ONE",
    "SS TWO",
    "SS THREE"
]

def pick_class(e):
    if my_school.get() == "Junior School":
        my_class.config(value=Junior_school)
        my_class.current(0)
        
    elif my_school.get() == "Senior School":
        my_class.config(value=Senior_School)
        my_class.current(0)
        
    else:
        my_class.delete(0, END)
        my_class.config(value= " ")


my_school = ttk.Combobox(other_frame, value= school)
my_school.current(0)
my_school.grid(row=6,column=0)
# binding it with another option button(combobox)
my_school.bind("<<ComboboxSelected>>",pick_class)

my_class = ttk.Combobox(other_frame, value= [" "])
my_class.grid(row=6,column=1)


# creating the command buttons
def prev():
    view_list.insert(1,f'{txt_first_name.get().upper()} {txt_last_name.get().upper()} {txt_other_name.get().upper()}')
    view_list.insert(2,f'{txt_d_o_b.get()}')
    view_list.insert(3,f'{txt_state_of_origin.get().upper()}')
    view_list.insert(4,f'{txt_nationality.get().upper()}')
    view_list.insert(5,f'{der.get().upper()}')
    view_list.insert(6,f'{my_age.get()}')
    view_list.insert(7,f'{txt_religion.get().upper()}')
    view_list.insert(8,f'REGISTRATION DATE: {my_month.get()} {my_year.get()}')
    view_list.insert(9,f'CLASS LEVEL: {my_school.get().upper()}, CLASS: {my_class.get().upper()}')

def reg():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #inserting to database
    
    c.execute("INSERT INTO student_registers VALUES(:f_name, :l_name, :o_name, :d_o_b, :s_o_o, :s_gender, :s_age, :s_religion, :s_nationality, :d_o_a, :s_level, :s_class)",
              
              {
                  'f_name': txt_first_name.get(),
                  'l_name': txt_last_name.get(),
                  'o_name': txt_other_name.get(),
                  'd_o_b': txt_d_o_b.get(),
                  's_o_o': txt_state_of_origin.get(),
                  's_gender': der.get(),
                  's_age': my_age.get(),
                  's_religion': txt_religion.get(),
                  's_nationality': txt_nationality.get(),
                  'd_o_a': my_month.get() +"/"+ my_year.get(),
                  's_level': my_school.get(),
                  's_class': my_class.get()
              })
    
    conn.commit()
    conn.close()
    
    txt_first_name.delete(0, END)
    txt_last_name.delete(0,END)
    txt_other_name.delete(0,END)
    txt_d_o_b.delete(0,END)
    txt_state_of_origin.delete(0,END)
    txt_religion.delete(0, END)
    txt_nationality.delete(0, END)
    
def clear():
    txt_first_name.delete(0,END)
    txt_last_name.delete(0,END)
    txt_other_name.delete(0,END)
    view_list.delete(0, END)
def close():
    txt_first_name.delete(0,END)
    txt_last_name.delete(0,END)
    txt_other_name.delete(0,END)
    hide_frame()
btn_preview = Button(preview_frame, text="PREVIEW",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command=prev)
btn_preview.grid(row=0, column=0, padx=2)

btn_clear = Button(preview_frame, text="CLEAR",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command= clear)
btn_clear.grid(row=0, column=1, padx=3)

btn_exit = Button(preview_frame, text="EXIT",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command= close)
btn_exit.grid(row=0, column=2, padx=3)

btn_register = Button(confirm_frame, text="REGISTER",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command=reg)
btn_register.grid(row=0, column=0, padx=3)


# ______________________________creating objects inside edit edit frame________________________________
lbl_Stud_reg = Label(edit_edit_frame, text="EDIT STUDENT INFO", font=("arial black", 12),bg="gray", fg='cyan')
lbl_Stud_reg.pack()

search_frame = Frame(edit_edit_frame, bg="gray")
search_frame.pack(pady=2)

def srch():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #select from database
    global txt_first_name_edit
    global txt_last_name_edit
    global txt_other_name_edit
    global txt_d_o_b_edit
    
    record_id = txt_search_edit.get()
    c.execute("SELECT * FROM student_registers WHERE oid =" + record_id)
    records = c.fetchall()
    print(records)
    txt_first_name_edit.delete(0,END)
    txt_last_name_edit.delete(0,END)
    txt_other_name_edit.delete(0,END)
    txt_d_o_b_edit.delete(0,END)
    
    # looping through the result
    for record in records:
        txt_first_name_edit.insert(0,record[0])
        txt_last_name_edit.insert(0,record[1])
        txt_other_name_edit.insert(0,record[2])
        txt_d_o_b_edit.insert(0,record[3])
        
    conn.commit()
    conn.close()


txt_search_edit = Entry(search_frame,width=20,font=("arial black", 10),bg="gray", fg="cyan",border=5,borderwidth=2)
txt_search_edit.focus_set()
txt_search_edit.grid(row=0,column=0, padx=10)
btn_search_edit = Button(search_frame,text="SEARCH",font=("arial black",6), width=5, bg="GREEN", fg="Black", borderwidth=5, command= srch)
btn_search_edit.grid(row=0, column=1, padx=10)

name_frame1 = Frame(edit_edit_frame, bg="gray",highlightthickness=2)
name_frame1.pack(pady=2)
confirm_frame1 = Frame(edit_edit_frame, bg="gray", borderwidth=5,highlightthickness=2)
confirm_frame1.pack(pady=5)

# _________________________________________main objects inside edit menu______________________________________________________________

lbl_First_name1 = Label(name_frame1, text="FIRST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_First_name1.grid(row=1, column=0, pady=2)
lbl_last_name1 = Label(name_frame1, text="LAST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_last_name1.grid(row=2,column=0, pady=2)
lbl_other_name1 = Label(name_frame1, text="OTHER NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_other_name1.grid(row=3,column=0,pady=2)
lbl_date_of_birth1 = Label(name_frame1, text="D.O.B", font=("arial black", 10),bg='gray', fg='cyan')
lbl_date_of_birth1.grid(row=4,column=0,pady=2)

# creating text boxes inside edit menu frame
txt_first_name_edit = Entry(name_frame1, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_first_name_edit.grid(row=1, column=1)
txt_last_name_edit = Entry(name_frame1, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_last_name_edit.grid(row=2, column=1)
txt_other_name_edit = Entry(name_frame1, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_other_name_edit.grid(row=3,column=1)
txt_d_o_b_edit = Entry(name_frame1, width=31, border=5, borderwidth= 2, font=("arial black", 10),bg='gray', fg='cyan')
txt_d_o_b_edit.grid(row=4,column=1)


# creating the command buttons
def upd():
    record_id = txt_search_edit.get()
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #inserting to database
    
    c.execute("""UPDATE student_registers SET
              first_name = :first,
              last_name = :last,
              other_name = :other,
              date_of_birth = :d_o_b
              
              WHERE oid = :oid""",
              
              {
                  'first': txt_first_name_edit.get(),
                  'last': txt_last_name_edit.get(),
                  'other': txt_other_name_edit.get(),
                  'd_o_b': txt_d_o_b_edit.get(),
                  
                  'oid' : record_id
              }
              )
    
    conn.commit()
    conn.close()
    txt_search_edit.delete(0,END)
    txt_first_name_edit.delete(0,END)
    txt_last_name_edit.delete(0,END)
    txt_other_name_edit.delete(0,END)
    txt_d_o_b_edit.delete(0,END)
    txt_search_edit.focus_set()


def close():
    txt_first_name_edit.delete(0,END)
    txt_last_name_edit.delete(0,END)
    txt_other_name_edit.delete(0,END)
    txt_d_o_b_edit.delete(0,END)

    hide_frame()

btn_update = Button(confirm_frame1, text="UPDATE",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command=upd)
btn_update.grid(row=0, column=1, padx=2)

btn_exit_edit = Button(confirm_frame1, text="EXIT",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command= close)
btn_exit_edit.grid(row=0, column=2, padx=2)


# ______________________________DELETING STUDENT INFO_____________________________________________________

lbl_Stud_reg_del = Label(edit_delete_frame, text="DELETE STUDENT INFO", font=("arial black", 12),bg="gray", fg='cyan')
lbl_Stud_reg_del.pack()

search_frame2 = Frame(edit_delete_frame, bg="gray")
search_frame2.pack(pady=2)


def s_id_del():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #inserting to database
    
    record_id = txt_search_del.get()
    c.execute("SELECT * FROM student_registers WHERE oid = " + record_id)
    records = c.fetchall()
    print(records)
    # looping through the result
    for record in records:
        global First_name_del
        global last_name_del
        global other_name_del
        global date_of_birth_del
        global gender_del
        global age_del
        global mnth_year_admission_del
        global school_del
        global class_del
        global religion_del
        global nationality_del
        global state_of_origin_del
        
        First_name_del = Label(name_frame2, text=record[0],width=20, border=5,borderwidth=5, highlightthickness=2 ,font=("arial black", 10),bg='gray', fg='cyan')
        First_name_del.grid(row=1, column=1, pady=2)
        last_name_del = Label(name_frame2, text=record[1],width=20, border=5,borderwidth=5, highlightthickness=2 ,font=("arial black", 10),bg='gray', fg='cyan')
        last_name_del.grid(row=2,column=1, pady=2)
        other_name_del = Label(name_frame2, text=record[2],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        other_name_del.grid(row=3,column=1,pady=2)
        date_of_birth_del = Label(name_frame2, text=record[3],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        date_of_birth_del.grid(row=4,column=1,pady=2)
        gender_del = Label(name_frame2, text=record[5],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        gender_del.grid(row=5,column=1,pady=2)
        age_del = Label(name_frame2, text=record[6],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        age_del.grid(row=6,column=1,pady=2)
        mnth_year_admission_del = Label(name_frame2, text=record[9],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        mnth_year_admission_del.grid(row=7,column=1,pady=2)
        school_del = Label(name_frame2, text=record[10],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        school_del.grid(row=8,column=1,pady=2)
        class_del = Label(name_frame2, text=record[11],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        class_del.grid(row=9,column=1,pady=2)
        religion_del = Label(name_frame2, text=record[7],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        religion_del.grid(row=10,column=1,pady=2)
        nationality_del = Label(name_frame2, text=record[8],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        nationality_del.grid(row=11,column=1,pady=2)
        state_of_origin_del = Label(name_frame2, text=record[4],width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
        state_of_origin_del.grid(row=12,column=1,pady=2)

        
    conn.commit()
    conn.close()

txt_search_del = Entry(search_frame2,width=20,font=("arial black", 10),bg="gray", fg="cyan",border=5,borderwidth=2)
txt_search_del.focus_set()
txt_search_del.grid(row=0,column=0)
btn_search_del = Button(search_frame2,text="SEARCH",font=("arial black",6), width=5, bg="GREEN", fg="Black", borderwidth=5, command= s_id_del)
btn_search_del.grid(row=0, column=1)

name_frame2 = Frame(edit_delete_frame, bg="gray",highlightthickness=2)
name_frame2.pack(pady=2)
other_frame2 = Frame(edit_delete_frame, bg="gray",highlightthickness=2)
other_frame2.pack()
confirm_frame2 = Frame(edit_delete_frame, bg="gray", borderwidth=5,highlightthickness=2)
confirm_frame2.pack(pady=5)

# _________________________________________main objects inside delete menu______________________________________________________________

lbl_First_name1 = Label(name_frame2, text="FIRST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_First_name1.grid(row=1, column=0, pady=2)
lbl_last_name1 = Label(name_frame2, text="LAST NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_last_name1.grid(row=2,column=0, pady=2)
lbl_other_name1 = Label(name_frame2, text="OTHER NAME", font=("arial black", 10),bg='gray', fg='cyan')
lbl_other_name1.grid(row=3,column=0,pady=2)
lbl_date_of_birth1 = Label(name_frame2, text="D.O.B", font=("arial black", 10),bg='gray', fg='cyan')
lbl_date_of_birth1.grid(row=4,column=0,pady=2)
lbl_gender1 = Label(name_frame2, text="GENDER", font=("arial black", 10),bg='gray', fg='cyan')
lbl_gender1.grid(row=5,column=0,pady=2)
lbl_age1 = Label(name_frame2, text="AGE", font=("arial black", 10),bg='gray', fg='cyan')
lbl_age1.grid(row=6,column=0,pady=2)
lbl_mnth_year_admission = Label(name_frame2, text="TIME OF ADMISSION", font=("arial black", 10),bg='gray', fg='cyan')
lbl_mnth_year_admission.grid(row=7,column=0,pady=2)
lbl_school1 = Label(name_frame2, text="SCHOOL", font=("arial black", 10),bg='gray', fg='cyan')
lbl_school1.grid(row=8,column=0,pady=2)
lbl_class1 = Label(name_frame2, text="CLASS", font=("arial black", 10),bg='gray', fg='cyan')
lbl_class1.grid(row=9,column=0,pady=2)
lbl_religion1 = Label(name_frame2, text="RELIGION", font=("arial black", 10),bg='gray', fg='cyan')
lbl_religion1.grid(row=10,column=0,pady=2)
lbl_nationality1 = Label(name_frame2, text="NATIONALITY", font=("arial black", 10),bg='gray', fg='cyan')
lbl_nationality1.grid(row=11,column=0,pady=2)
lbl_state_of_origin1 = Label(name_frame2, text="SUBJECT", font=("arial black", 10),bg='gray', fg='cyan')
lbl_state_of_origin1.grid(row=12,column=0,pady=2)


First_name_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2 ,font=("arial black", 10),bg='gray', fg='cyan')
First_name_del.grid(row=1, column=1, pady=2)
last_name_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2 ,font=("arial black", 10),bg='gray', fg='cyan')
last_name_del.grid(row=2,column=1, pady=2)
other_name_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
other_name_del.grid(row=3,column=1,pady=2)
date_of_birth_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
date_of_birth_del.grid(row=4,column=1,pady=2)
gender_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
gender_del.grid(row=5,column=1,pady=2)
age_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
age_del.grid(row=6,column=1,pady=2)
mnth_year_admission_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
mnth_year_admission_del.grid(row=7,column=1,pady=2)
school_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
school_del.grid(row=8,column=1,pady=2)
class_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
class_del.grid(row=9,column=1,pady=2)
religion_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
religion_del.grid(row=10,column=1,pady=2)
nationality_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
nationality_del.grid(row=11,column=1,pady=2)
state_of_origin_del = Label(name_frame2, text="",width=20, border=5,borderwidth=5, highlightthickness=2, font=("arial black", 10),bg='gray', fg='cyan')
state_of_origin_del.grid(row=12,column=1,pady=2)

def exd():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #inserting to database
    
    record_id = txt_search_del.get()
    c.execute("DELETE from student_registers WHERE  oid =" + record_id)
    
    conn.commit()
    conn.close()
    First_name_del.destroy()
    last_name_del.destroy()
    other_name_del.destroy()
    date_of_birth_del.destroy()
    gender_del.destroy()
    age_del.destroy()
    mnth_year_admission_del.destroy()
    school_del.destroy()
    class_del.destroy()
    religion_del.destroy()
    nationality_del.destroy()
    state_of_origin_del.destroy()
    txt_search_del.delete(0, END)
    
def exit():
    
    First_name_del.destroy()
    last_name_del.destroy()
    other_name_del.destroy()
    date_of_birth_del.destroy()
    gender_del.destroy()
    age_del.destroy()
    mnth_year_admission_del.destroy()
    school_del.destroy()
    class_del.destroy()
    religion_del.destroy()
    nationality_del.destroy()
    state_of_origin_del.destroy()
    txt_search_del.delete(0, END)
    hide_frame()
# _____________________________________________creating Buttons_____________________________________________
btn_delete = Button(confirm_frame2, text="DELETE",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command=exd)
btn_delete.grid(row=11, column=0, padx=2)

btn_exit_del = Button(confirm_frame2, text="EXIT",font=("arial black",8), width=13, bg="GREEN", fg="Black", borderwidth=5, command= exit)
btn_exit_del.grid(row=11, column=1, padx=2)

#_____________________________________COURSE REGISTRATION MENU__________________________________________
def search_id():
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #select from database
    
    record_id = search_stud.get()
    c.execute("SELECT * FROM student_registers WHERE oid =" + record_id)
    records = c.fetchall()
    print(records)
    
    txt_full_name.delete(0,END)
    txt_class_level.delete(0,END)
    txt_class_sub.delete(0,END)
    txt_gender_sub.delete(0,END)
    txt_age_sub.delete(0,END)
    txt_stud_id.delete(0,END)
    
    
    # looping through the result
    for record in records:
        txt_full_name.insert(0,record[0] + " " + record[1] + " " + record[2])
        txt_class_level.insert(0,record[10])
        txt_class_sub.insert(0,record[11])
        txt_gender_sub.insert(0,record[5])
        txt_age_sub.insert(0,record[6])
        txt_stud_id.insert(0,"PKC/" + record[9] + "/" + record_id)
    conn.commit()
    conn.close()
    
    

    if txt_class_level.get().upper()== "JUNIOR SCHOOL":
        j_sub_frame.grid(row=8,column=0, columnspan=2, pady= 10)
        s_sub_frame.grid_forget()
        prev_sub_frame.grid_forget()

    elif txt_class_level.get().upper()== "SENIOR SCHOOL":
        s_sub_frame.grid(row=8,column=0, columnspan=2, pady= 10)
        j_sub_frame.grid_forget()
        prev_sub_frame.grid_forget()
    
x_frame= Frame(course_reg_frame)
x_frame.pack()

main_course_frame = Frame(x_frame,highlightthickness=2)
main_course_frame.pack()
lbl_main_course_frame = customtkinter.CTkLabel(main_course_frame,text="SUBJECT REGISTRATION", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_main_course_frame.grid(row=0, column=0, columnspan=2)
search_stud = customtkinter.CTkEntry(main_course_frame, fg_color="cyan", corner_radius=8 )
search_stud.grid(row=1, column=0)
btn_stud_search = customtkinter.CTkButton(main_course_frame, text="search",font=("Arial black",12), fg_color="cyan",width=20 , height=20, corner_radius=8, hover_color="green", command = search_id)
btn_stud_search.grid(row = 1,column=0, columnspan=2)

lbl_full_name = customtkinter.CTkLabel(main_course_frame,text="FULL NAME", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_full_name.grid(row=2, column=0)
lbl_class_level = customtkinter.CTkLabel(main_course_frame,text="CLASS LEVEL", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_class_level.grid(row=3, column=0)
lbl_class = customtkinter.CTkLabel(main_course_frame,text="CLASS", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_class.grid(row=4, column=0)
lbl_gender = customtkinter.CTkLabel(main_course_frame,text="GENDER", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_gender.grid(row=5, column=0)
lbl_age = customtkinter.CTkLabel(main_course_frame,text="AGE", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_age.grid(row=6, column=0)
lbl_stud_id = customtkinter.CTkLabel(main_course_frame,text="STUDENT I.D", text_color="cyan",font=("Arial black",13),corner_radius=8)
lbl_stud_id.grid(row=7, column=0)

txt_full_name = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_full_name.grid(row=2, column=1, padx=3,pady=2)
txt_class_level = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_class_level.grid(row=3, column=1, padx=3,pady=2)
txt_class_sub = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_class_sub.grid(row=4, column=1, padx=3,pady=2)
txt_gender_sub = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_gender_sub.grid(row=5, column=1, padx=3,pady=2)
txt_age_sub = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_age_sub.grid(row=6, column=1, padx=3,pady=2)
txt_stud_id = customtkinter.CTkEntry(main_course_frame,font=("Arial black", 10), width= 250,corner_radius=10,fg_color='cyan')
txt_stud_id.grid(row=7, column=1, padx=3,pady=2)

#creating frame and scrollbar for the list boxes
j_sub_var1 = StringVar()
j_sub_var2 = StringVar()
j_sub_var3 = StringVar()
j_sub_var4 = StringVar()
j_sub_var5 = StringVar()
j_sub_var6 = StringVar()
j_sub_var7 = StringVar()
j_sub_var8 = StringVar()
j_sub_var9 = StringVar()
j_sub_var10 = StringVar()
j_sub_var11 =StringVar()

j_sub_frame = LabelFrame(main_course_frame,text="JUNIOR SCHOOL SUBJECT",height=5)
j_sub_frame.grid_forget()

j_sub_scroll= customtkinter.CTkScrollableFrame(j_sub_frame, fg_color="white", scrollbar_button_hover_color="green")
j_sub_scroll.pack()

cbx_sub_1 = Checkbutton(j_sub_scroll, text = "PROVOCATIONAL STUDIES", variable=j_sub_var1, onvalue="PROVOCATIONAL STUDIES" , offvalue=" ")
cbx_sub_1.deselect()
cbx_sub_1.grid(row=0, column=0, pady=3)
cbx_sub_2 = Checkbutton(j_sub_scroll, text = "ENGLISH LANGAUGE", variable=j_sub_var2, onvalue="ENGLISH LANGAUGE" , offvalue=" ")
cbx_sub_2.deselect()
cbx_sub_2.grid(row=1, column=0, pady=3)
cbx_sub_3 = Checkbutton(j_sub_scroll, text = "BASIC TECHNOLOGY", variable=j_sub_var3, onvalue="BASIC TECHNOLOGY" , offvalue=" ")
cbx_sub_3.deselect()
cbx_sub_3.grid(row=2, column=0, pady=3)
cbx_sub_4 = Checkbutton(j_sub_scroll, text = "BUSINESS STUDIES", variable=j_sub_var4, onvalue="BUSINESS STUDIES" , offvalue=" ")
cbx_sub_4.deselect()
cbx_sub_4.grid(row=3, column=0, pady=3)
cbx_sub_5 = Checkbutton(j_sub_scroll, text = "YORUBA LANGUAGE", variable=j_sub_var5, onvalue="YORUBA LANGUAGE" , offvalue=" ")
cbx_sub_5.deselect()
cbx_sub_5.grid(row=4, column=0, pady=3)
cbx_sub_6 = Checkbutton(j_sub_scroll, text = "IGBO LANGUAGE", variable=j_sub_var6, onvalue="IGBO LANGUAGE", offvalue=" " )
cbx_sub_6.deselect()
cbx_sub_6.grid(row=5, column=0, pady=3)
cbx_sub_7 = Checkbutton(j_sub_scroll, text = "MATHEMATICS", variable=j_sub_var7, onvalue="MATHEMATICS" , offvalue=" ")
cbx_sub_7.deselect()
cbx_sub_7.grid(row=6, column=0, pady=3)
cbx_sub_8 = Checkbutton(j_sub_scroll, text = "FRENCH", variable=j_sub_var8, onvalue="FRENCH" , offvalue=" ")
cbx_sub_8.deselect()
cbx_sub_8.grid(row=7, column=0, pady=3)
cbx_sub_9 = Checkbutton(j_sub_scroll, text = "HISTORY", variable=j_sub_var9, onvalue="HISTORY" , offvalue=" ")
cbx_sub_9.deselect()
cbx_sub_9.grid(row=8, column=0, pady=3)
cbx_sub_10 = Checkbutton(j_sub_scroll, text = "C.C.A", variable=j_sub_var10, onvalue="C.C.A" , offvalue=" ")
cbx_sub_10.deselect()
cbx_sub_10.grid(row=9, column=0, pady=3)
cbx_sub_11 = Checkbutton(j_sub_scroll, text = "R.N.V", variable=j_sub_var11, onvalue="R.N.V" , offvalue=" ")
cbx_sub_11.deselect()
cbx_sub_11.grid(row=10, column=0, pady=3)


s_sub_frame = Frame(main_course_frame)
s_sub_frame.grid_forget()

s_sub_var1 = StringVar()
s_sub_var2 = StringVar()
s_sub_var3 = StringVar()
s_sub_var4 = StringVar()
s_sub_var5 = StringVar()
s_sub_var6 = StringVar()
s_sub_var7 = StringVar()
s_sub_var8 = StringVar()
s_sub_var9 = StringVar()
s_sub_var10 = StringVar()
s_sub_var11 = StringVar()
s_sub_var12 = StringVar()
s_sub_var13 = StringVar()
s_sub_var14 = StringVar()
s_sub_var15 = StringVar()
s_sub_var16 = StringVar()
s_sub_var17 = StringVar()
s_sub_var18 = StringVar()
s_sub_var19 = StringVar()
s_sub_var20 = StringVar()

s_sub_scroll= customtkinter.CTkScrollableFrame(s_sub_frame, fg_color="white", scrollbar_button_hover_color="green")
s_sub_scroll.pack()

s_cbx_sub_1 = Checkbutton(s_sub_scroll, text = "AGRICULTURAL SCIENCE", variable=s_sub_var1 , onvalue="AGRICULTURAL SCIENCE" , offvalue=" ")
s_cbx_sub_1.deselect()
s_cbx_sub_1.grid(row=0, column=0, pady=3)
s_cbx_sub_2 = Checkbutton(s_sub_scroll, text = "FUTHER-MATHEMATICS", variable=s_sub_var2 , onvalue="FUTHER-MATHEMATICS" , offvalue="")
s_cbx_sub_2.deselect()
s_cbx_sub_2.grid(row=1, column=0, pady=3)
s_cbx_sub_3 = Checkbutton(s_sub_scroll, text = "TECHNICAL DARWING", variable=s_sub_var3 , onvalue="TECHNICAL DARWING" , offvalue="")
s_cbx_sub_3.deselect()
s_cbx_sub_3.grid(row=2, column=0, pady=3)
s_cbx_sub_4 = Checkbutton(s_sub_scroll, text = "ENGLISH LANGAUGE", variable=s_sub_var4 , onvalue="ENGLISH LANGAUGE" , offvalue="")
s_cbx_sub_4.deselect()
s_cbx_sub_4.grid(row=3, column=0, pady=3)
s_cbx_sub_5 = Checkbutton(s_sub_scroll, text = "YORUBA LANGUAGE", variable=s_sub_var5 , onvalue="YORUBA LANGUAGE" , offvalue="")
s_cbx_sub_5.deselect()
s_cbx_sub_5.grid(row=4, column=0, pady=3)
s_cbx_sub_6 = Checkbutton(s_sub_scroll, text = "DATA-PROCESSING", variable=s_sub_var6 , onvalue="DATA-PROCESSING" , offvalue="")
s_cbx_sub_6.deselect()
s_cbx_sub_6.grid(row=5, column=0, pady=3)
s_cbx_sub_7 = Checkbutton(s_sub_scroll, text = "IGBO LANGUAGE", variable=s_sub_var7 , onvalue="IGBO LANGUAGE" , offvalue="")
s_cbx_sub_7.deselect()
s_cbx_sub_7.grid(row=6, column=0, pady=3)
s_cbx_sub_8 = Checkbutton(s_sub_scroll, text = "MATHEMATICS", variable=s_sub_var8, onvalue="MATHEMATICS" , offvalue="")
s_cbx_sub_8.deselect()
s_cbx_sub_8.grid(row=7, column=0, pady=3)
s_cbx_sub_9 = Checkbutton(s_sub_scroll, text = "GOVERNMENT", variable=s_sub_var9 , onvalue="GOVERNMENT" , offvalue="")
s_cbx_sub_9.deselect()
s_cbx_sub_9.grid(row=8, column=0, pady=3)
s_cbx_sub_10 = Checkbutton(s_sub_scroll, text = "ACCOUNTING", variable=s_sub_var10 , onvalue="ACCOUNTING" , offvalue="")
s_cbx_sub_10.deselect()
s_cbx_sub_10.grid(row=9, column=0, pady=3)
s_cbx_sub_11 = Checkbutton(s_sub_scroll, text = "GEOGRAPHY", variable=s_sub_var11 , onvalue="GEOGRAPHY" , offvalue="")
s_cbx_sub_11.deselect()
s_cbx_sub_11.grid(row=10, column=0, pady=3)
s_cbx_sub_12 = Checkbutton(s_sub_scroll, text = "ECONOMICS", variable=s_sub_var12 , onvalue="ECONOMICS" , offvalue="")
s_cbx_sub_12.deselect()
s_cbx_sub_12.grid(row=11, column=0, pady=3)
s_cbx_sub_13 = Checkbutton(s_sub_scroll, text = "LITERATURE", variable=s_sub_var13, onvalue="LITERATURE" , offvalue="")
s_cbx_sub_13.deselect()
s_cbx_sub_13.grid(row=12, column=0, pady=3)
s_cbx_sub_14 = Checkbutton(s_sub_scroll, text = "COMMERCE", variable=s_sub_var14 , onvalue="COMMERCE" , offvalue="")
s_cbx_sub_14.deselect()
s_cbx_sub_14.grid(row=13, column=0, pady=3)
s_cbx_sub_15 = Checkbutton(s_sub_scroll, text = "CHEMISTRY", variable=s_sub_var15, onvalue="CHEMISTRY" , offvalue="")
s_cbx_sub_15.deselect()
s_cbx_sub_15.grid(row=14, column=0, pady=3)
s_cbx_sub_16 = Checkbutton(s_sub_scroll, text = "PHYSICS", variable=s_sub_var16 , onvalue="PHYSICS" , offvalue="")
s_cbx_sub_16.deselect()
s_cbx_sub_16.grid(row=15, column=0, pady=3)
s_cbx_sub_17 = Checkbutton(s_sub_scroll, text = "BIOLOGY", variable=s_sub_var17 , onvalue="BIOLOGY" , offvalue="")
s_cbx_sub_17.deselect()
s_cbx_sub_17.grid(row=16, column=0, pady=3)
s_cbx_sub_18 = Checkbutton(s_sub_scroll, text = "CIVIC", variable=s_sub_var18 , onvalue="CIVIC" , offvalue="")
s_cbx_sub_18.deselect()
s_cbx_sub_18.grid(row=17, column=0, pady=3)
s_cbx_sub_19 = Checkbutton(s_sub_scroll, text = "C.R.S", variable=s_sub_var19 , onvalue="C.R.S", offvalue="" )
s_cbx_sub_19.deselect()
s_cbx_sub_19.grid(row=18, column=0, pady=3)
s_cbx_sub_20 = Checkbutton(s_sub_scroll, text = "I.C.T", variable=s_sub_var20 , onvalue="I.C.T", offvalue="" )
s_cbx_sub_20.deselect()
s_cbx_sub_20.grid(row=19, column=0, pady=3)


prev_sub_frame = Frame(course_reg_frame)

prev_sub_scroll = Scrollbar(prev_sub_frame, orient=HORIZONTAL)
prev_list = ttk.Treeview(prev_sub_frame,xscrollcommand=prev_sub_scroll.set)

prev_sub_scroll.config(command=prev_list.xview)
prev_sub_scroll.pack(side=BOTTOM, fill=X)
prev_list.pack()


prev_list['columns'] = ("NAME","SCHOOL","CLASS","GENDER","AGE","ID","COURSE")

prev_list.column("#0", width=0, minwidth=0)
prev_list.column("NAME", anchor=W, width=180)
prev_list.column("SCHOOL", anchor=W, width=100)
prev_list.column("CLASS", anchor=W, width=50)
prev_list.column("GENDER", anchor=CENTER, width=80)
prev_list.column("AGE", anchor=W, width=50)
prev_list.column("ID", anchor=W, width=120)
prev_list.column("COURSE", anchor=W, width=2000)

prev_list.heading("#0",text= "", anchor=W)
prev_list.heading("NAME",text= "NAME", anchor=W)
prev_list.heading("SCHOOL",text= "SCHOOL LEVEL", anchor=W)
prev_list.heading("CLASS",text= "CLASS", anchor=W)
prev_list.heading("GENDER",text= "GENDER", anchor=CENTER)
prev_list.heading("AGE",text= "AGE", anchor=W)
prev_list.heading("ID",text= "STUDENT ID", anchor=W)
prev_list.heading("COURSE",text= "COURSES", anchor=W)

prev_sub_frame.pack_forget()


chk_frame = customtkinter.CTkFrame(main_course_frame,fg_color="white", corner_radius=5)
chk_frame.grid(row=9,column=0, columnspan=2, pady= 10)
                    
def c_pre():
    prev_sub_frame.pack(pady= 10)
    global course
    course =""
    if txt_class_level.get().upper()== "JUNIOR SCHOOL":
        course = j_sub_var1.get() + "  " + j_sub_var2.get()+ "  " + j_sub_var3.get()+ "  " + j_sub_var4.get()+ "  " + j_sub_var5.get()+ "  " + j_sub_var6.get() + "  " + j_sub_var7.get()+ "  " + j_sub_var8.get()+ "  " + j_sub_var9.get()+ "  " + j_sub_var10.get()+ "  " + j_sub_var11.get()
        print(course)
            
    elif txt_class_level.get().upper()== "SENIOR SCHOOL":
        course = s_sub_var1.get() + "  " + s_sub_var2.get()+ "  " + s_sub_var3.get()+ "  " + s_sub_var4.get()+ "  " + s_sub_var5.get()+ "  " + s_sub_var6.get() + "  " + s_sub_var7.get()+ "  " + s_sub_var8.get()+ "  " + s_sub_var9.get()+ "  " + s_sub_var10.get()+ "  " + s_sub_var11.get() + s_sub_var12.get() + "  " + s_sub_var13.get()+ "  " + s_sub_var14.get()+ "  " + s_sub_var15.get()+ "  " + s_sub_var16.get()+ "  " + s_sub_var17.get() + "  " + s_sub_var18.get()+ "  " + s_sub_var19.get()+ "  " + s_sub_var20.get()
        print(course)
        
    j_sub_frame.grid_forget()
    s_sub_frame.grid_forget()

    prev_list.insert(parent="", index="end", iid=0,text = "", values=(txt_full_name.get().upper(),txt_class_level.get().upper(),txt_class_sub.get().upper(),txt_gender_sub.get().upper(),txt_age_sub.get().upper(),
                                                                            txt_stud_id.get().upper(),course))
    
    
def c_reg():
    # saving student required subject to database
        course = ""
        
    
        conn = sqlite3.connect('student management system.db')

        c = conn.cursor()
    #inserting to database
          
        c.execute("INSERT INTO subjects VALUES(:full_name, :class_level, :class, :gender, :age, :student_id, :subject1, :subject2, :subject3, :subject4, :subject5, :subject6,:subject7,:subject8,:subject9,:subject10,:subject11,:subject12,:subject13,:subject14,:subject15,:subject16,:subject17,:subject18,:subject19,:subject20)",
              
                  {
                      'full_name': txt_full_name.get(),
                      'class_level': txt_class_level.get(),
                      'class': txt_class_sub.get(),
                      'gender': txt_gender_sub.get(),
                      'age': txt_age_sub.get(),
                      'student_id': txt_stud_id.get(),
                      'subject1': s_sub_var1.get(),
                      'subject2': s_sub_var2.get(),
                      'subject3': s_sub_var3.get(),
                      'subject4': s_sub_var4.get(),
                      'subject5': s_sub_var5.get(),
                      'subject6': s_sub_var6.get(),
                      'subject7': s_sub_var7.get(),
                      'subject8': s_sub_var8.get(),
                      'subject9': s_sub_var9.get(),
                      'subject10': s_sub_var10.get(),
                      'subject11': s_sub_var11.get(),
                      'subject12': s_sub_var12.get(),
                      'subject13': s_sub_var13.get(),
                      'subject14': s_sub_var14.get(),
                      'subject15': s_sub_var15.get(),
                      'subject16': s_sub_var16.get(),
                      'subject17': s_sub_var17.get(),
                      'subject18': s_sub_var18.get(),
                      'subject19': s_sub_var19.get(),
                      'subject20': s_sub_var20.get()
                  })
            
           
        conn.commit()
        conn.close()
        messagebox.showinfo("COMFIRMATION","DATA SAVED SUCCESSFULLY")
        txt_full_name.delete(0,END)
        txt_class_level.delete(0,END)
        txt_class_sub.delete(0,END)
        txt_gender_sub.delete(0,END)
        txt_age_sub.delete(0,END)
        txt_stud_id.delete(0,END)
        txt_class_level.delete(0,END)
        search_stud.delete(0, END)
        search_stud.focus_set()
        

        
def c_clear():
    txt_full_name.delete(0,END)
    txt_class_level.delete(0,END)
    txt_class_sub.delete(0,END)
    txt_gender_sub.delete(0,END)
    txt_age_sub.delete(0,END)
    txt_stud_id.delete(0,END)
    txt_class_level.delete(0,END)
    search_stud.delete(0, END)
    prev_list.delete()
    
    prev_sub_frame.grid_forget()
    j_sub_frame.grid_forget()
    s_sub_frame.grid_forget()
    
    search_stud.focus_set()


    
def c_exit():
    hide_frame()

btn_subject_preview = customtkinter.CTkButton(chk_frame, text="PREVIEW",font=("Arial black",12), fg_color="cyan",width=20 , height=20, corner_radius=8, hover_color="green", command = c_pre)
btn_subject_preview.grid(row = 0,column=0, padx=5)
btn_subject_register = customtkinter.CTkButton(chk_frame, text="REGISTER",font=("Arial black",12), fg_color="cyan",width=20 , height=20, corner_radius=8, hover_color="green", command = c_reg)
btn_subject_register.grid(row = 0,column=1, padx=5)
btn_subject_clear = customtkinter.CTkButton(chk_frame, text="CLEAR",font=("Arial black",12), fg_color="cyan",width=20 , height=20, corner_radius=8, hover_color="green", command = c_clear)
btn_subject_clear.grid(row = 0,column=2, padx=5)
btn_subject_exit = customtkinter.CTkButton(chk_frame, text="EXIT",font=("Arial black",12), fg_color="cyan",width=20 , height=20, corner_radius=8, hover_color="red", command = c_exit)
btn_subject_exit.grid(row = 0,column=3,padx = 5)

#_____________________________________editing of selected subject_______________________________________

def stud_id():
    
    conn = sqlite3.connect('student management system.db')

    c = conn.cursor()
    #select from database
    
    sub_rec_id = search_edit_sub.get()
    c.execute("SELECT * FROM subjects WHERE student_id=?",(sub_rec_id,))
    sub_records = c.fetchall()
    print(sub_records)
    
    txt_full_name_edit_sub.delete(0,END)
    txt_class_level_edit_sub.delete(0,END)
    txt_class_edit_sub.delete(0,END)
    txt_gender_edit_sub.delete(0,END)
    txt_age_edit_sub.delete(0,END)
    txt_stud_id_edit_sub.delete(0,END)
    sub1.configure(text="")
    sub2.configure(text="")
    sub3.configure(text="")
    sub4.configure(text="")
    sub5.configure(text="")
    sub6.configure(text="")
    sub7.configure(text="")
    sub8.configure(text="")
    sub9.configure(text="")
    sub10.configure(text="")
    sub11.configure(text="")
    sub12.configure(text="")
    sub13.configure(text="")
    sub14.configure(text="")
    sub15.configure(text="")
    sub16.configure(text="")
    sub17.configure(text="")
    sub18.configure(text="")
    sub19.configure(text="")
    sub20.configure(text="")
    
    
    # looping through the result
    for record in sub_records:
        txt_full_name_edit_sub.insert(0,record[0])
        txt_class_level_edit_sub.insert(0,record[1])
        txt_class_edit_sub.insert(0,record[2])
        txt_gender_edit_sub.insert(0,record[3])
        txt_age_edit_sub.insert(0,record[4])
        txt_stud_id_edit_sub.insert(0,record[5])
        
        sub1.configure(text=record[6])
        sub2.configure(text=record[7])
        sub3.configure(text=record[8])
        sub4.configure(text=record[9])
        sub5.configure(text=record[10])
        sub6.configure(text=record[11])
        sub7.configure(text=record[12])
        sub8.configure(text=record[13])
        sub9.configure(text=record[14])
        sub10.configure(text=record[15])
        sub11.configure(text=record[16])
        sub12.configure(text=record[17])
        sub13.configure(text=record[18])
        sub14.configure(text=record[19])
        sub15.configure(text=record[20])
        sub16.configure(text=record[21])
        sub17.configure(text=record[22])
        sub18.configure(text=record[23])
        sub19.configure(text=record[24])
        sub20.configure(text=record[25])
    
    conn.commit()
    conn.close()
    
    
    
    
main_course_edit_frame = LabelFrame(course_edit_frame,text="SUBJECT FRAME",highlightthickness=2)
main_course_edit_frame.pack()
lbl_main_course_edit_frame = customtkinter.CTkLabel(main_course_edit_frame,text="SUBJECT EDITING PAGE", text_color="black",font=("cambria",20),corner_radius=8)
lbl_main_course_edit_frame.grid(row=0, column=0, columnspan=2)
search_edit_sub = customtkinter.CTkEntry(main_course_edit_frame, fg_color="white", text_color="black", corner_radius=8 )
search_edit_sub.grid(row=1, column=0)
btn_stud_search_edit = customtkinter.CTkButton(main_course_edit_frame, text="SEARCH",font=("cambria",12), fg_color="white", text_color="black",width=20 , height=20, corner_radius=8, hover_color="green", command = stud_id)
btn_stud_search_edit.grid(row = 1,column=0, columnspan=2)

lbl_full_name1 = customtkinter.CTkLabel(main_course_edit_frame,text="FULL NAME", text_color="black",font=("cambria",13),corner_radius=8)
lbl_full_name1.grid(row=2, column=0)
lbl_class_level1 = customtkinter.CTkLabel(main_course_edit_frame,text="CLASS LEVEL", text_color="black",font=("cambria",13),corner_radius=8)
lbl_class_level1.grid(row=3, column=0)
lbl_class1 = customtkinter.CTkLabel(main_course_edit_frame,text="CLASS", text_color="black",font=("cambria",13),corner_radius=8)
lbl_class1.grid(row=4, column=0)
lbl_gender1 = customtkinter.CTkLabel(main_course_edit_frame,text="GENDER", text_color="black",font=("cambria",13),corner_radius=8)
lbl_gender1.grid(row=5, column=0)
lbl_age1 = customtkinter.CTkLabel(main_course_edit_frame,text="AGE", text_color="black",font=("cambria",13),corner_radius=8)
lbl_age1.grid(row=6, column=0)
lbl_stud_id1 = customtkinter.CTkLabel(main_course_edit_frame,text="STUDENT I.D", text_color="black",font=("cambria",13),corner_radius=8)
lbl_stud_id1.grid(row=7, column=0)

txt_full_name_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_full_name_edit_sub.grid(row=2, column=1, padx=3,pady=2)
txt_class_level_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_class_level_edit_sub.grid(row=3, column=1, padx=3,pady=2)
txt_class_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_class_edit_sub.grid(row=4, column=1, padx=3,pady=2)
txt_gender_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_gender_edit_sub.grid(row=5, column=1, padx=3,pady=2)
txt_age_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_age_edit_sub.grid(row=6, column=1, padx=3,pady=2)
txt_stud_id_edit_sub = customtkinter.CTkEntry(main_course_edit_frame,font=("cambria", 10), width= 250,corner_radius=10,fg_color='white',bg_color="white", text_color="black")
txt_stud_id_edit_sub.grid(row=7, column=1, padx=3,pady=2)

senior_subject_frame_edit= LabelFrame(main_course_edit_frame,text= "SENIOR SUBJECT",font=("cambria", 10), foreground="black")
senior_subject_frame_edit.grid(row=8, column=0)
senior_subject_frame_edit_load= LabelFrame(main_course_edit_frame,text= " UPDATE SENIOR SUBJECT",font=("cambria", 10), foreground="black")
senior_subject_frame_edit_load.grid(row=8, column=1)

# __________________ creating channel for value in from the databbase_____________________
 

subject_edit_scrollframe =customtkinter.CTkScrollableFrame(senior_subject_frame_edit,bg_color="white", fg_color="white", scrollbar_button_hover_color="green", orientation="horizontal")
subject_edit_scrollframe.pack()
subject_edit_scrollframe_edit =customtkinter.CTkScrollableFrame(senior_subject_frame_edit_load,bg_color="white", fg_color="white", scrollbar_button_hover_color="green", orientation="horizontal")
subject_edit_scrollframe_edit.pack()
#__________ creating subject textbox for database fillup_________________________

sub1 =Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub1.grid(row=0, column = 0, padx=5, pady=5)
sub2 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub2.grid(row=0, column = 1, padx=5, pady=5)
sub3 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub3.grid(row=0, column = 2, padx=5, pady=5)
sub4 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub4.grid(row=0, column = 3, padx=5, pady=5)
sub5 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub5.grid(row=1, column = 0, padx=5, pady=5)
sub6 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub6.grid(row=1, column = 1, padx=5, pady=5)
sub7 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub7.grid(row=1, column = 2, padx=5, pady=5)
sub8 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub8.grid(row=1, column = 3, padx=5, pady=5)
sub9 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub9.grid(row=2, column = 0, padx=5, pady=5)
sub10 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub10.grid(row=2, column = 1, padx=5, pady=5)
sub11 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub11.grid(row=2, column = 2, padx=5, pady=5)
sub12 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub12.grid(row=2, column = 3, padx=5, pady=5)
sub13 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub13.grid(row=3, column = 0, padx=5, pady=5)
sub14 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub14.grid(row=3, column = 1, padx=5, pady=5)
sub15 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub15.grid(row=3, column = 2, padx=5, pady=5)
sub16 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub16.grid(row=3, column = 3, padx=5, pady=5)
sub17 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub17.grid(row=4, column = 0, padx=5, pady=5)
sub18 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub18.grid(row=4, column = 1, padx=5, pady=5)
sub19 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub19.grid(row=4, column = 2, padx=5, pady=5)
sub20 = Label(subject_edit_scrollframe,text="",font=("cambria", 12), width= 20,foreground='black',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="white")
sub20.grid(row=4, column = 3, padx=5, pady=5)

# creating subject selection part

e_sub_var1 = StringVar()
e_sub_var2 = StringVar()
e_sub_var3 = StringVar()
e_sub_var4 = StringVar()
e_sub_var5 = StringVar()
e_sub_var6 = StringVar()
e_sub_var7 = StringVar()
e_sub_var8 = StringVar()
e_sub_var9 = StringVar()
e_sub_var10 = StringVar()
e_sub_var11 = StringVar()
e_sub_var12 = StringVar()
e_sub_var13 = StringVar()
e_sub_var14 = StringVar()
e_sub_var15 = StringVar()
e_sub_var16 = StringVar()
e_sub_var17 = StringVar()
e_sub_var18 = StringVar()
e_sub_var19 = StringVar()
e_sub_var20 = StringVar()


def cbx1():
    if e_cbx_sub_1.select:
        sub1.configure(text= e_sub_var1.get())
    else:
        sub1.configure(text= "")
e_cbx_sub_1 = Checkbutton(subject_edit_scrollframe_edit, text = "AGRICULTURAL SCIENCE", variable=e_sub_var1 , onvalue="AGRICULTURAL SCIENCE" , offvalue="",command=cbx1)
e_cbx_sub_1.deselect()
e_cbx_sub_1.grid(row=0, column=0, padx=5 ,pady=5)

def cbx2():
    if e_cbx_sub_2.select:
        sub2.configure(text= e_sub_var2.get())
    else:
        sub2.configure(text= "")
e_cbx_sub_2 = Checkbutton(subject_edit_scrollframe_edit, text = "FUTHER-MATHEMATICS", variable=e_sub_var2 , onvalue="FUTHER-MATHEMATICS" , offvalue="",command=cbx2)
e_cbx_sub_2.deselect()
e_cbx_sub_2.grid(row=1, column=0, padx=5 ,pady=5)

def cbx3():
    if e_cbx_sub_3.select:
        sub3.configure(text= e_sub_var3.get())
    else:
        sub3.configure(text= "")
e_cbx_sub_3 = Checkbutton(subject_edit_scrollframe_edit, text = "TECHNICAL DARWING", variable=e_sub_var3 , onvalue="TECHNICAL DARWING" , offvalue="",command=cbx3)
e_cbx_sub_3.deselect()
e_cbx_sub_3.grid(row=2, column=0, padx=5 ,pady=5)

def cbx4():
    if e_cbx_sub_4.select:
        sub4.configure(text= e_sub_var4.get())
    else:
        sub4.configure(text= "")
e_cbx_sub_4 = Checkbutton(subject_edit_scrollframe_edit, text = "ENGLISH LANGAUGE", variable=e_sub_var4 , onvalue="ENGLISH LANGAUGE" , offvalue="",command=cbx4)
e_cbx_sub_4.deselect()
e_cbx_sub_4.grid(row=3, column=0, padx=5 ,pady=5)

def cbx5():
    if e_cbx_sub_5.select:
        sub5.configure(text= e_sub_var5.get())
    else:
        sub5.configure(text= "")
e_cbx_sub_5 = Checkbutton(subject_edit_scrollframe_edit, text = "YORUBA LANGUAGE", variable=e_sub_var5 , onvalue="YORUBA LANGUAGE" , offvalue="",command=cbx5)
e_cbx_sub_5.deselect()
e_cbx_sub_5.grid(row=4, column=0, padx=5 ,pady=5)

def cbx6():
    if e_cbx_sub_6.select:
        sub6.configure(text= e_sub_var6.get())
    else:
        sub6.configure(text= "")
e_cbx_sub_6 = Checkbutton(subject_edit_scrollframe_edit, text = "DATA-PROCESSING", variable=e_sub_var6 , onvalue="DATA-PROCESSING" , offvalue="",command=cbx6)
e_cbx_sub_6.deselect()
e_cbx_sub_6.grid(row=0, column=1, padx=5 ,pady=5)

def cbx7():
    if e_cbx_sub_7.select:
        sub7.configure(text= e_sub_var7.get())
    else:
        sub7.configure(text= "")
e_cbx_sub_7 = Checkbutton(subject_edit_scrollframe_edit, text = "IGBO LANGUAGE", variable=e_sub_var7 , onvalue="IGBO LANGUAGE" , offvalue="", command=cbx7)
e_cbx_sub_7.deselect()
e_cbx_sub_7.grid(row=1, column=1, padx=5 ,pady=5)

def cbx8():
    if e_cbx_sub_8.select:
        sub8.configure(text= e_sub_var8.get())
    else:
        sub8.configure(text= "")
e_cbx_sub_8 = Checkbutton(subject_edit_scrollframe_edit, text = "MATHEMATICS", variable=e_sub_var8, onvalue="MATHEMATICS" , offvalue="", command=cbx8)
e_cbx_sub_8.deselect()
e_cbx_sub_8.grid(row=2, column=1, padx=5 ,pady=5)

def cbx9():
    if e_cbx_sub_9.select:
        sub9.configure(text= e_sub_var9.get())
    else:
        sub9.configure(text= "")
e_cbx_sub_9 = Checkbutton(subject_edit_scrollframe_edit, text = "GOVERNMENT", variable=e_sub_var9 , onvalue="GOVERNMENT" , offvalue="", command=cbx9)
e_cbx_sub_9.deselect()
e_cbx_sub_9.grid(row=3, column=1, padx=5 ,pady=5)

def cbx10():
    if e_cbx_sub_10.select:
        sub10.configure(text= e_sub_var10.get())
    else:
        sub10.configure(text= "")
e_cbx_sub_10 = Checkbutton(subject_edit_scrollframe_edit, text = "ACCOUNTING", variable=e_sub_var10 , onvalue="ACCOUNTING" , offvalue="",command=cbx10)
e_cbx_sub_10.deselect()
e_cbx_sub_10.grid(row=4, column=1, padx=5 ,pady=5)

def cbx11():
    if e_cbx_sub_11.select:
        sub11.configure(text= e_sub_var11.get())
    else:
        sub11.configure(text= "")
e_cbx_sub_11 = Checkbutton(subject_edit_scrollframe_edit, text = "GEOGRAPHY", variable=e_sub_var11 , onvalue="GEOGRAPHY" , offvalue="", command=cbx11)
e_cbx_sub_11.deselect()
e_cbx_sub_11.grid(row=0, column=2, padx=5 ,pady=5)

def cbx12():
    if e_cbx_sub_12.select:
        sub12.configure(text= e_sub_var12.get())
    else:
        sub12.configure(text= "")
e_cbx_sub_12 = Checkbutton(subject_edit_scrollframe_edit, text = "ECONOMICS", variable=e_sub_var12 , onvalue="ECONOMICS" , offvalue="", command=cbx12)
e_cbx_sub_12.deselect()
e_cbx_sub_12.grid(row=1, column=2, padx=5 ,pady=5)

def cbx13():
    if e_cbx_sub_13.select:
        sub13.configure(text= e_sub_var13.get())
    else:
        sub13.configure(text= "")
e_cbx_sub_13 = Checkbutton(subject_edit_scrollframe_edit, text = "LITERATURE", variable=e_sub_var13, onvalue="LITERATURE" , offvalue="",command=cbx13)
e_cbx_sub_13.deselect()
e_cbx_sub_13.grid(row=2, column=2, padx=5 ,pady=5)

def cbx14():
    if e_cbx_sub_14.select:
        sub14.configure(text= e_sub_var14.get())
    else:
        sub14.configure(text= "")
e_cbx_sub_14 = Checkbutton(subject_edit_scrollframe_edit, text = "COMMERCE", variable=e_sub_var14 , onvalue="COMMERCE" , offvalue="", command=cbx14)
e_cbx_sub_14.deselect()
e_cbx_sub_14.grid(row=3, column=2, padx=5 ,pady=5)

def cbx15():
    if e_cbx_sub_15.select:
        sub15.configure(text= e_sub_var15.get())
    else:
        sub15.configure(text= "")
e_cbx_sub_15 = Checkbutton(subject_edit_scrollframe_edit, text = "CHEMISTRY", variable=e_sub_var15, onvalue="CHEMISTRY" , offvalue="", command=cbx15)
e_cbx_sub_15.deselect()
e_cbx_sub_15.grid(row=4, column=2, padx=5 ,pady=5)

def cbx16():
    if e_cbx_sub_16.select:
        sub16.configure(text= e_sub_var16.get())
    else:
        sub16.configure(text= "")
e_cbx_sub_16 = Checkbutton(subject_edit_scrollframe_edit, text = "PHYSICS", variable=e_sub_var16 , onvalue="PHYSICS" , offvalue="", command=cbx16)
e_cbx_sub_16.deselect()
e_cbx_sub_16.grid(row=0, column=3, padx=5 ,pady=5)

def cbx17():
    if e_cbx_sub_17.select:
        sub17.configure(text= e_sub_var17.get())
    else:
        sub17.configure(text= "")
e_cbx_sub_17 = Checkbutton(subject_edit_scrollframe_edit, text = "BIOLOGY", variable=e_sub_var17 , onvalue="BIOLOGY" , offvalue="", command = cbx17)
e_cbx_sub_17.deselect()
e_cbx_sub_17.grid(row=1, column=3, padx=5 ,pady=5)

def cbx18():
    if e_cbx_sub_18.select:
        sub18.configure(text= e_sub_var18.get())
    else:
        sub18.configure(text= "")
e_cbx_sub_18 = Checkbutton(subject_edit_scrollframe_edit, text = "CIVIC", variable=e_sub_var18 , onvalue="CIVIC" , offvalue="",command= cbx18)
e_cbx_sub_18.deselect()
e_cbx_sub_18.grid(row=2, column=3, padx=5 ,pady=5)

def cbx19():
    if e_cbx_sub_19.select:
        sub19.configure(text= e_sub_var19.get())
    else:
        sub19.configure(text= "")
e_cbx_sub_19 = Checkbutton(subject_edit_scrollframe_edit, text = "C.R.S", variable=e_sub_var19 , onvalue="C.R.S", offvalue="", command= cbx19 )
e_cbx_sub_19.deselect()
e_cbx_sub_19.grid(row=3, column=3, padx=5 ,pady=5)

def cbx20():
    if e_cbx_sub_20.select:
        sub20.configure(text= e_sub_var20.get())
    else:
        sub20.configure(text= "")
e_cbx_sub_20 = Checkbutton(subject_edit_scrollframe_edit, text = "I.C.T", variable=e_sub_var20 , onvalue="I.C.T", offvalue="",command= cbx20 )
e_cbx_sub_20.deselect()
e_cbx_sub_20.grid(row=4, column=3, padx=5 ,pady=5)

   
chk_frame1 = customtkinter.CTkFrame(main_course_edit_frame, fg_color="white", corner_radius=5)
chk_frame1.grid(row=9,column=0, columnspan=2, pady= 10)

def e_sub_exit():
    search_edit_sub.delete(0,END)
    txt_full_name_edit_sub.delete(0,END)
    txt_class_level_edit_sub.delete(0,END)
    txt_class_edit_sub.delete(0,END)
    txt_gender_edit_sub.delete(0,END)
    txt_age_edit_sub.delete(0,END)
    txt_stud_id_edit_sub.delete(0,END)
    sub1.configure(text="")
    sub2.configure(text="")
    sub3.configure(text="")
    sub4.configure(text="")
    sub5.configure(text="")
    sub6.configure(text="")
    sub7.configure(text="")
    sub8.configure(text="")
    sub9.configure(text="")
    sub10.configure(text="")
    sub11.configure(text="")
    sub12.configure(text="")
    sub13.configure(text="")
    sub14.configure(text="")
    sub15.configure(text="")
    sub16.configure(text="")
    sub17.configure(text="")
    sub18.configure(text="")
    sub19.configure(text="")
    sub20.configure(text="")
    e_cbx_sub_1.deselect()
    e_cbx_sub_2.deselect()
    e_cbx_sub_3.deselect()
    e_cbx_sub_4.deselect()
    e_cbx_sub_5.deselect()
    e_cbx_sub_6.deselect()
    e_cbx_sub_7.deselect()
    e_cbx_sub_8.deselect()
    e_cbx_sub_9.deselect()
    e_cbx_sub_10.deselect()
    e_cbx_sub_11.deselect()
    e_cbx_sub_12.deselect()
    e_cbx_sub_13.deselect()
    e_cbx_sub_14.deselect()
    e_cbx_sub_15.deselect()
    e_cbx_sub_16.deselect()
    e_cbx_sub_17.deselect()
    e_cbx_sub_18.deselect()
    e_cbx_sub_19.deselect()
    e_cbx_sub_20.deselect()
    hide_frame()


def e_sub_update():
    sub_rec_id = search_edit_sub.get()
    conn = sqlite3.connect('student management system.db')
    
    c = conn.cursor()
    
     
    c.execute("""UPDATE subjects SET
              full_name = :full_name,
              class_level = :class_level,
              class = :class,
              gender = :gender,
              age = :age,
              student_id = :student_id,
              subject1 = :subject1,
              subject2 = :subject2,
              subject3 = :subject3,
              subject4 = :subject4,
              subject5 = :subject5,
              subject6 = :subject6,
              subject7 = :subject7,
              subject8 = :subject8,
              subject9 = :subject9,
              subject10 = :subject10,
              subject11 = :subject11,
              subject12 = :subject12,
              subject13 = :subject13,
              subject14 = :subject14,
              subject15 = :subject15,
              subject16 = :subject16,
              subject17 = :subject17,
              subject18 = :subject18,
              subject19 = :subject19,
              subject20 = :subject20
              
              WHERE student_id = :student_id""",
              
              {
                  'full_name': txt_full_name_edit_sub.get(),
                  'class_level': txt_class_level_edit_sub.get(),
                  'class': txt_class_edit_sub.get(),
                  'gender': txt_gender_edit_sub.get(),
                  'age' : txt_age_edit_sub.get(),
                  'student_id' : txt_stud_id_edit_sub.get(),
                  
                  'subject1' : e_sub_var1.get(),
                  'subject2' : e_sub_var2.get(),
                  'subject3' : e_sub_var3.get(),
                  'subject4' : e_sub_var4.get(),
                  'subject5' : e_sub_var5.get(),
                  'subject6' : e_sub_var6.get(),
                  'subject7' : e_sub_var7.get(),
                  'subject8' : e_sub_var8.get(),
                  'subject9' : e_sub_var9.get(),
                  'subject10' : e_sub_var10.get(),
                  'subject11' : e_sub_var11.get(),
                  'subject12' : e_sub_var12.get(),
                  'subject13' : e_sub_var13.get(),
                  'subject14' : e_sub_var14.get(),
                  'subject15' : e_sub_var15.get(),
                  'subject16' : e_sub_var16.get(),
                  'subject17' : e_sub_var17.get(),
                  'subject18' : e_sub_var18.get(),
                  'subject19' : e_sub_var19.get(),
                  'subject20' : e_sub_var20.get(), 
                #   m'oid' : sub_rec_id
              }
              )
    
    conn.commit()
    conn.close()
    messagebox.showinfo("INFO", "Table Updated Successfully")
    search_edit_sub.delete(0,END)
    txt_full_name_edit_sub.delete(0,END)
    txt_class_level_edit_sub.delete(0,END)
    txt_class_edit_sub.delete(0,END)
    txt_gender_edit_sub.delete(0,END)
    txt_age_edit_sub.delete(0,END)
    txt_stud_id_edit_sub.delete(0,END)
    sub1.configure(text="")
    sub2.configure(text="")
    sub3.configure(text="")
    sub4.configure(text="")
    sub5.configure(text="")
    sub6.configure(text="")
    sub7.configure(text="")
    sub8.configure(text="")
    sub9.configure(text="")
    sub10.configure(text="")
    sub11.configure(text="")
    sub12.configure(text="")
    sub13.configure(text="")
    sub14.configure(text="")
    sub15.configure(text="")
    sub16.configure(text="")
    sub17.configure(text="")
    sub18.configure(text="")
    sub19.configure(text="")
    sub20.configure(text="")
    e_cbx_sub_1.deselect()
    e_cbx_sub_2.deselect()
    e_cbx_sub_3.deselect()
    e_cbx_sub_4.deselect()
    e_cbx_sub_5.deselect()
    e_cbx_sub_6.deselect()
    e_cbx_sub_7.deselect()
    e_cbx_sub_8.deselect()
    e_cbx_sub_9.deselect()
    e_cbx_sub_10.deselect()
    e_cbx_sub_11.deselect()
    e_cbx_sub_12.deselect()
    e_cbx_sub_13.deselect()
    e_cbx_sub_14.deselect()
    e_cbx_sub_15.deselect()
    e_cbx_sub_16.deselect()
    e_cbx_sub_17.deselect()
    e_cbx_sub_18.deselect()
    e_cbx_sub_19.deselect()
    e_cbx_sub_20.deselect()


btn_subject_update = customtkinter.CTkButton(chk_frame1, text="UPDATE",font=("cambria",12), fg_color="white",bg_color="white", text_color="black",width=20 , height=20, corner_radius=8, hover_color="green", command = e_sub_update)
btn_subject_update.grid(row = 0,column=0, padx=5)
btn_subject_exit_edit = customtkinter.CTkButton(chk_frame1, text="EXIT",font=("cambria",12), fg_color="white",bg_color="white", text_color="black",width=20 , height=20, corner_radius=8, hover_color="red", command = e_sub_exit)
btn_subject_exit_edit.grid(row = 0,column=1,padx = 5)

# ____________________________________ RESULT MENU______________________________________________________

up_frame = LabelFrame(result_upload_frame,text="UPLOAD RESULT",width=200 ,background="gray",foreground="cyan")
up_frame.pack(pady=20)

# lbl_Stud_reg2 = Label(up_frame, text=, font=("arial black", 12),bg="gray", fg='cyan')
# lbl_Stud_reg2.grid(row=0, column=0)

search_upload_frame = LabelFrame(up_frame,text="STUDENT RECORD", bg="gray",fg="cyan")
search_upload_frame.grid(row=0, column=0)
stud_info_frame = LabelFrame(up_frame,text="INFO FRAME",bg="gray",fg="cyan")
stud_info_frame.grid(row=1, column=0)
course_frame = LabelFrame(up_frame,bg="gray",text="FIRST TERM", fg="cyan")
course_frame.grid_forget()
course_frame1 = LabelFrame(up_frame,bg="gray",text="SECOND TERM",fg="cyan")
course_frame1.grid_forget()
course_frame2 = LabelFrame(up_frame,bg="gray",text="THIRD TERM",fg="cyan")
course_frame2.grid_forget()

verification_frame = LabelFrame(up_frame,bg="gray")
verification_frame.grid(row=4, column=0, pady=5)

def r_cal():
    if opt_term.get() == "FIRST TERM":
        a = int(test_course_subject1.get()) + int(exam_course_subject1.get())
        total_course_subject1.delete(0,END)
        total_course_subject1.insert(0,a)
        if  int(total_course_subject1.get()) > 0 and int(total_course_subject1.get()) <= 39:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"F")
            point_course_subject1.insert(0,0)
            
        elif  (int(total_course_subject1.get()) > 40 and int(total_course_subject1.get()) <= 49):
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"E")    
            point_course_subject1.insert(0,1)
            
        elif  int(total_course_subject1.get()) > 49 and int(total_course_subject1.get()) <= 59:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"D")
            point_course_subject1.insert(0,2)
            
        elif  int(total_course_subject1.get()) > 59 and int(total_course_subject1.get()) <= 69:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"c")
            point_course_subject1.insert(0,3)
            
        elif  int(total_course_subject1.get()) > 69 and int(total_course_subject1.get()) <= 79:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"B")
            point_course_subject1.insert(0,4)
            
        elif  int(total_course_subject1.get()) > 79 and int(total_course_subject1.get()) <= 89:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"A")
            point_course_subject1.insert(0,5)
            
        elif  int(total_course_subject1.get()) > 89:
            grade_course_subject1.delete(0,END)
            point_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"A+")
            point_course_subject1.insert(0,6)
                        
        b = int(test_course_subject2.get()) + int(exam_course_subject2.get())
        total_course_subject2.delete(0,END)
        total_course_subject2.insert(0,b)
        if  int(total_course_subject2.get()) > 0 and int(total_course_subject2.get()) <= 39:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"F")
            point_course_subject2.insert(0,0)
            
        elif  int(total_course_subject2.get()) > 39 and int(total_course_subject2.get()) <= 49:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"E")    
            point_course_subject2.insert(0,1)
        
        elif  int(total_course_subject2.get()) > 49 and int(total_course_subject2.get()) <= 59:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"D")
            point_course_subject2.insert(0,2)
            
        elif  int(total_course_subject2.get()) > 59 and int(total_course_subject2.get()) <= 69:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"C")
            point_course_subject2.insert(0,3)
            
        elif  int(total_course_subject2.get()) > 69 and int(total_course_subject2.get()) <= 79:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"B")
            point_course_subject2.insert(0,4)
            
        elif  int(total_course_subject2.get()) > 79 and int(total_course_subject2.get()) <= 89:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"A")
            point_course_subject2.insert(0,5)
            
        elif  int(total_course_subject2.get()) > 89:
            grade_course_subject2.delete(0,END)
            point_course_subject2.delete(0,END)
            grade_course_subject2.insert(0,"A+")
            point_course_subject2.insert(0,6)
            
        
        c = int(test_course_subject3.get()) + int(exam_course_subject3.get())
        total_course_subject3.delete(0,END)
        total_course_subject3.insert(0,c)
        if  int(total_course_subject3.get()) > 0 and int(total_course_subject3.get()) <= 39:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"F")
            point_course_subject3.insert(0,0)
            
        elif  int(total_course_subject3.get()) > 39 and int(total_course_subject3.get()) <= 49:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"E")
            point_course_subject3.insert(0,1)    
        
        elif  int(total_course_subject3.get()) > 49 and int(total_course_subject3.get()) <= 59:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"D")
            point_course_subject3.insert(0,2)
            
        elif  int(total_course_subject3.get()) > 59 and int(total_course_subject3.get()) <= 69:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"C")
            point_course_subject3.insert(0,3)
            
        elif  int(total_course_subject3.get()) > 69 and int(total_course_subject3.get()) <= 79:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"B")
            point_course_subject3.insert(0,4)
            
        elif  int(total_course_subject3.get()) > 79 and int(total_course_subject3.get()) <= 89:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"A")
            point_course_subject3.insert(0,5)
            
        elif  int(total_course_subject3.get()) > 89:
            grade_course_subject3.delete(0,END)
            point_course_subject3.delete(0,END)
            grade_course_subject3.insert(0,"A+")
            point_course_subject3.insert(0,6)
        
        d = int(test_course_subject4.get()) + int(exam_course_subject4.get())
        total_course_subject4.delete(0,END)
        total_course_subject4.insert(0,d)
        if  int(total_course_subject4.get()) > 0 and int(total_course_subject4.get()) <= 39:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"F")
            point_course_subject4.insert(0,0)
            
        elif  int(total_course_subject4.get()) > 39 and int(total_course_subject4.get()) <= 49:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"E")    
            point_course_subject4.insert(0,1)
        
        elif  int(total_course_subject4.get()) > 49 and int(total_course_subject4.get()) <= 59:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"D")
            point_course_subject4.insert(0,2)
                        
        elif  int(total_course_subject4.get()) > 59 and int(total_course_subject4.get()) <= 69:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"C")
            point_course_subject4.insert(0,3)
            
        elif  int(total_course_subject4.get()) > 69 and int(total_course_subject4.get()) <= 79:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"B")
            point_course_subject4.insert(0,4)
            
        elif  int(total_course_subject4.get()) > 79 and int(total_course_subject4.get()) <= 89:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"A")
            point_course_subject4.insert(0,5)
            
        elif  int(total_course_subject4.get()) > 89:
            grade_course_subject4.delete(0,END)
            point_course_subject4.delete(0,END)
            grade_course_subject4.insert(0,"A+")
            point_course_subject4.insert(0,6)
            
        
        e = int(test_course_subject5.get()) + int(exam_course_subject5.get())
        total_course_subject5.delete(0,END)
        total_course_subject5.insert(0,e)
        if  int(total_course_subject5.get()) > 0 and int(total_course_subject5.get()) <= 39:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"F")
            point_course_subject5.insert(0,0)
            
        elif  int(total_course_subject5.get()) > 39 and int(total_course_subject5.get()) <= 49:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"E")
            point_course_subject5.insert(0,1)    
        
        elif  int(total_course_subject5.get()) > 49 and int(total_course_subject5.get()) <= 59:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"D")
            point_course_subject5.insert(0,2)
            
        elif  int(total_course_subject5.get()) > 59 and int(total_course_subject5.get()) <= 69:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"C")
            point_course_subject5.insert(0,3)
            
        elif  int(total_course_subject5.get()) > 69 and int(total_course_subject5.get()) <= 79:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"B")
            point_course_subject5.insert(0,4)
            
        elif  int(total_course_subject5.get()) > 79 and int(total_course_subject5.get()) <= 89:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"A")
            point_course_subject5.insert(0,5)
            
        elif  int(total_course_subject5.get()) > 89:
            grade_course_subject5.delete(0,END)
            point_course_subject5.delete(0,END)
            grade_course_subject5.insert(0,"A+")
            point_course_subject5.insert(0,6)
            
        
        f = int(test_course_subject6.get()) + int(exam_course_subject6.get())
        total_course_subject6.delete(0,END)
        total_course_subject6.insert(0,f)
        if  int(total_course_subject6.get()) > 0 and int(total_course_subject6.get()) <= 39:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"F")
            point_course_subject6.insert(0,0)
            
        elif  int(total_course_subject6.get()) > 39 and int(total_course_subject6.get()) <= 49:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"E")
            point_course_subject6.insert(0,1)    
        
        elif  int(total_course_subject6.get()) > 49 and int(total_course_subject6.get()) <= 59:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"D")
            point_course_subject6.insert(0,2)
            
        elif  int(total_course_subject6.get()) > 59 and int(total_course_subject6.get()) <= 69:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"C")
            point_course_subject6.insert(0,3)
            
        elif  int(total_course_subject6.get()) > 69 and int(total_course_subject6.get()) <= 79:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"B")
            point_course_subject6.delete(0,4)
            
        elif  int(total_course_subject1.get()) > 79 and int(total_course_subject1.get()) <= 89:
            grade_course_subject1.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject1.insert(0,"A")
            point_course_subject6.insert(0,5)
            
        elif  int(total_course_subject6.get()) > 89:
            grade_course_subject6.delete(0,END)
            point_course_subject6.delete(0,END)
            grade_course_subject6.insert(0,"A+")
            point_course_subject6.delete(0,6)
            
        
        g = int(test_course_subject7.get()) + int(exam_course_subject7.get())
        total_course_subject7.delete(0,END)
        total_course_subject7.insert(0,g)
        if  int(total_course_subject7.get()) > 0 and int(total_course_subject7.get()) <= 39:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"F9")
            
        elif  int(total_course_subject7.get()) > 39 and int(total_course_subject7.get()) <= 45:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"E8")    
        
        elif  int(total_course_subject7.get()) > 45 and int(total_course_subject7.get()) <= 49:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"D7")
            
        elif  int(total_course_subject7.get()) > 49 and int(total_course_subject7.get()) <= 55:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"D7")
            
        elif  int(total_course_subject7.get()) > 55 and int(total_course_subject7.get()) <= 59:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"C6")
            
        elif  int(total_course_subject7.get()) > 59 and int(total_course_subject7.get()) <= 65:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"C4")
            
        elif  int(total_course_subject7.get()) > 65 and int(total_course_subject7.get()) <= 69:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"B3")
            
        elif  int(total_course_subject7.get()) > 69 and int(total_course_subject7.get()) <= 75:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"B3")
            
        elif  int(total_course_subject7.get()) > 75 and int(total_course_subject7.get()) <= 79:
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"B2")
            
        elif  int(total_course_subject7.get()) > 79 :
            grade_course_subject7.delete(0,END)
            grade_course_subject7.insert(0,"A1")
        
        h = int(test_course_subject8.get()) + int(exam_course_subject8.get())
        total_course_subject8.delete(0,END)
        total_course_subject8.insert(0,h)
        if  int(total_course_subject8.get()) > 0 and int(total_course_subject8.get()) <= 39:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"F9")
            
        elif  int(total_course_subject8.get()) > 39 and int(total_course_subject8.get()) <= 45:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"E8")    
        
        elif  int(total_course_subject8.get()) > 45 and int(total_course_subject8.get()) <= 49:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"D7")
            
        elif  int(total_course_subject8.get()) > 49 and int(total_course_subject8.get()) <= 55:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"D7")
            
        elif  int(total_course_subject8.get()) > 55 and int(total_course_subject8.get()) <= 59:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"C6")
            
        elif  int(total_course_subject8.get()) > 59 and int(total_course_subject8.get()) <= 65:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"C4")
            
        elif  int(total_course_subject8.get()) > 65 and int(total_course_subject8.get()) <= 69:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"B3")
            
        elif  int(total_course_subject8.get()) > 69 and int(total_course_subject8.get()) <= 75:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"B3")
            
        elif  int(total_course_subject8.get()) > 75 and int(total_course_subject8.get()) <= 79:
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"B2")
            
        elif  int(total_course_subject8.get()) > 79 :
            grade_course_subject8.delete(0,END)
            grade_course_subject8.insert(0,"A1")

        i = int(test_course_subject9.get()) + int(exam_course_subject9.get())
        total_course_subject9.delete(0,END)
        total_course_subject9.insert(0,i)
        if  int(total_course_subject9.get()) > 0 and int(total_course_subject9.get()) <= 39:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"F9")
            
        elif  int(total_course_subject9.get()) > 39 and int(total_course_subject9.get()) <= 45:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"E8")    
        
        elif  int(total_course_subject9.get()) > 45 and int(total_course_subject9.get()) <= 49:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"D7")
            
        elif  int(total_course_subject9.get()) > 49 and int(total_course_subject9.get()) <= 55:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"D7")
            
        elif  int(total_course_subject9.get()) > 55 and int(total_course_subject9.get()) <= 59:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"C6")
            
        elif  int(total_course_subject9.get()) > 59 and int(total_course_subject9.get()) <= 65:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"C4")
            
        elif  int(total_course_subject9.get()) > 65 and int(total_course_subject9.get()) <= 69:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"B3")
            
        elif  int(total_course_subject9.get()) > 69 and int(total_course_subject9.get()) <= 75:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"B3")
            
        elif  int(total_course_subject9.get()) > 75 and int(total_course_subject9.get()) <= 79:
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"B2")
            
        elif  int(total_course_subject9.get()) > 79 :
            grade_course_subject9.delete(0,END)
            grade_course_subject9.insert(0,"A1")
        
        j = int(test_course_subject10.get()) + int(exam_course_subject10.get())
        total_course_subject10.delete(0,END)
        total_course_subject10.insert(0,j)
        if  int(total_course_subject10.get()) > 0 and int(total_course_subject10.get()) <= 39:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"F9")
            
        elif  int(total_course_subject10.get()) > 39 and int(total_course_subject10.get()) <= 45:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"E8")    
        
        elif  int(total_course_subject10.get()) > 45 and int(total_course_subject10.get()) <= 49:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"D7")
            
        elif  int(total_course_subject10.get()) > 49 and int(total_course_subject10.get()) <= 55:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"D7")
            
        elif  int(total_course_subject10.get()) > 55 and int(total_course_subject10.get()) <= 59:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"C6")
            
        elif  int(total_course_subject10.get()) > 59 and int(total_course_subject10.get()) <= 65:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"C4")
            
        elif  int(total_course_subject10.get()) > 65 and int(total_course_subject10.get()) <= 69:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"B3")
            
        elif  int(total_course_subject10.get()) > 69 and int(total_course_subject10.get()) <= 75:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"B3")
            
        elif  int(total_course_subject10.get()) > 75 and int(total_course_subject10.get()) <= 79:
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"B2")
            
        elif  int(total_course_subject10.get()) > 79 :
            grade_course_subject10.delete(0,END)
            grade_course_subject10.insert(0,"A1")
        
        k = int(test_course_subject11.get()) + int(exam_course_subject11.get())
        total_course_subject11.delete(0,END)
        total_course_subject11.insert(0,k)
        if  int(total_course_subject11.get()) > 0 and int(total_course_subject11.get()) <= 39:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"F9")
            
        elif  int(total_course_subject11.get()) > 39 and int(total_course_subject11.get()) <= 45:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"E8")    
        
        elif  int(total_course_subject11.get()) > 45 and int(total_course_subject11.get()) <= 49:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"D7")
            
        elif  int(total_course_subject11.get()) > 49 and int(total_course_subject11.get()) <= 55:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"D7")
            
        elif  int(total_course_subject11.get()) > 55 and int(total_course_subject11.get()) <= 59:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"C6")
            
        elif  int(total_course_subject11.get()) > 59 and int(total_course_subject11.get()) <= 65:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"C4")
            
        elif  int(total_course_subject11.get()) > 65 and int(total_course_subject11.get()) <= 69:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"B3")
            
        elif  int(total_course_subject11.get()) > 69 and int(total_course_subject11.get()) <= 75:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"B3")
            
        elif  int(total_course_subject11.get()) > 75 and int(total_course_subject11.get()) <= 79:
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"B2")
            
        elif  int(total_course_subject11.get()) > 79 :
            grade_course_subject11.delete(0,END)
            grade_course_subject11.insert(0,"A1")
        
        l = int(test_course_subject12.get()) + int(exam_course_subject12.get())
        total_course_subject12.delete(0,END)
        total_course_subject12.insert(0,l)
        if  int(total_course_subject12.get()) > 0 and int(total_course_subject12.get()) <= 39:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"F9")
            
        elif  int(total_course_subject12.get()) > 39 and int(total_course_subject12.get()) <= 45:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"E8")    
        
        elif  int(total_course_subject12.get()) > 45 and int(total_course_subject12.get()) <= 49:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"D7")
            
        elif  int(total_course_subject12.get()) > 49 and int(total_course_subject12.get()) <= 55:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"D7")
            
        elif  int(total_course_subject12.get()) > 55 and int(total_course_subject12.get()) <= 59:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"C6")
            
        elif  int(total_course_subject12.get()) > 59 and int(total_course_subject12.get()) <= 65:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"C4")
            
        elif  int(total_course_subject12.get()) > 65 and int(total_course_subject12.get()) <= 69:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"B3")
            
        elif  int(total_course_subject12.get()) > 69 and int(total_course_subject12.get()) <= 75:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"B3")
            
        elif  int(total_course_subject12.get()) > 75 and int(total_course_subject12.get()) <= 79:
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"B2")
            
        elif  int(total_course_subject12.get()) > 79 :
            grade_course_subject12.delete(0,END)
            grade_course_subject12.insert(0,"A1")

        m = int(test_course_subject13.get()) + int(exam_course_subject13.get())
        total_course_subject13.delete(0,END)
        total_course_subject13.insert(0,m)
        if  int(total_course_subject13.get()) > 0 and int(total_course_subject13.get()) <= 39:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"F9")
            
        elif  int(total_course_subject13.get()) > 39 and int(total_course_subject13.get()) <= 45:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"E8")    
        
        elif  int(total_course_subject13.get()) > 45 and int(total_course_subject13.get()) <= 49:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"D7")
            
        elif  int(total_course_subject13.get()) > 49 and int(total_course_subject13.get()) <= 55:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"D7")
            
        elif  int(total_course_subject1.get()) > 55 and int(total_course_subject1.get()) <= 59:
            grade_course_subject1.delete(0,END)
            grade_course_subject1.insert(0,"C6")
            
        elif  int(total_course_subject13.get()) > 59 and int(total_course_subject13.get()) <= 65:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"C4")
            
        elif  int(total_course_subject13.get()) > 65 and int(total_course_subject13.get()) <= 69:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"B3")
            
        elif  int(total_course_subject13.get()) > 69 and int(total_course_subject13.get()) <= 75:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"B3")
            
        elif  int(total_course_subject13.get()) > 75 and int(total_course_subject13.get()) <= 79:
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"B2")
            
        elif  int(total_course_subject13.get()) > 79 :
            grade_course_subject13.delete(0,END)
            grade_course_subject13.insert(0,"A1")
        
        n = int(test_course_subject14.get()) + int(exam_course_subject14.get())
        total_course_subject14.delete(0,END)
        total_course_subject14.insert(0,n)
        if  int(total_course_subject14.get()) > 0 and int(total_course_subject14.get()) <= 39:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"F9")
            
        elif  int(total_course_subject14.get()) > 39 and int(total_course_subject14.get()) <= 45:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"E8")    
        
        elif  int(total_course_subject14.get()) > 45 and int(total_course_subject14.get()) <= 49:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"D7")
            
        elif  int(total_course_subject14.get()) > 49 and int(total_course_subject14.get()) <= 55:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"D7")
           
            
        elif  int(total_course_subject14.get()) > 55 and int(total_course_subject14.get()) <= 59:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"C6")
            
        elif  int(total_course_subject14.get()) > 59 and int(total_course_subject14.get()) <= 65:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"C4")
            
        elif  int(total_course_subject14.get()) > 65 and int(total_course_subject14.get()) <= 69:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"B3")
            
        elif  int(total_course_subject14.get()) > 69 and int(total_course_subject14.get()) <= 75:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"B3")
            
        elif  int(total_course_subject14.get()) > 75 and int(total_course_subject14.get()) <= 79:
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"B2")
            
        elif  int(total_course_subject14.get()) > 79 :
            grade_course_subject14.delete(0,END)
            grade_course_subject14.insert(0,"A1")
        
        o = int(test_course_subject15.get()) + int(exam_course_subject15.get())
        total_course_subject15.delete(0,END)
        total_course_subject15.insert(0,o)
        if  int(total_course_subject15.get()) > 0 and int(total_course_subject15.get()) <= 39:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"F9")
            
        elif  int(total_course_subject15.get()) > 39 and int(total_course_subject15.get()) <= 45:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"E8")    
        
        elif  int(total_course_subject15.get()) > 45 and int(total_course_subject15.get()) <= 49:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"D7")
            
        elif  int(total_course_subject15.get()) > 49 and int(total_course_subject15.get()) <= 55:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"D7")
            
        elif  int(total_course_subject15.get()) > 55 and int(total_course_subject15.get()) <= 59:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"C6")
            
        elif  int(total_course_subject15.get()) > 59 and int(total_course_subject15.get()) <= 65:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"C4")
            
        elif  int(total_course_subject15.get()) > 65 and int(total_course_subject15.get()) <= 69:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"B3")
            
        elif  int(total_course_subject15.get()) > 69 and int(total_course_subject15.get()) <= 75:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"B3")
            
        elif  int(total_course_subject15.get()) > 75 and int(total_course_subject15.get()) <= 79:
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"B2")
            
        elif  int(total_course_subject15.get()) > 79 :
            grade_course_subject15.delete(0,END)
            grade_course_subject15.insert(0,"A1")
        
        p = int(test_course_subject16.get()) + int(exam_course_subject16.get())
        total_course_subject16.delete(0,END)
        total_course_subject16.insert(0,p)
        if  int(total_course_subject16.get()) > 0 and int(total_course_subject16.get()) <= 39:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"F9")
            
        elif  int(total_course_subject16.get()) > 39 and int(total_course_subject16.get()) <= 45:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"E8")    
        
        elif  int(total_course_subject16.get()) > 45 and int(total_course_subject16.get()) <= 49:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"D7")
            
        elif  int(total_course_subject16.get()) > 49 and int(total_course_subject16.get()) <= 55:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"D7")
            
        elif  int(total_course_subject16.get()) > 55 and int(total_course_subject16.get()) <= 59:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"C6")
            
        elif  int(total_course_subject16.get()) > 59 and int(total_course_subject16.get()) <= 65:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"C4")
            
        elif  int(total_course_subject16.get()) > 65 and int(total_course_subject16.get()) <= 69:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"B3")
            
        elif  int(total_course_subject16.get()) > 69 and int(total_course_subject16.get()) <= 75:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"B3")
            
        elif  int(total_course_subject16.get()) > 75 and int(total_course_subject16.get()) <= 79:
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"B2")
            
        elif  int(total_course_subject16.get()) > 79 :
            grade_course_subject16.delete(0,END)
            grade_course_subject16.insert(0,"A1")

        q = int(test_course_subject17.get()) + int(exam_course_subject17.get())
        total_course_subject17.delete(0,END)
        total_course_subject17.insert(0,q)
        if  int(total_course_subject17.get()) > 0 and int(total_course_subject17.get()) <= 39:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"F9")
            
        elif  int(total_course_subject17.get()) > 39 and int(total_course_subject17.get()) <= 45:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"E8")    
        
        elif  int(total_course_subject17.get()) > 45 and int(total_course_subject17.get()) <= 49:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"D7")
            
        elif  int(total_course_subject17.get()) > 49 and int(total_course_subject17.get()) <= 55:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"D7")
            
        elif  int(total_course_subject17.get()) > 55 and int(total_course_subject17.get()) <= 59:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"C6")
            
        elif  int(total_course_subject17.get()) > 59 and int(total_course_subject17.get()) <= 65:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"C4")
            
        elif  int(total_course_subject17.get()) > 65 and int(total_course_subject17.get()) <= 69:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"B3")
            
        elif  int(total_course_subject17.get()) > 69 and int(total_course_subject17.get()) <= 75:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"B3")
            
        elif  int(total_course_subject17.get()) > 75 and int(total_course_subject17.get()) <= 79:
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"B2")
            
        elif  int(total_course_subject17.get()) > 79 :
            grade_course_subject17.delete(0,END)
            grade_course_subject17.insert(0,"A1")
        
        r = int(test_course_subject18.get()) + int(exam_course_subject18.get())
        total_course_subject18.delete(0,END)
        total_course_subject18.insert(0,r)
        if  int(total_course_subject18.get()) > 0 and int(total_course_subject18.get()) <= 39:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"F9")
            
        elif  int(total_course_subject18.get()) > 39 and int(total_course_subject18.get()) <= 45:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"E8")    
        
        elif  int(total_course_subject18.get()) > 45 and int(total_course_subject18.get()) <= 49:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"D7")
            
        elif  int(total_course_subject18.get()) > 49 and int(total_course_subject18.get()) <= 55:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"D7")
            
        elif  int(total_course_subject18.get()) > 55 and int(total_course_subject18.get()) <= 59:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"C6")
            
        elif  int(total_course_subject18.get()) > 59 and int(total_course_subject18.get()) <= 65:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"C4")
            
        elif  int(total_course_subject18.get()) > 65 and int(total_course_subject18.get()) <= 69:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"B3")
            
        elif  int(total_course_subject18.get()) > 69 and int(total_course_subject18.get()) <= 75:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"B3")
            
        elif  int(total_course_subject18.get()) > 75 and int(total_course_subject18.get()) <= 79:
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"B2")
            
        elif  int(total_course_subject18 .get()) > 79 :
            grade_course_subject18.delete(0,END)
            grade_course_subject18.insert(0,"A1")
        
        s = int(test_course_subject19.get()) + int(exam_course_subject19.get())
        total_course_subject19.delete(0,END)
        total_course_subject19.insert(0,s)
        if  int(total_course_subject19.get()) > 0 and int(total_course_subject19.get()) <= 39:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"F9")
            
        elif  int(total_course_subject19.get()) > 39 and int(total_course_subject19.get()) <= 45:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"E8")    
        
        elif  int(total_course_subject19.get()) > 45 and int(total_course_subject19.get()) <= 49:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"D7")
            
        elif  int(total_course_subject19.get()) > 49 and int(total_course_subject19.get()) <= 55:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"D7")
            
        elif  int(total_course_subject19.get()) > 55 and int(total_course_subject19.get()) <= 59:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"C6")
            
        elif  int(total_course_subject19.get()) > 59 and int(total_course_subject19.get()) <= 65:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"C4")
            
        elif  int(total_course_subject19.get()) > 65 and int(total_course_subject19.get()) <= 69:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"B3")
            
        elif  int(total_course_subject19.get()) > 69 and int(total_course_subject19.get()) <= 75:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"B3")
            
        elif  int(total_course_subject19.get()) > 75 and int(total_course_subject19.get()) <= 79:
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"B2")
            
        elif  int(total_course_subject19.get()) > 79 :
            grade_course_subject19.delete(0,END)
            grade_course_subject19.insert(0,"A1")
        
        t = int(test_course_subject20.get()) + int(exam_course_subject20.get())
        total_course_subject20.delete(0,END)
        total_course_subject20.insert(0,t)
        if  int(total_course_subject20.get()) > 0 and int(total_course_subject20.get()) <= 39:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"F9")
            
        elif  int(total_course_subject20.get()) > 39 and int(total_course_subject20.get()) <= 45:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"E8")    
        
        elif  int(total_course_subject20.get()) > 45 and int(total_course_subject20.get()) <= 49:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"D7")
            
        elif  int(total_course_subject20.get()) > 49 and int(total_course_subject20.get()) <= 55:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"D7")
            
        elif  int(total_course_subject20.get()) > 55 and int(total_course_subject20.get()) <= 59:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"C6")
            
        elif  int(total_course_subject20.get()) > 59 and int(total_course_subject20.get()) <= 65:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"C4")
            
        elif  int(total_course_subject20.get()) > 65 and int(total_course_subject20.get()) <= 69:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"B3")
            
        elif  int(total_course_subject20.get()) > 69 and int(total_course_subject20.get()) <= 75:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"B3")
            
        elif  int(total_course_subject20.get()) > 75 and int(total_course_subject20.get()) <= 79:
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"B2")
            
        elif  int(total_course_subject20.get()) > 79 :
            grade_course_subject20.delete(0,END)
            grade_course_subject20.insert(0,"A1")
    
    elif opt_term.get() == "SECOND TERM":
            a2 = int(test_sub_subject1.get()) + int(exam_sub_subject1.get())
            total_sub_subject1.delete(0,END)
            total_sub_subject1.insert(0,a2)
            if  int(total_sub_subject1.get()) > 0 and int(total_sub_subject1.get()) <= 39:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"F9")
                
            elif  int(total_sub_subject1.get()) > 39 and int(total_sub_subject1.get()) <= 45:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"E8")    
            
            elif  int(total_sub_subject1.get()) > 45 and int(total_sub_subject1.get()) <= 49:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"D7")
                
            elif  int(total_sub_subject1.get()) > 49 and int(total_sub_subject1.get()) <= 55:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"D7")
                
            elif  int(total_sub_subject1.get()) > 55 and int(total_sub_subject1.get()) <= 59:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"C6")
                
            elif  int(total_sub_subject1.get()) > 59 and int(total_sub_subject1.get()) <= 65:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"C4")
                
            elif  int(total_sub_subject1.get()) > 65 and int(total_sub_subject1.get()) <= 69:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"B3")
                
            elif  int(total_sub_subject1.get()) > 69 and int(total_sub_subject1.get()) <= 75:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"B3")
                
            elif  int(total_sub_subject1.get()) > 75 and int(total_sub_subject1.get()) <= 79:
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"B2")
                
            elif  int(total_sub_subject1.get()) > 79 :
                grade_sub_subject1.delete(0,END)
                grade_sub_subject1.insert(0,"A1")
            
                        
            b2 = int(test_sub_subject2.get()) + int(exam_sub_subject2.get())
            total_sub_subject2.delete(0,END)
            total_sub_subject2.insert(0,b2)
            if  int(total_sub_subject2.get()) > 0 and int(total_sub_subject2.get()) <= 39:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"F9")
                
            elif  int(total_sub_subject2.get()) > 39 and int(total_sub_subject2.get()) <= 45:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"E8")    
            
            elif  int(total_sub_subject2.get()) > 45 and int(total_sub_subject2.get()) <= 49:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"D7")
                
            elif  int(total_sub_subject2.get()) > 49 and int(total_sub_subject2.get()) <= 55:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"D7")
                
            elif  int(total_sub_subject2.get()) > 55 and int(total_sub_subject2.get()) <= 59:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"C6")
                
            elif  int(total_sub_subject2.get()) > 59 and int(total_sub_subject2.get()) <= 65:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"C4")
                
            elif  int(total_sub_subject2.get()) > 65 and int(total_sub_subject2.get()) <= 69:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"B3")
                
            elif  int(total_sub_subject2.get()) > 69 and int(total_sub_subject2.get()) <= 75:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"B3")
                
            elif  int(total_sub_subject2.get()) > 75 and int(total_sub_subject2.get()) <= 79:
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"B2")
                
            elif  int(total_sub_subject2.get()) > 79 :
                grade_sub_subject2.delete(0,END)
                grade_sub_subject2.insert(0,"A1")
            
            
            c2 = int(test_sub_subject3.get()) + int(exam_sub_subject3.get())
            total_sub_subject3.delete(0,END)
            total_sub_subject3.insert(0,c2)
            if  int(total_sub_subject3.get()) > 0 and int(total_sub_subject3.get()) <= 39:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"F9")
                
            elif  int(total_sub_subject3.get()) > 39 and int(total_sub_subject3.get()) <= 45:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"E8")    
            
            elif  int(total_sub_subject3.get()) > 45 and int(total_sub_subject3.get()) <= 49:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"D7")
                
            elif  int(total_sub_subject3.get()) > 49 and int(total_sub_subject3.get()) <= 55:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"D7")
                
            elif  int(total_sub_subject3.get()) > 55 and int(total_sub_subject3.get()) <= 59:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"C6")
                
            elif  int(total_sub_subject3.get()) > 59 and int(total_sub_subject3.get()) <= 65:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"C4")
                
            elif  int(total_sub_subject3.get()) > 65 and int(total_sub_subject3.get()) <= 69:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"B3")
                
            elif  int(total_sub_subject3.get()) > 69 and int(total_sub_subject3.get()) <= 75:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"B3")
                
            elif  int(total_sub_subject3.get()) > 75 and int(total_sub_subject3.get()) <= 79:
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"B2")
                
            elif  int(total_sub_subject3.get()) > 79 :
                grade_sub_subject3.delete(0,END)
                grade_sub_subject3.insert(0,"A1")
            
            
            d2 = int(test_sub_subject4.get()) + int(exam_sub_subject4.get())
            total_sub_subject4.delete(0,END)
            total_sub_subject4.insert(0,d2)
            if  int(total_sub_subject4.get()) > 0 and int(total_sub_subject4.get()) <= 39:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"F9")
                
            elif  int(total_sub_subject4.get()) > 39 and int(total_sub_subject4.get()) <= 45:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"E8")    
            
            elif  int(total_sub_subject4.get()) > 45 and int(total_sub_subject4.get()) <= 49:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"D7")
                
            elif  int(total_sub_subject4.get()) > 49 and int(total_sub_subject4.get()) <= 55:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"D7")
                
            elif  int(total_sub_subject4.get()) > 55 and int(total_sub_subject4.get()) <= 59:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"C6")
                
            elif  int(total_sub_subject4.get()) > 59 and int(total_sub_subject4.get()) <= 65:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"C4")
                
            elif  int(total_sub_subject4.get()) > 65 and int(total_sub_subject4.get()) <= 69:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"B3")
                
            elif  int(total_sub_subject4.get()) > 69 and int(total_sub_subject4.get()) <= 75:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"B3")
                
            elif  int(total_sub_subject4.get()) > 75 and int(total_sub_subject4.get()) <= 79:
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"B2")
                
            elif  int(total_sub_subject4.get()) > 79 :
                grade_sub_subject4.delete(0,END)
                grade_sub_subject4.insert(0,"A1")
            
            
            e2 = int(test_sub_subject5.get()) + int(exam_sub_subject5.get())
            total_sub_subject5.delete(0,END)
            total_sub_subject5.insert(0,e2)
            if  int(total_sub_subject5.get()) > 0 and int(total_sub_subject5.get()) <= 39:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"F9")
                
            elif  int(total_sub_subject5.get()) > 39 and int(total_sub_subject5.get()) <= 45:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"E8")    
            
            elif  int(total_sub_subject5.get()) > 45 and int(total_sub_subject5.get()) <= 49:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"D7")
                
            elif  int(total_sub_subject5.get()) > 49 and int(total_sub_subject5.get()) <= 55:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"D7")
                
            elif  int(total_sub_subject5.get()) > 55 and int(total_sub_subject5.get()) <= 59:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"C6")
                
            elif  int(total_sub_subject5.get()) > 59 and int(total_sub_subject5.get()) <= 65:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"C4")
                
            elif  int(total_sub_subject5.get()) > 65 and int(total_sub_subject5.get()) <= 69:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"B3")
                
            elif  int(total_sub_subject5.get()) > 69 and int(total_sub_subject5.get()) <= 75:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"B3")
                
            elif  int(total_sub_subject5.get()) > 75 and int(total_sub_subject5.get()) <= 79:
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"B2")
                
            elif  int(total_sub_subject5.get()) > 79 :
                grade_sub_subject5.delete(0,END)
                grade_sub_subject5.insert(0,"A1")
            
            
            f2 = int(test_sub_subject6.get()) + int(exam_sub_subject6.get())
            total_sub_subject6.delete(0,END)
            total_sub_subject6.insert(0,f2)
            if  int(total_sub_subject6.get()) > 0 and int(total_sub_subject6.get()) <= 39:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"F9")
                
            elif  int(total_sub_subject6.get()) > 39 and int(total_sub_subject6.get()) <= 45:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"E8")    
            
            elif  int(total_sub_subject6.get()) > 45 and int(total_sub_subject6.get()) <= 49:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"D7")
                
            elif  int(total_sub_subject6.get()) > 49 and int(total_sub_subject6.get()) <= 55:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"D7")
                
            elif  int(total_sub_subject6.get()) > 55 and int(total_sub_subject6.get()) <= 59:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"C6")
                
            elif  int(total_sub_subject6.get()) > 59 and int(total_sub_subject6.get()) <= 65:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"C4")
                
            elif  int(total_sub_subject6.get()) > 65 and int(total_sub_subject6.get()) <= 69:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"B3")
                
            elif  int(total_sub_subject6.get()) > 69 and int(total_sub_subject6.get()) <= 75:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"B3")
                
            elif  int(total_sub_subject6.get()) > 75 and int(total_sub_subject6.get()) <= 79:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"B2")
                
            elif  int(total_sub_subject6.get()) > 79 :
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"A1")
            
            g2 = int(test_sub_subject7.get()) + int(exam_sub_subject7.get())
            total_sub_subject7.delete(0,END)
            total_sub_subject7.insert(0,g2)
            if  int(total_sub_subject7.get()) > 0 and int(total_sub_subject7.get()) <= 39:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"F9")
                
            elif  int(total_sub_subject7.get()) > 39 and int(total_sub_subject7.get()) <= 45:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"E8")    
            
            elif  int(total_sub_subject7.get()) > 45 and int(total_sub_subject7.get()) <= 49:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"D7")
                
            elif  int(total_sub_subject7.get()) > 49 and int(total_sub_subject7.get()) <= 55:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"D7")
                
            elif  int(total_sub_subject7.get()) > 55 and int(total_sub_subject7.get()) <= 59:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"C6")
                
            elif  int(total_sub_subject7.get()) > 59 and int(total_sub_subject7.get()) <= 65:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"C4")
                
            elif  int(total_sub_subject7.get()) > 65 and int(total_sub_subject7.get()) <= 69:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"B3")
                
            elif  int(total_sub_subject7.get()) > 69 and int(total_sub_subject7.get()) <= 75:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"B3")
                
            elif  int(total_sub_subject7.get()) > 75 and int(total_sub_subject7.get()) <= 79:
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"B2")
                
            elif  int(total_sub_subject7.get()) > 79 :
                grade_sub_subject7.delete(0,END)
                grade_sub_subject7.insert(0,"A1")
                
            h2 = int(test_sub_subject8.get()) + int(exam_sub_subject8.get())
            total_sub_subject8.delete(0,END)
            total_sub_subject8.insert(0,h2)
            if  int(total_sub_subject8.get()) > 0 and int(total_sub_subject8.get()) <= 39:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"F9")
                
            elif  int(total_sub_subject8.get()) > 39 and int(total_sub_subject8.get()) <= 45:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"E8")    
            
            elif  int(total_sub_subject8.get()) > 45 and int(total_sub_subject8.get()) <= 49:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"D7")
                
            elif  int(total_sub_subject8.get()) > 49 and int(total_sub_subject8.get()) <= 55:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"D7")
                
            elif  int(total_sub_subject8.get()) > 55 and int(total_sub_subject8.get()) <= 59:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"C6")
                
            elif  int(total_sub_subject8.get()) > 59 and int(total_sub_subject8.get()) <= 65:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"C4")
                
            elif  int(total_sub_subject8.get()) > 65 and int(total_sub_subject8.get()) <= 69:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"B3")
                
            elif  int(total_sub_subject8.get()) > 69 and int(total_sub_subject8.get()) <= 75:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"B3")
                
            elif  int(total_sub_subject8.get()) > 75 and int(total_sub_subject8.get()) <= 79:
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"B2")
                
            elif  int(total_sub_subject8.get()) > 79 :
                grade_sub_subject8.delete(0,END)
                grade_sub_subject8.insert(0,"A1")
                
            i2 = int(test_sub_subject9.get()) + int(exam_sub_subject9.get())
            total_sub_subject9.delete(0,END)
            total_sub_subject9.insert(0,i2)
            if  int(total_sub_subject9.get()) > 0 and int(total_sub_subject9.get()) <= 39:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"F9")
                
            elif  int(total_sub_subject9.get()) > 39 and int(total_sub_subject9.get()) <= 45:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"E8")    
            
            elif  int(total_sub_subject9.get()) > 45 and int(total_sub_subject9.get()) <= 49:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"D7")
                
            elif  int(total_sub_subject9.get()) > 49 and int(total_sub_subject9.get()) <= 55:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"D7")
                
            elif  int(total_sub_subject9.get()) > 55 and int(total_sub_subject9.get()) <= 59:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"C6")
                
            elif  int(total_sub_subject9.get()) > 59 and int(total_sub_subject9.get()) <= 65:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"C4")
                
            elif  int(total_sub_subject9.get()) > 65 and int(total_sub_subject9.get()) <= 69:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"B3")
                
            elif  int(total_sub_subject9.get()) > 69 and int(total_sub_subject9.get()) <= 75:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"B3")
                
            elif  int(total_sub_subject9.get()) > 75 and int(total_sub_subject9.get()) <= 79:
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"B2")
                
            elif  int(total_sub_subject9.get()) > 79 :
                grade_sub_subject9.delete(0,END)
                grade_sub_subject9.insert(0,"A1")
            
            j2 = int(test_sub_subject10.get()) + int(exam_sub_subject10.get())
            total_sub_subject10.delete(0,END)
            total_sub_subject10.insert(0,j2)
            if  int(total_sub_subject10.get()) > 0 and int(total_sub_subject10.get()) <= 39:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"F9")
                
            elif  int(total_sub_subject10.get()) > 39 and int(total_sub_subject10.get()) <= 45:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"E8")    
            
            elif  int(total_sub_subject10.get()) > 45 and int(total_sub_subject10.get()) <= 49:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"D7")
                
            elif  int(total_sub_subject10.get()) > 49 and int(total_sub_subject10.get()) <= 55:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"D7")
                
            elif  int(total_sub_subject10.get()) > 55 and int(total_sub_subject10.get()) <= 59:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"C6")
                
            elif  int(total_sub_subject10.get()) > 59 and int(total_sub_subject10.get()) <= 65:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"C4")
                
            elif  int(total_sub_subject10.get()) > 65 and int(total_sub_subject10.get()) <= 69:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"B3")
                
            elif  int(total_sub_subject10.get()) > 69 and int(total_sub_subject10.get()) <= 75:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"B3")
                
            elif  int(total_sub_subject10.get()) > 75 and int(total_sub_subject10.get()) <= 79:
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"B2")
                
            elif  int(total_sub_subject10.get()) > 79 :
                grade_sub_subject10.delete(0,END)
                grade_sub_subject10.insert(0,"A1")
            
            k2 = int(test_sub_subject11.get()) + int(exam_sub_subject11.get())
            total_sub_subject11.delete(0,END)
            total_sub_subject11.insert(0,k2)
            if  int(total_sub_subject11.get()) > 0 and int(total_sub_subject11.get()) <= 39:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"F9")
                
            elif  int(total_sub_subject11.get()) > 39 and int(total_sub_subject11.get()) <= 45:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"E8")    
            
            elif  int(total_sub_subject11.get()) > 45 and int(total_sub_subject11.get()) <= 49:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"D7")
                
            elif  int(total_sub_subject11.get()) > 49 and int(total_sub_subject11.get()) <= 55:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"D7")
                
            elif  int(total_sub_subject11.get()) > 55 and int(total_sub_subject11.get()) <= 59:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"C6")
                
            elif  int(total_sub_subject11.get()) > 59 and int(total_sub_subject11.get()) <= 65:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"C4")
                
            elif  int(total_sub_subject6.get()) > 65 and int(total_sub_subject6.get()) <= 69:
                grade_sub_subject6.delete(0,END)
                grade_sub_subject6.insert(0,"B3")
                
            elif  int(total_sub_subject11.get()) > 69 and int(total_sub_subject11.get()) <= 75:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"B3")
                
            elif  int(total_sub_subject11.get()) > 75 and int(total_sub_subject11.get()) <= 79:
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"B2")
                
            elif  int(total_sub_subject11.get()) > 79 :
                grade_sub_subject11.delete(0,END)
                grade_sub_subject11.insert(0,"A1")
            
            l2 = int(test_sub_subject12.get()) + int(exam_sub_subject12.get())
            total_sub_subject12.delete(0,END)
            total_sub_subject12.insert(0,l2)
            if  int(total_sub_subject12.get()) > 0 and int(total_sub_subject12.get()) <= 39:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"F9")
                
            elif  int(total_sub_subject12.get()) > 39 and int(total_sub_subject12.get()) <= 45:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"E8")    
            
            elif  int(total_sub_subject12.get()) > 45 and int(total_sub_subject12.get()) <= 49:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"D7")
                
            elif  int(total_sub_subject12.get()) > 49 and int(total_sub_subject12.get()) <= 55:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"D7")
                
            elif  int(total_sub_subject12.get()) > 55 and int(total_sub_subject12.get()) <= 59:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"C6")
                
            elif  int(total_sub_subject12.get()) > 59 and int(total_sub_subject12.get()) <= 65:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"C4")
                
            elif  int(total_sub_subject12.get()) > 65 and int(total_sub_subject12.get()) <= 69:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"B3")
                
            elif  int(total_sub_subject12.get()) > 69 and int(total_sub_subject12.get()) <= 75:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"B3")
                
            elif  int(total_sub_subject12.get()) > 75 and int(total_sub_subject12.get()) <= 79:
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"B2")
                
            elif  int(total_sub_subject12.get()) > 79 :
                grade_sub_subject12.delete(0,END)
                grade_sub_subject12.insert(0,"A1")
            
            m2 = int(test_sub_subject13.get()) + int(exam_sub_subject13.get())
            total_sub_subject13.delete(0,END)
            total_sub_subject13.insert(0,m2)
            if  int(total_sub_subject13.get()) > 0 and int(total_sub_subject13.get()) <= 39:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"F9")
                
            elif  int(total_sub_subject13.get()) > 39 and int(total_sub_subject13.get()) <= 45:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"E8")    
            
            elif  int(total_sub_subject13.get()) > 45 and int(total_sub_subject13.get()) <= 49:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"D7")
                
            elif  int(total_sub_subject13.get()) > 49 and int(total_sub_subject13.get()) <= 55:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"D7")
                
            elif  int(total_sub_subject13.get()) > 55 and int(total_sub_subject13.get()) <= 59:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"C6")
                
            elif  int(total_sub_subject13.get()) > 59 and int(total_sub_subject13.get()) <= 65:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"C4")
                
            elif  int(total_sub_subject13.get()) > 65 and int(total_sub_subject13.get()) <= 69:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"B3")
                
            elif  int(total_sub_subject13.get()) > 69 and int(total_sub_subject13.get()) <= 75:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"B3")
                
            elif  int(total_sub_subject13.get()) > 75 and int(total_sub_subject13.get()) <= 79:
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"B2")
                
            elif  int(total_sub_subject13.get()) > 79 :
                grade_sub_subject13.delete(0,END)
                grade_sub_subject13.insert(0,"A1")
            
            n2 = int(test_sub_subject14.get()) + int(exam_sub_subject14.get())
            total_sub_subject14.delete(0,END)
            total_sub_subject14.insert(0,n2)
            if  int(total_sub_subject14.get()) > 0 and int(total_sub_subject14.get()) <= 39:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"F9")
                
            elif  int(total_sub_subject14.get()) > 39 and int(total_sub_subject14.get()) <= 45:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"E8")    
            
            elif  int(total_sub_subject14.get()) > 45 and int(total_sub_subject14.get()) <= 49:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"D7")
                
            elif  int(total_sub_subject14.get()) > 49 and int(total_sub_subject14.get()) <= 55:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"D7")
                
            elif  int(total_sub_subject14.get()) > 55 and int(total_sub_subject14.get()) <= 59:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"C6")
                
            elif  int(total_sub_subject14.get()) > 59 and int(total_sub_subject14.get()) <= 65:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"C4")
                
            elif  int(total_sub_subject14.get()) > 65 and int(total_sub_subject14.get()) <= 69:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"B3")
                
            elif  int(total_sub_subject14.get()) > 69 and int(total_sub_subject14.get()) <= 75:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"B3")
                
            elif  int(total_sub_subject14.get()) > 75 and int(total_sub_subject14.get()) <= 79:
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"B2")
                
            elif  int(total_sub_subject14.get()) > 79 :
                grade_sub_subject14.delete(0,END)
                grade_sub_subject14.insert(0,"A1")
            
            o2 = int(test_sub_subject15.get()) + int(exam_sub_subject15.get())
            total_sub_subject15.delete(0,END)
            total_sub_subject15.insert(0,o2)
            if  int(total_sub_subject15.get()) > 0 and int(total_sub_subject15.get()) <= 39:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"F9")
                
            elif  int(total_sub_subject15.get()) > 39 and int(total_sub_subject15.get()) <= 45:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"E8")    
            
            elif  int(total_sub_subject15.get()) > 45 and int(total_sub_subject15.get()) <= 49:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"D7")
                
            elif  int(total_sub_subject15.get()) > 49 and int(total_sub_subject15.get()) <= 55:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"D7")
                
            elif  int(total_sub_subject15.get()) > 55 and int(total_sub_subject15.get()) <= 59:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"C6")
                
            elif  int(total_sub_subject15.get()) > 59 and int(total_sub_subject15.get()) <= 65:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"C4")
                
            elif  int(total_sub_subject15.get()) > 65 and int(total_sub_subject15.get()) <= 69:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"B3")
                
            elif  int(total_sub_subject15.get()) > 69 and int(total_sub_subject15.get()) <= 75:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"B3")
                
            elif  int(total_sub_subject15.get()) > 75 and int(total_sub_subject15.get()) <= 79:
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"B2")
                
            elif  int(total_sub_subject15.get()) > 79 :
                grade_sub_subject15.delete(0,END)
                grade_sub_subject15.insert(0,"A1")
            
            p2 = int(test_sub_subject16.get()) + int(exam_sub_subject16.get())
            total_sub_subject16.delete(0,END)
            total_sub_subject16.insert(0,p2)
            if  int(total_sub_subject16.get()) > 0 and int(total_sub_subject16.get()) <= 39:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"F9")
                
            elif  int(total_sub_subject16.get()) > 39 and int(total_sub_subject16.get()) <= 45:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"E8")    
            
            elif  int(total_sub_subject16.get()) > 45 and int(total_sub_subject16.get()) <= 49:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"D7")
                
            elif  int(total_sub_subject16.get()) > 49 and int(total_sub_subject16.get()) <= 55:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"D7")
                
            elif  int(total_sub_subject16.get()) > 55 and int(total_sub_subject16.get()) <= 59:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"C6")
                
            elif  int(total_sub_subject16.get()) > 59 and int(total_sub_subject16.get()) <= 65:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"C4")
                
            elif  int(total_sub_subject16.get()) > 65 and int(total_sub_subject16.get()) <= 69:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"B3")
                
            elif  int(total_sub_subject16.get()) > 69 and int(total_sub_subject16.get()) <= 75:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"B3")
                
            elif  int(total_sub_subject16.get()) > 75 and int(total_sub_subject16.get()) <= 79:
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"B2")
                
            elif  int(total_sub_subject16.get()) > 79 :
                grade_sub_subject16.delete(0,END)
                grade_sub_subject16.insert(0,"A1")
            
            q2 = int(test_sub_subject17.get()) + int(exam_sub_subject17.get())
            total_sub_subject17.delete(0,END)
            total_sub_subject17.insert(0,q2)
            if  int(total_sub_subject17.get()) > 0 and int(total_sub_subject17.get()) <= 39:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"F9")
                
            elif  int(total_sub_subject17.get()) > 39 and int(total_sub_subject17.get()) <= 45:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"E8")    
            
            elif  int(total_sub_subject17.get()) > 45 and int(total_sub_subject17.get()) <= 49:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"D7")
                
            elif  int(total_sub_subject17.get()) > 49 and int(total_sub_subject17.get()) <= 55:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"D7")
                
            elif  int(total_sub_subject17.get()) > 55 and int(total_sub_subject17.get()) <= 59:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"C6")
                
            elif  int(total_sub_subject17.get()) > 59 and int(total_sub_subject17.get()) <= 65:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"C4")
                
            elif  int(total_sub_subject17.get()) > 65 and int(total_sub_subject17.get()) <= 69:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"B3")
                
            elif  int(total_sub_subject17.get()) > 69 and int(total_sub_subject17.get()) <= 75:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"B3")
                
            elif  int(total_sub_subject17.get()) > 75 and int(total_sub_subject17.get()) <= 79:
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"B2")
                
            elif  int(total_sub_subject17.get()) > 79 :
                grade_sub_subject17.delete(0,END)
                grade_sub_subject17.insert(0,"A1")
            
            r2 = int(test_sub_subject18.get()) + int(exam_sub_subject18.get())
            total_sub_subject18.delete(0,END)
            total_sub_subject18.insert(0,r2)
            if  int(total_sub_subject18.get()) > 0 and int(total_sub_subject18.get()) <= 39:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"F9")
                
            elif  int(total_sub_subject18.get()) > 39 and int(total_sub_subject18.get()) <= 45:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"E8")    
            
            elif  int(total_sub_subject18.get()) > 45 and int(total_sub_subject18.get()) <= 49:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"D7")
                
            elif  int(total_sub_subject18.get()) > 49 and int(total_sub_subject18.get()) <= 55:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"D7")
                
            elif  int(total_sub_subject18.get()) > 55 and int(total_sub_subject18.get()) <= 59:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"C6")
                
            elif  int(total_sub_subject18.get()) > 59 and int(total_sub_subject18.get()) <= 65:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"C4")
                
            elif  int(total_sub_subject18.get()) > 65 and int(total_sub_subject18.get()) <= 69:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"B3")
                
            elif  int(total_sub_subject18.get()) > 69 and int(total_sub_subject18.get()) <= 75:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"B3")
                
            elif  int(total_sub_subject18.get()) > 75 and int(total_sub_subject18.get()) <= 79:
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"B2")
                
            elif  int(total_sub_subject18.get()) > 79 :
                grade_sub_subject18.delete(0,END)
                grade_sub_subject18.insert(0,"A1")
            
            s2 = int(test_sub_subject19.get()) + int(exam_sub_subject19.get())
            total_sub_subject19.delete(0,END)
            total_sub_subject19.insert(0,s2)
            if  int(total_sub_subject19.get()) > 0 and int(total_sub_subject19.get()) <= 39:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"F9")
                
            elif  int(total_sub_subject19.get()) > 39 and int(total_sub_subject19.get()) <= 45:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"E8")    
            
            elif  int(total_sub_subject19.get()) > 45 and int(total_sub_subject19.get()) <= 49:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"D7")
                
            elif  int(total_sub_subject19.get()) > 49 and int(total_sub_subject19.get()) <= 55:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"D7")
                
            elif  int(total_sub_subject19.get()) > 55 and int(total_sub_subject19.get()) <= 59:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"C6")
                
            elif  int(total_sub_subject19.get()) > 59 and int(total_sub_subject19.get()) <= 65:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"C4")
                
            elif  int(total_sub_subject19.get()) > 65 and int(total_sub_subject19.get()) <= 69:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"B3")
                
            elif  int(total_sub_subject19.get()) > 69 and int(total_sub_subject19.get()) <= 75:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"B3")
                
            elif  int(total_sub_subject19.get()) > 75 and int(total_sub_subject19.get()) <= 79:
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"B2")
                
            elif  int(total_sub_subject19.get()) > 79 :
                grade_sub_subject19.delete(0,END)
                grade_sub_subject19.insert(0,"A1")
            
            t2 = int(test_sub_subject20.get()) + int(exam_sub_subject20.get())
            total_sub_subject20.delete(0,END)
            total_sub_subject20.insert(0,t2)
            if  int(total_sub_subject20.get()) > 0 and int(total_sub_subject20.get()) <= 39:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"F9")
                
            elif  int(total_sub_subject20.get()) > 39 and int(total_sub_subject20.get()) <= 45:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"E8")    
            
            elif  int(total_sub_subject20.get()) > 45 and int(total_sub_subject20.get()) <= 49:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"D7")
                
            elif  int(total_sub_subject20.get()) > 49 and int(total_sub_subject20.get()) <= 55:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"D7")
                
            elif  int(total_sub_subject20.get()) > 55 and int(total_sub_subject20.get()) <= 59:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"C6")
                
            elif  int(total_sub_subject20.get()) > 59 and int(total_sub_subject20.get()) <= 65:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"C4")
                
            elif  int(total_sub_subject20.get()) > 65 and int(total_sub_subject20.get()) <= 69:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"B3")
                
            elif  int(total_sub_subject20.get()) > 69 and int(total_sub_subject20.get()) <= 75:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"B3")
                
            elif  int(total_sub_subject20.get()) > 75 and int(total_sub_subject20.get()) <= 79:
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"B2")
                
            elif  int(total_sub_subject20.get()) > 79 :
                grade_sub_subject20.delete(0,END)
                grade_sub_subject20.insert(0,"A1")

    elif opt_term.get() == "THIRD TERM":
            a3 = int(test_subs_subject1.get()) + int(exam_subs_subject1.get())
            total_subs_subject1.delete(0,END)
            total_subs_subject1.insert(0,a2)
            if  int(total_subs_subject1.get()) > 0 and int(total_subs_subject1.get()) <= 39:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"F9")
                
            elif  int(total_subs_subject1.get()) > 39 and int(total_subs_subject1.get()) <= 45:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"E8")    
            
            elif  int(total_subs_subject1.get()) > 45 and int(total_subs_subject1.get()) <= 49:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"D7")
                
            elif  int(total_subs_subject1.get()) > 49 and int(total_subs_subject1.get()) <= 55:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"D7")
                
            elif  int(total_subs_subject1.get()) > 55 and int(total_subs_subject1.get()) <= 59:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"C6")
                
            elif  int(total_subs_subject1.get()) > 59 and int(total_subs_subject1.get()) <= 65:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"C4")
                
            elif  int(total_subs_subject1.get()) > 65 and int(total_subs_subject1.get()) <= 69:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"B3")
                
            elif  int(total_subs_subject1.get()) > 69 and int(total_subs_subject1.get()) <= 75:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"B3")
                
            elif  int(total_subs_subject1.get()) > 75 and int(total_subs_subject1.get()) <= 79:
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"B2")
                
            elif  int(total_subs_subject1.get()) > 79 :
                grade_subs_subject1.delete(0,END)
                grade_subs_subject1.insert(0,"A1")
            
                        
            b3 = int(test_subs_subject2.get()) + int(exam_subs_subject2.get())
            total_subs_subject2.delete(0,END)
            total_subs_subject2.insert(0,b2)
            if  int(total_subs_subject2.get()) > 0 and int(total_subs_subject2.get()) <= 39:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"F9")
                
            elif  int(total_subs_subject2.get()) > 39 and int(total_subs_subject2.get()) <= 45:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"E8")    
            
            elif  int(total_subs_subject2.get()) > 45 and int(total_subs_subject2.get()) <= 49:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"D7")
                
            elif  int(total_subs_subject2.get()) > 49 and int(total_subs_subject2.get()) <= 55:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"D7")
                
            elif  int(total_subs_subject2.get()) > 55 and int(total_subs_subject2.get()) <= 59:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"C6")
                
            elif  int(total_subs_subject2.get()) > 59 and int(total_subs_subject2.get()) <= 65:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"C4")
                
            elif  int(total_subs_subject2.get()) > 65 and int(total_subs_subject2.get()) <= 69:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"B3")
                
            elif  int(total_subs_subject2.get()) > 69 and int(total_subs_subject2.get()) <= 75:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"B3")
                
            elif  int(total_subs_subject2.get()) > 75 and int(total_subs_subject2.get()) <= 79:
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"B2")
                
            elif  int(total_subs_subject2.get()) > 79 :
                grade_subs_subject2.delete(0,END)
                grade_subs_subject2.insert(0,"A1")
            
            
            c3 = int(test_subs_subject3.get()) + int(exam_subs_subject3.get())
            total_subs_subject3.delete(0,END)
            total_subs_subject3.insert(0,c2)
            if  int(total_subs_subject3.get()) > 0 and int(total_subs_subject3.get()) <= 39:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"F9")
                
            elif  int(total_subs_subject3.get()) > 39 and int(total_subs_subject3.get()) <= 45:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"E8")    
            
            elif  int(total_subs_subject3.get()) > 45 and int(total_subs_subject3.get()) <= 49:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"D7")
                
            elif  int(total_subs_subject3.get()) > 49 and int(total_subs_subject3.get()) <= 55:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"D7")
                
            elif  int(total_subs_subject3.get()) > 55 and int(total_subs_subject3.get()) <= 59:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"C6")
                
            elif  int(total_subs_subject3.get()) > 59 and int(total_subs_subject3.get()) <= 65:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"C4")
                
            elif  int(total_subs_subject3.get()) > 65 and int(total_subs_subject3.get()) <= 69:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"B3")
                
            elif  int(total_subs_subject3.get()) > 69 and int(total_subs_subject3.get()) <= 75:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"B3")
                
            elif  int(total_subs_subject3.get()) > 75 and int(total_subs_subject3.get()) <= 79:
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"B2")
                
            elif  int(total_subs_subject3.get()) > 79 :
                grade_subs_subject3.delete(0,END)
                grade_subs_subject3.insert(0,"A1")
            
            
            d3 = int(test_subs_subject4.get()) + int(exam_subs_subject4.get())
            total_subs_subject4.delete(0,END)
            total_subs_subject4.insert(0,d2)
            if  int(total_subs_subject4.get()) > 0 and int(total_subs_subject4.get()) <= 39:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"F9")
                
            elif  int(total_subs_subject4.get()) > 39 and int(total_subs_subject4.get()) <= 45:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"E8")    
            
            elif  int(total_subs_subject4.get()) > 45 and int(total_subs_subject4.get()) <= 49:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"D7")
                
            elif  int(total_subs_subject4.get()) > 49 and int(total_subs_subject4.get()) <= 55:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"D7")
                
            elif  int(total_subs_subject4.get()) > 55 and int(total_subs_subject4.get()) <= 59:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"C6")
                
            elif  int(total_subs_subject4.get()) > 59 and int(total_subs_subject4.get()) <= 65:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"C4")
                
            elif  int(total_subs_subject4.get()) > 65 and int(total_subs_subject4.get()) <= 69:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"B3")
                
            elif  int(total_subs_subject4.get()) > 69 and int(total_subs_subject4.get()) <= 75:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"B3")
                
            elif  int(total_subs_subject4.get()) > 75 and int(total_subs_subject4.get()) <= 79:
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"B2")
                
            elif  int(total_subs_subject4.get()) > 79 :
                grade_subs_subject4.delete(0,END)
                grade_subs_subject4.insert(0,"A1")
            
            
            e3 = int(test_subs_subject5.get()) + int(exam_subs_subject5.get())
            total_subs_subject5.delete(0,END)
            total_subs_subject5.insert(0,e2)
            if  int(total_subs_subject5.get()) > 0 and int(total_subs_subject5.get()) <= 39:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"F9")
                
            elif  int(total_subs_subject5.get()) > 39 and int(total_subs_subject5.get()) <= 45:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"E8")    
            
            elif  int(total_subs_subject5.get()) > 45 and int(total_subs_subject5.get()) <= 49:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"D7")
                
            elif  int(total_subs_subject5.get()) > 49 and int(total_subs_subject5.get()) <= 55:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"D7")
                
            elif  int(total_subs_subject5.get()) > 55 and int(total_subs_subject5.get()) <= 59:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"C6")
                
            elif  int(total_subs_subject5.get()) > 59 and int(total_subs_subject5.get()) <= 65:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"C4")
                
            elif  int(total_subs_subject5.get()) > 65 and int(total_subs_subject5.get()) <= 69:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"B3")
                
            elif  int(total_subs_subject5.get()) > 69 and int(total_subs_subject5.get()) <= 75:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"B3")
                
            elif  int(total_subs_subject5.get()) > 75 and int(total_subs_subject5.get()) <= 79:
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"B2")
                
            elif  int(total_subs_subject5.get()) > 79 :
                grade_subs_subject5.delete(0,END)
                grade_subs_subject5.insert(0,"A1")
            
            
            f3 = int(test_subs_subject6.get()) + int(exam_subs_subject6.get())
            total_subs_subject6.delete(0,END)
            total_subs_subject6.insert(0,f2)
            if  int(total_subs_subject6.get()) > 0 and int(total_subs_subject6.get()) <= 39:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"F9")
                
            elif  int(total_subs_subject6.get()) > 39 and int(total_subs_subject6.get()) <= 45:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"E8")    
            
            elif  int(total_subs_subject6.get()) > 45 and int(total_subs_subject6.get()) <= 49:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"D7")
                
            elif  int(total_subs_subject6.get()) > 49 and int(total_subs_subject6.get()) <= 55:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"D7")
                
            elif  int(total_subs_subject6.get()) > 55 and int(total_subs_subject6.get()) <= 59:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"C6")
                
            elif  int(total_subs_subject6.get()) > 59 and int(total_subs_subject6.get()) <= 65:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"C4")
                
            elif  int(total_subs_subject6.get()) > 65 and int(total_subs_subject6.get()) <= 69:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"B3")
                
            elif  int(total_subs_subject6.get()) > 69 and int(total_subs_subject6.get()) <= 75:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"B3")
                
            elif  int(total_subs_subject6.get()) > 75 and int(total_subs_subject6.get()) <= 79:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"B2")
                
            elif  int(total_subs_subject6.get()) > 79 :
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"A1")
            
            g3 = int(test_subs_subject7.get()) + int(exam_subs_subject7.get())
            total_subs_subject7.delete(0,END)
            total_subs_subject7.insert(0,g2)
            if  int(total_subs_subject7.get()) > 0 and int(total_subs_subject7.get()) <= 39:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"F9")
                
            elif  int(total_subs_subject7.get()) > 39 and int(total_subs_subject7.get()) <= 45:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"E8")    
            
            elif  int(total_subs_subject7.get()) > 45 and int(total_subs_subject7.get()) <= 49:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"D7")
                
            elif  int(total_subs_subject7.get()) > 49 and int(total_subs_subject7.get()) <= 55:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"D7")
                
            elif  int(total_subs_subject7.get()) > 55 and int(total_subs_subject7.get()) <= 59:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"C6")
                
            elif  int(total_subs_subject7.get()) > 59 and int(total_subs_subject7.get()) <= 65:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"C4")
                
            elif  int(total_subs_subject7.get()) > 65 and int(total_subs_subject7.get()) <= 69:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"B3")
                
            elif  int(total_subs_subject7.get()) > 69 and int(total_subs_subject7.get()) <= 75:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"B3")
                
            elif  int(total_subs_subject7.get()) > 75 and int(total_subs_subject7.get()) <= 79:
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"B2")
                
            elif  int(total_subs_subject7.get()) > 79 :
                grade_subs_subject7.delete(0,END)
                grade_subs_subject7.insert(0,"A1")
                
            h3 = int(test_subs_subject8.get()) + int(exam_subs_subject8.get())
            total_subs_subject8.delete(0,END)
            total_subs_subject8.insert(0,h2)
            if  int(total_subs_subject8.get()) > 0 and int(total_subs_subject8.get()) <= 39:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"F9")
                
            elif  int(total_subs_subject8.get()) > 39 and int(total_subs_subject8.get()) <= 45:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"E8")    
            
            elif  int(total_subs_subject8.get()) > 45 and int(total_subs_subject8.get()) <= 49:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"D7")
                
            elif  int(total_subs_subject8.get()) > 49 and int(total_subs_subject8.get()) <= 55:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"D7")
                
            elif  int(total_subs_subject8.get()) > 55 and int(total_subs_subject8.get()) <= 59:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"C6")
                
            elif  int(total_subs_subject8.get()) > 59 and int(total_subs_subject8.get()) <= 65:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"C4")
                
            elif  int(total_subs_subject8.get()) > 65 and int(total_subs_subject8.get()) <= 69:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"B3")
                
            elif  int(total_subs_subject8.get()) > 69 and int(total_subs_subject8.get()) <= 75:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"B3")
                
            elif  int(total_subs_subject8.get()) > 75 and int(total_subs_subject8.get()) <= 79:
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"B2")
                
            elif  int(total_subs_subject8.get()) > 79 :
                grade_subs_subject8.delete(0,END)
                grade_subs_subject8.insert(0,"A1")
                
            i3 = int(test_subs_subject9.get()) + int(exam_subs_subject9.get())
            total_subs_subject9.delete(0,END)
            total_subs_subject9.insert(0,i2)
            if  int(total_subs_subject9.get()) > 0 and int(total_subs_subject9.get()) <= 39:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"F9")
                
            elif  int(total_subs_subject9.get()) > 39 and int(total_subs_subject9.get()) <= 45:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"E8")    
            
            elif  int(total_subs_subject9.get()) > 45 and int(total_subs_subject9.get()) <= 49:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"D7")
                
            elif  int(total_subs_subject9.get()) > 49 and int(total_subs_subject9.get()) <= 55:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"D7")
                
            elif  int(total_subs_subject9.get()) > 55 and int(total_subs_subject9.get()) <= 59:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"C6")
                
            elif  int(total_subs_subject9.get()) > 59 and int(total_subs_subject9.get()) <= 65:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"C4")
                
            elif  int(total_subs_subject9.get()) > 65 and int(total_subs_subject9.get()) <= 69:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"B3")
                
            elif  int(total_subs_subject9.get()) > 69 and int(total_subs_subject9.get()) <= 75:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"B3")
                
            elif  int(total_subs_subject9.get()) > 75 and int(total_subs_subject9.get()) <= 79:
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"B2")
                
            elif  int(total_subs_subject9.get()) > 79 :
                grade_subs_subject9.delete(0,END)
                grade_subs_subject9.insert(0,"A1")
            
            j3 = int(test_subs_subject10.get()) + int(exam_subs_subject10.get())
            total_subs_subject10.delete(0,END)
            total_subs_subject10.insert(0,j2)
            if  int(total_subs_subject10.get()) > 0 and int(total_subs_subject10.get()) <= 39:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"F9")
                
            elif  int(total_subs_subject10.get()) > 39 and int(total_subs_subject10.get()) <= 45:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"E8")    
            
            elif  int(total_subs_subject10.get()) > 45 and int(total_subs_subject10.get()) <= 49:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"D7")
                
            elif  int(total_subs_subject10.get()) > 49 and int(total_subs_subject10.get()) <= 55:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"D7")
                
            elif  int(total_subs_subject10.get()) > 55 and int(total_subs_subject10.get()) <= 59:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"C6")
                
            elif  int(total_subs_subject10.get()) > 59 and int(total_subs_subject10.get()) <= 65:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"C4")
                
            elif  int(total_subs_subject10.get()) > 65 and int(total_subs_subject10.get()) <= 69:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"B3")
                
            elif  int(total_subs_subject10.get()) > 69 and int(total_subs_subject10.get()) <= 75:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"B3")
                
            elif  int(total_subs_subject10.get()) > 75 and int(total_subs_subject10.get()) <= 79:
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"B2")
                
            elif  int(total_subs_subject10.get()) > 79 :
                grade_subs_subject10.delete(0,END)
                grade_subs_subject10.insert(0,"A1")
            
            k3 = int(test_subs_subject11.get()) + int(exam_subs_subject11.get())
            total_subs_subject11.delete(0,END)
            total_subs_subject11.insert(0,k2)
            if  int(total_subs_subject11.get()) > 0 and int(total_subs_subject11.get()) <= 39:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"F9")
                
            elif  int(total_subs_subject11.get()) > 39 and int(total_subs_subject11.get()) <= 45:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"E8")    
            
            elif  int(total_subs_subject11.get()) > 45 and int(total_subs_subject11.get()) <= 49:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"D7")
                
            elif  int(total_subs_subject11.get()) > 49 and int(total_subs_subject11.get()) <= 55:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"D7")
                
            elif  int(total_subs_subject11.get()) > 55 and int(total_subs_subject11.get()) <= 59:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"C6")
                
            elif  int(total_subs_subject11.get()) > 59 and int(total_subs_subject11.get()) <= 65:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"C4")
                
            elif  int(total_subs_subject6.get()) > 65 and int(total_subs_subject6.get()) <= 69:
                grade_subs_subject6.delete(0,END)
                grade_subs_subject6.insert(0,"B3")
                
            elif  int(total_subs_subject11.get()) > 69 and int(total_subs_subject11.get()) <= 75:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"B3")
                
            elif  int(total_subs_subject11.get()) > 75 and int(total_subs_subject11.get()) <= 79:
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"B2")
                
            elif  int(total_subs_subject11.get()) > 79 :
                grade_subs_subject11.delete(0,END)
                grade_subs_subject11.insert(0,"A1")
            
            l3 = int(test_subs_subject12.get()) + int(exam_subs_subject12.get())
            total_subs_subject12.delete(0,END)
            total_subs_subject12.insert(0,l2)
            if  int(total_subs_subject12.get()) > 0 and int(total_subs_subject12.get()) <= 39:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"F9")
                
            elif  int(total_subs_subject12.get()) > 39 and int(total_subs_subject12.get()) <= 45:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"E8")    
            
            elif  int(total_subs_subject12.get()) > 45 and int(total_subs_subject12.get()) <= 49:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"D7")
                
            elif  int(total_subs_subject12.get()) > 49 and int(total_subs_subject12.get()) <= 55:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"D7")
                
            elif  int(total_subs_subject12.get()) > 55 and int(total_subs_subject12.get()) <= 59:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"C6")
                
            elif  int(total_subs_subject12.get()) > 59 and int(total_subs_subject12.get()) <= 65:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"C4")
                
            elif  int(total_subs_subject12.get()) > 65 and int(total_subs_subject12.get()) <= 69:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"B3")
                
            elif  int(total_subs_subject12.get()) > 69 and int(total_subs_subject12.get()) <= 75:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"B3")
                
            elif  int(total_subs_subject12.get()) > 75 and int(total_subs_subject12.get()) <= 79:
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"B2")
                
            elif  int(total_subs_subject12.get()) > 79 :
                grade_subs_subject12.delete(0,END)
                grade_subs_subject12.insert(0,"A1")
            
            m3 = int(test_subs_subject13.get()) + int(exam_subs_subject13.get())
            total_subs_subject13.delete(0,END)
            total_subs_subject13.insert(0,m2)
            if  int(total_subs_subject13.get()) > 0 and int(total_subs_subject13.get()) <= 39:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"F9")
                
            elif  int(total_subs_subject13.get()) > 39 and int(total_subs_subject13.get()) <= 45:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"E8")    
            
            elif  int(total_subs_subject13.get()) > 45 and int(total_subs_subject13.get()) <= 49:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"D7")
                
            elif  int(total_subs_subject13.get()) > 49 and int(total_subs_subject13.get()) <= 55:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"D7")
                
            elif  int(total_subs_subject13.get()) > 55 and int(total_subs_subject13.get()) <= 59:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"C6")
                
            elif  int(total_subs_subject13.get()) > 59 and int(total_subs_subject13.get()) <= 65:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"C4")
                
            elif  int(total_subs_subject13.get()) > 65 and int(total_subs_subject13.get()) <= 69:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"B3")
                
            elif  int(total_subs_subject13.get()) > 69 and int(total_subs_subject13.get()) <= 75:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"B3")
                
            elif  int(total_subs_subject13.get()) > 75 and int(total_subs_subject13.get()) <= 79:
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"B2")
                
            elif  int(total_subs_subject13.get()) > 79 :
                grade_subs_subject13.delete(0,END)
                grade_subs_subject13.insert(0,"A1")
            
            n3 = int(test_subs_subject14.get()) + int(exam_subs_subject14.get())
            total_subs_subject14.delete(0,END)
            total_subs_subject14.insert(0,n2)
            if  int(total_subs_subject14.get()) > 0 and int(total_subs_subject14.get()) <= 39:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"F9")
                
            elif  int(total_subs_subject14.get()) > 39 and int(total_subs_subject14.get()) <= 45:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"E8")    
            
            elif  int(total_subs_subject14.get()) > 45 and int(total_subs_subject14.get()) <= 49:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"D7")
                
            elif  int(total_subs_subject14.get()) > 49 and int(total_subs_subject14.get()) <= 55:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"D7")
                
            elif  int(total_subs_subject14.get()) > 55 and int(total_subs_subject14.get()) <= 59:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"C6")
                
            elif  int(total_subs_subject14.get()) > 59 and int(total_subs_subject14.get()) <= 65:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"C4")
                
            elif  int(total_subs_subject14.get()) > 65 and int(total_subs_subject14.get()) <= 69:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"B3")
                
            elif  int(total_subs_subject14.get()) > 69 and int(total_subs_subject14.get()) <= 75:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"B3")
                
            elif  int(total_subs_subject14.get()) > 75 and int(total_subs_subject14.get()) <= 79:
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"B2")
                
            elif  int(total_subs_subject14.get()) > 79 :
                grade_subs_subject14.delete(0,END)
                grade_subs_subject14.insert(0,"A1")
            
            o3 = int(test_subs_subject15.get()) + int(exam_subs_subject15.get())
            total_subs_subject15.delete(0,END)
            total_subs_subject15.insert(0,o2)
            if  int(total_subs_subject15.get()) > 0 and int(total_subs_subject15.get()) <= 39:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"F9")
                
            elif  int(total_subs_subject15.get()) > 39 and int(total_subs_subject15.get()) <= 45:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"E8")    
            
            elif  int(total_subs_subject15.get()) > 45 and int(total_subs_subject15.get()) <= 49:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"D7")
                
            elif  int(total_subs_subject15.get()) > 49 and int(total_subs_subject15.get()) <= 55:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"D7")
                
            elif  int(total_subs_subject15.get()) > 55 and int(total_subs_subject15.get()) <= 59:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"C6")
                
            elif  int(total_subs_subject15.get()) > 59 and int(total_subs_subject15.get()) <= 65:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"C4")
                
            elif  int(total_subs_subject15.get()) > 65 and int(total_subs_subject15.get()) <= 69:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"B3")
                
            elif  int(total_subs_subject15.get()) > 69 and int(total_subs_subject15.get()) <= 75:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"B3")
                
            elif  int(total_subs_subject15.get()) > 75 and int(total_subs_subject15.get()) <= 79:
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"B2")
                
            elif  int(total_subs_subject15.get()) > 79 :
                grade_subs_subject15.delete(0,END)
                grade_subs_subject15.insert(0,"A1")
            
            p3 = int(test_subs_subject16.get()) + int(exam_subs_subject16.get())
            total_subs_subject16.delete(0,END)
            total_subs_subject16.insert(0,p2)
            if  int(total_subs_subject16.get()) > 0 and int(total_subs_subject16.get()) <= 39:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"F9")
                
            elif  int(total_subs_subject16.get()) > 39 and int(total_subs_subject16.get()) <= 45:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"E8")    
            
            elif  int(total_subs_subject16.get()) > 45 and int(total_subs_subject16.get()) <= 49:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"D7")
                
            elif  int(total_subs_subject16.get()) > 49 and int(total_subs_subject16.get()) <= 55:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"D7")
                
            elif  int(total_subs_subject16.get()) > 55 and int(total_subs_subject16.get()) <= 59:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"C6")
                
            elif  int(total_subs_subject16.get()) > 59 and int(total_subs_subject16.get()) <= 65:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"C4")
                
            elif  int(total_subs_subject16.get()) > 65 and int(total_subs_subject16.get()) <= 69:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"B3")
                
            elif  int(total_subs_subject16.get()) > 69 and int(total_subs_subject16.get()) <= 75:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"B3")
                
            elif  int(total_subs_subject16.get()) > 75 and int(total_subs_subject16.get()) <= 79:
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"B2")
                
            elif  int(total_subs_subject16.get()) > 79 :
                grade_subs_subject16.delete(0,END)
                grade_subs_subject16.insert(0,"A1")
            
            q3 = int(test_subs_subject17.get()) + int(exam_subs_subject17.get())
            total_subs_subject17.delete(0,END)
            total_subs_subject17.insert(0,q2)
            if  int(total_subs_subject17.get()) > 0 and int(total_subs_subject17.get()) <= 39:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"F9")
                
            elif  int(total_subs_subject17.get()) > 39 and int(total_subs_subject17.get()) <= 45:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"E8")    
            
            elif  int(total_subs_subject17.get()) > 45 and int(total_subs_subject17.get()) <= 49:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"D7")
                
            elif  int(total_subs_subject17.get()) > 49 and int(total_subs_subject17.get()) <= 55:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"D7")
                
            elif  int(total_subs_subject17.get()) > 55 and int(total_subs_subject17.get()) <= 59:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"C6")
                
            elif  int(total_subs_subject17.get()) > 59 and int(total_subs_subject17.get()) <= 65:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"C4")
                
            elif  int(total_subs_subject17.get()) > 65 and int(total_subs_subject17.get()) <= 69:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"B3")
                
            elif  int(total_subs_subject17.get()) > 69 and int(total_subs_subject17.get()) <= 75:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"B3")
                
            elif  int(total_subs_subject17.get()) > 75 and int(total_subs_subject17.get()) <= 79:
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"B2")
                
            elif  int(total_subs_subject17.get()) > 79 :
                grade_subs_subject17.delete(0,END)
                grade_subs_subject17.insert(0,"A1")
            
            r3 = int(test_subs_subject18.get()) + int(exam_subs_subject18.get())
            total_subs_subject18.delete(0,END)
            total_subs_subject18.insert(0,r2)
            if  int(total_subs_subject18.get()) > 0 and int(total_subs_subject18.get()) <= 39:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"F9")
                
            elif  int(total_subs_subject18.get()) > 39 and int(total_subs_subject18.get()) <= 45:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"E8")    
            
            elif  int(total_subs_subject18.get()) > 45 and int(total_subs_subject18.get()) <= 49:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"D7")
                
            elif  int(total_subs_subject18.get()) > 49 and int(total_subs_subject18.get()) <= 55:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"D7")
                
            elif  int(total_subs_subject18.get()) > 55 and int(total_subs_subject18.get()) <= 59:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"C6")
                
            elif  int(total_subs_subject18.get()) > 59 and int(total_subs_subject18.get()) <= 65:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"C4")
                
            elif  int(total_subs_subject18.get()) > 65 and int(total_subs_subject18.get()) <= 69:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"B3")
                
            elif  int(total_subs_subject18.get()) > 69 and int(total_subs_subject18.get()) <= 75:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"B3")
                
            elif  int(total_subs_subject18.get()) > 75 and int(total_subs_subject18.get()) <= 79:
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"B2")
                
            elif  int(total_subs_subject18.get()) > 79 :
                grade_subs_subject18.delete(0,END)
                grade_subs_subject18.insert(0,"A1")
            
            s3 = int(test_subs_subject19.get()) + int(exam_subs_subject19.get())
            total_subs_subject19.delete(0,END)
            total_subs_subject19.insert(0,s2)
            if  int(total_subs_subject19.get()) > 0 and int(total_subs_subject19.get()) <= 39:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"F9")
                
            elif  int(total_subs_subject19.get()) > 39 and int(total_subs_subject19.get()) <= 45:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"E8")    
            
            elif  int(total_subs_subject19.get()) > 45 and int(total_subs_subject19.get()) <= 49:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"D7")
                
            elif  int(total_subs_subject19.get()) > 49 and int(total_subs_subject19.get()) <= 55:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"D7")
                
            elif  int(total_subs_subject19.get()) > 55 and int(total_subs_subject19.get()) <= 59:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"C6")
                
            elif  int(total_subs_subject19.get()) > 59 and int(total_subs_subject19.get()) <= 65:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"C4")
                
            elif  int(total_subs_subject19.get()) > 65 and int(total_subs_subject19.get()) <= 69:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"B3")
                
            elif  int(total_subs_subject19.get()) > 69 and int(total_subs_subject19.get()) <= 75:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"B3")
                
            elif  int(total_subs_subject19.get()) > 75 and int(total_subs_subject19.get()) <= 79:
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"B2")
                
            elif  int(total_subs_subject19.get()) > 79 :
                grade_subs_subject19.delete(0,END)
                grade_subs_subject19.insert(0,"A1")
            
            t3 = int(test_subs_subject20.get()) + int(exam_subs_subject20.get())
            total_subs_subject20.delete(0,END)
            total_subs_subject20.insert(0,t2)
            if  int(total_subs_subject20.get()) > 0 and int(total_subs_subject20.get()) <= 39:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"F9")
                
            elif  int(total_subs_subject20.get()) > 39 and int(total_subs_subject20.get()) <= 45:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"E8")    
            
            elif  int(total_subs_subject20.get()) > 45 and int(total_subs_subject20.get()) <= 49:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"D7")
                
            elif  int(total_subs_subject20.get()) > 49 and int(total_subs_subject20.get()) <= 55:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"D7")
                
            elif  int(total_subs_subject20.get()) > 55 and int(total_subs_subject20.get()) <= 59:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"C6")
                
            elif  int(total_subs_subject20.get()) > 59 and int(total_subs_subject20.get()) <= 65:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"C4")
                
            elif  int(total_subs_subject20.get()) > 65 and int(total_subs_subject20.get()) <= 69:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"B3")
                
            elif  int(total_subs_subject20.get()) > 69 and int(total_subs_subject20.get()) <= 75:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"B3")
                
            elif  int(total_subs_subject20.get()) > 75 and int(total_subs_subject20.get()) <= 79:
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"B2")
                
            elif  int(total_subs_subject20.get()) > 79 :
                grade_subs_subject20.delete(0,END)
                grade_subs_subject20.insert(0,"A1")

def r_clear():
    view_search.delete(0,END)
    name.delete(0,END)
    stud_gender.delete(0,END)
    stud_class.delete(0,END)
    stud_reg_num.delete(0,END)
    
    lbl_course_subject1.delete(0,END)
    lbl_course_subject2.delete(0,END)
    lbl_course_subject3.delete(0,END)
    lbl_course_subject4.delete(0,END)
    lbl_course_subject5.delete(0,END)
    lbl_course_subject6.delete(0,END)
    lbl_course_subject7.delete(0,END)
    lbl_course_subject8.delete(0,END)
    lbl_course_subject9.delete(0,END)
    lbl_course_subject10.delete(0,END)
    lbl_course_subject11.delete(0,END)
    lbl_course_subject12.delete(0,END)
    lbl_course_subject13.delete(0,END)
    lbl_course_subject14.delete(0,END)
    lbl_course_subject15.delete(0,END)
    lbl_course_subject16.delete(0,END)
    lbl_course_subject17.delete(0,END)
    lbl_course_subject18.delete(0,END)
    lbl_course_subject19.delete(0,END)
    lbl_course_subject20.delete(0,END)
    
    messagebox.showinfo("Confirmation", "Data Cleared Successfully!!!")


def r_search():
    conn = sqlite3.connect('student management system.db')
    
    c = conn.cursor()
    
    view_rec_id = view_search.get()
    c.execute("SELECT * FROM subjects WHERE student_id=?",(view_rec_id,))
    view_records = c.fetchall()
    print(view_records)
    
    name.delete(0,END)
    stud_gender.delete(0,END)
    stud_class.delete(0,END)
    stud_reg_num.delete(0,END)
    
    lbl_course_subject1.configure(text="")
    lbl_course_subject2.configure(text="")
    lbl_course_subject3.configure(text="")
    lbl_course_subject4.configure(text="")
    lbl_course_subject5.configure(text="")
    lbl_course_subject6.configure(text="")
    lbl_course_subject7.configure(text="")
    lbl_course_subject8.configure(text="")
    lbl_course_subject9.configure(text="")
    lbl_course_subject10.configure(text="")
    lbl_course_subject11.configure(text="")
    lbl_course_subject12.configure(text="")
    lbl_course_subject13.configure(text="")
    lbl_course_subject14.configure(text="")
    lbl_course_subject15.configure(text="")
    lbl_course_subject16.configure(text="")
    lbl_course_subject17.configure(text="")
    lbl_course_subject18.configure(text="")
    lbl_course_subject19.configure(text="")
    lbl_course_subject20.configure(text="")

    
    # looping through the result
    if opt_term.get() == "FIRST TERM":
        
        for record in view_records:
            name.insert(0,record[0])
            stud_gender.insert(0,record[3])
            stud_class.insert(0,record[2])
            stud_reg_num.insert(0,record[5])
            
            lbl_course_subject1.insert(0,record[6])
            lbl_course_subject2.insert(0,record[7])
            lbl_course_subject3.insert(0,record[8])
            lbl_course_subject4.insert(0,record[9])
            lbl_course_subject5.insert(0,record[10])
            lbl_course_subject6.insert(0,record[11])
            lbl_course_subject7.insert(0,record[12])
            lbl_course_subject8.insert(0,record[13])
            lbl_course_subject9.insert(0,record[14])
            lbl_course_subject10.insert(0,record[15])
            lbl_course_subject11.insert(0,record[16])
            lbl_course_subject12.insert(0,record[17])
            lbl_course_subject13.insert(0,record[18])
            lbl_course_subject14.insert(0,record[19])
            lbl_course_subject15.insert(0,record[20])
            lbl_course_subject16.insert(0,record[21])
            lbl_course_subject17.insert(0,record[22])
            lbl_course_subject18.insert(0,record[23])
            lbl_course_subject19.insert(0,record[24])
            lbl_course_subject20.insert(0,record[25])
    
    elif opt_term.get() == "SECOND TERM":
        
        for record in view_records:
            name.insert(0,record[0])
            stud_gender.insert(0,record[3])
            stud_class.insert(0,record[2])
            stud_reg_num.insert(0,record[5])
            
            sub_subject1.insert(0,record[6])
            sub_subject2.insert(0,record[7])
            sub_subject3.insert(0,record[8])
            sub_subject4.insert(0,record[9])
            sub_subject5.insert(0,record[10])
            sub_subject6.insert(0,record[11])
            sub_subject7.insert(0,record[12])
            sub_subject8.insert(0,record[13])
            sub_subject9.insert(0,record[14])
            sub_subject10.insert(0,record[15])
            sub_subject11.insert(0,record[16])
            sub_subject12.insert(0,record[17])
            sub_subject13.insert(0,record[18])
            sub_subject14.insert(0,record[19])
            sub_subject15.insert(0,record[20])
            sub_subject16.insert(0,record[21])
            sub_subject17.insert(0,record[22])
            sub_subject18.insert(0,record[23])
            sub_subject19.insert(0,record[24])
            sub_subject20.insert(0,record[25])

    elif opt_term.get() == "THIRD TERM":
               
        for record in view_records:
            name.insert(0,record[0])
            stud_gender.insert(0,record[3])
            stud_class.insert(0,record[2])
            stud_reg_num.insert(0,record[5])
            
            lbl_subs_subject1.insert(0,record[6])
            lbl_subs_subject2.insert(0,record[7])
            lbl_subs_subject3.insert(0,record[8])
            lbl_subs_subject4.insert(0,record[9])
            lbl_subs_subject5.insert(0,record[10])
            lbl_subs_subject6.insert(0,record[11])
            lbl_subs_subject7.insert(0,record[12])
            lbl_subs_subject8.insert(0,record[13])
            lbl_subs_subject9.insert(0,record[14])
            lbl_subs_subject10.insert(0,record[15])
            lbl_subs_subject11.insert(0,record[16])
            lbl_subs_subject12.insert(0,record[17])
            lbl_subs_subject13.insert(0,record[18])
            lbl_subs_subject14.insert(0,record[19])
            lbl_subs_subject15.insert(0,record[20])
            lbl_subs_subject16.insert(0,record[21])
            lbl_subs_subject17.insert(0,record[22])
            lbl_subs_subject18.insert(0,record[23])
            lbl_subs_subject19.insert(0,record[24])
            lbl_subs_subject20.insert(0,record[25])
    else:
        messagebox.showerror("ERROR MESSAGE","PLEASE SELECT TERM")
    conn.commit()
    conn.close()

def r_reg():
    
    conn = sqlite3.connect('student management system.db')
    
    c = conn.cursor()
    

    c.execute()
    
    conn.commit()
    conn.close()



view_search = customtkinter.CTkEntry(search_upload_frame,width=120,height=10,font=("cambria", 12),bg_color="gray", fg_color="gray", text_color="cyan", corner_radius=5, placeholder_text="Enter Reg.No.", placeholder_text_color="cyan")
view_search.focus_set()
view_search.grid(row=0,column=0)
btn_view_search = customtkinter.CTkButton(search_upload_frame,text="SEARCH",font=("cambria", 12),text_color="cyan", width=20, height=10, bg_color="gray", fg_color="gray",hover_color="green", command= r_search)
btn_view_search.grid(row=0, column=2)

lbl_name = Label(stud_info_frame, text="FULL NAME",font=("cambria", 10),bg='gray', fg='cyan')
lbl_name.grid(row=0, column=0)
lbl_stud_gender = Label(stud_info_frame, text="GENDER",font=("cambria", 10),bg='gray', fg='cyan')
lbl_stud_gender.grid(row=0, column=1)
lbl_stud_class = Label(stud_info_frame, text="CLASS",font=("cambria", 10),bg='gray', fg='cyan')
lbl_stud_class.grid(row=0, column=2)
lbl_stud_reg_num = Label(stud_info_frame, text="REG. NO.",font=("cambria", 10),bg='gray', fg='cyan')
lbl_stud_reg_num.grid(row=0, column=3)


name = customtkinter.CTkEntry(stud_info_frame,width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
name.grid(row=1, column=0)
stud_gender = customtkinter.CTkEntry(stud_info_frame,width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_gender.grid(row=1, column=1)
stud_class = customtkinter.CTkEntry(stud_info_frame,width= 60, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_class.grid(row=1, column=2)
stud_reg_num = customtkinter.CTkEntry(stud_info_frame,width= 100, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_reg_num.grid(row=1, column=3, padx=3)

        
term =[
    "SELECT TERM",
    "FIRST TERM",
    "SECOND TERM",
    "THIRD TERM"
]

def pick_term(e):
    if opt_term.get() == "FIRST TERM":
        course_frame1.grid_forget()
        course_frame2.grid_forget()
        course_frame.grid(row=3, column=0,pady=5)
        # sub1.configure(text=record[6])
        # sub2.configure(text=record[7])
        # sub3.configure(text=record[8])
        # sub4.configure(text=record[9])
        # sub5.configure(text=record[10])
        # sub6.configure(text=record[11])
        # sub7.configure(text=record[12])
        # sub8.configure(text=record[13])
        # sub9.configure(text=record[14])
        # sub10.configure(text=record[15])
        # sub11.configure(text=record[16])
        # sub12.configure(text=record[17])
        # sub13.configure(text=record[18])
        # sub14.configure(text=record[19])
        # sub15.configure(text=record[20])
        # sub16.configure(text=record[21])
        # sub17.configure(text=record[22])
        # sub18.configure(text=record[23])
        # sub19.configure(text=record[24])
        # sub20.configure(text=record[25])

        
        
    elif opt_term.get() == "SECOND TERM":
        course_frame.grid_forget()
        course_frame2.grid_forget()
        course_frame1.grid(row=3, column=0,pady=5)

        
    elif opt_term.get() == "THIRD TERM":
        course_frame.grid_forget()
        course_frame1.grid_forget()
        course_frame2.grid(row=3, column=0,pady=5)

    
    else:
        course_frame.grid_forget()
        course_frame1.grid_forget()
        course_frame2.grid_forget()
        

opt_term = ttk.Combobox(search_upload_frame, value= term ,width=13,background="gray", foreground="cyan",font=("cambria", 10))
opt_term.current(0)
opt_term.bind("<<ComboboxSelected>>", pick_term)
opt_term.grid(row=0, column=1,pady=5)

#______________________________________ first term________________________________________________________________________

lbl_stud_class = Label(course_frame, text="FIRST-TERM SCORE",font=("cambria", 15),bg='gray', fg='cyan')
lbl_stud_class.grid(row=0, column=0)
scrollable_frame = customtkinter.CTkScrollableFrame(course_frame,bg_color="gray", fg_color="gray", scrollbar_button_hover_color="green", width=480)
scrollable_frame.grid(row=1, column=0)
lbl_course_subject1 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject1.grid(row=2, column=0,padx=2,pady=2)
lbl_course_subject2 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject2.grid(row=3, column=0,padx=2,pady=2)
lbl_course_subject3 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject3.grid(row=4, column=0,padx=2,pady=2)
lbl_course_subject4 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject4.grid(row=5, column=0,padx=2,pady=2)
lbl_course_subject5 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject5.grid(row=6, column=0,padx=2,pady=2)
lbl_course_subject6 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject6.grid(row=7, column=0,padx=2,pady=2)
lbl_course_subject7 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject7.grid(row=8, column=0,padx=2,pady=2)
lbl_course_subject8 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject8.grid(row=9, column=0,padx=2,pady=2)
lbl_course_subject9 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject9.grid(row=10, column=0)
lbl_course_subject10 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject10.grid(row=11, column=0)
lbl_course_subject11 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject11.grid(row=12, column=0)
lbl_course_subject12 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject12.grid(row=13, column=0)
lbl_course_subject13 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject13.grid(row=14, column=0)
lbl_course_subject14 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject14.grid(row=15, column=0)
lbl_course_subject15 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject15.grid(row=16, column=0)
lbl_course_subject16 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject16.grid(row=17, column=0)
lbl_course_subject17 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject17.grid(row=18, column=0)
lbl_course_subject18 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject18.grid(row=19, column=0)
lbl_course_subject19 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject19.grid(row=20, column=0)
lbl_course_subject20 = Label(scrollable_frame,text="",font=("cambria", 10), width= 27,foreground='cyan',highlightthickness=1,highlightcolor="black",highlightbackground="black",background="gray")
lbl_course_subject20.grid(row=21, column=0)

lbl_sub_subject = Label(scrollable_frame, text="SUBJECT",font=("cambria", 8), fg='cyan',bg='gray')
lbl_sub_subject.grid(row=1, column=0)
lbl_test_subject = Label(scrollable_frame, text="TEST\n(40%)", font=("cambria", 8), fg='cyan',bg='gray')
lbl_test_subject.grid(row=1, column=1)
lbl_exam_subject = Label(scrollable_frame, text="EXAM\n(60%)", font=("cambria", 8), fg='cyan',bg='gray')
lbl_exam_subject.grid(row=1, column=2)
lbl_total_subject = Label(scrollable_frame, text="TOTAL\n(100%)",font=("cambria", 8), fg='cyan',bg='gray')
lbl_total_subject.grid(row=1, column=3)
lbl_grade_subject = Label(scrollable_frame, text="GRADE\n(A1 - F9)",font=("cambria", 8), fg='cyan',bg='gray')
lbl_grade_subject.grid(row=1, column=4)
lbl_point_subject = Label(scrollable_frame, text="POINT\n(0-6)",font=("cambria", 8), fg='cyan',bg='gray')
lbl_point_subject.grid(row=1, column=5)


test_course_subject1 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject1.grid(row=2, column=1,padx=3)
exam_course_subject1 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject1.grid(row=2, column=2,padx=3)
total_course_subject1 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject1.grid(row=2, column=3,padx=3)
grade_course_subject1 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject1.grid(row=2, column=4,padx=3)
point_course_subject1 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject1.grid(row=2, column=5,padx=3)

test_course_subject2 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject2.grid(row=3, column=1,padx=2,pady=2)
exam_course_subject2 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject2.grid(row=3, column=2)
total_course_subject2 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject2.grid(row=3, column=3)
grade_course_subject2 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject2.grid(row=3, column=4)
point_course_subject2 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject2.grid(row=3, column=5)

test_course_subject3 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject3.grid(row=4, column=1,padx=2,pady=2)
exam_course_subject3 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject3.grid(row=4, column=2)
total_course_subject3 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject3.grid(row=4, column=3)
grade_course_subject3 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject3.grid(row=4, column=4)
point_course_subject3 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject3.grid(row=4, column=5)

test_course_subject4 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject4.grid(row=5, column=1,padx=2,pady=2)
exam_course_subject4 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject4.grid(row=5, column=2)
total_course_subject4 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject4.grid(row=5, column=3)
grade_course_subject4 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject4.grid(row=5, column=4)
point_course_subject4 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject4.grid(row=5, column=5)

test_course_subject5 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject5.grid(row=6, column=1,padx=2,pady=2)
exam_course_subject5 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject5.grid(row=6, column=2)
total_course_subject5 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject5.grid(row=6, column=3)
grade_course_subject5 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject5.grid(row=6, column=4)
point_course_subject5 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject5.grid(row=6, column=5)

test_course_subject6 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject6.grid(row=7, column=1,padx=2,pady=2)
exam_course_subject6 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject6.grid(row=7, column=2)
total_course_subject6 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject6.grid(row=7, column=3)
grade_course_subject6 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject6.grid(row=7, column=4)
point_course_subject6 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject6.grid(row=7, column=5)

test_course_subject7 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject7.grid(row=8, column=1,padx=2,pady=2)
exam_course_subject7 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject7.grid(row=8, column=2)
total_course_subject7 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject7.grid(row=8, column=3)
grade_course_subject7 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject7.grid(row=8, column=4)
point_course_subject7 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject7.grid(row=8, column=5)

test_course_subject8 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject8.grid(row=9, column=1,padx=2,pady=2)
exam_course_subject8 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject8.grid(row=9, column=2)
total_course_subject8 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject8.grid(row=9, column=3)
grade_course_subject8 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject8.grid(row=9, column=4)
point_course_subject8 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject8.grid(row=9, column=5)

test_course_subject9 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject9.grid(row=10, column=1,padx=2,pady=2)
exam_course_subject9 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject9.grid(row=10, column=2)
total_course_subject9 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject9.grid(row=10, column=3)
grade_course_subject9 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject9.grid(row=10, column=4)
point_course_subject9 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject9.grid(row=10, column=5)

test_course_subject10 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject10.grid(row=11, column=1,padx=2,pady=2)
exam_course_subject10 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject10.grid(row=11, column=2)
total_course_subject10 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject10.grid(row=11, column=3)
grade_course_subject10 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject10.grid(row=11, column=4)
point_course_subject10 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject10.grid(row=11, column=5)

test_course_subject11 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject11.grid(row=12, column=1,padx=2,pady=2)
exam_course_subject11 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject11.grid(row=12, column=2)
total_course_subject11 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject11.grid(row=12, column=3)
grade_course_subject11 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject11.grid(row=12, column=4)
point_course_subject11 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject11.grid(row=12, column=5)

test_course_subject12 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject12.grid(row=13, column=1,padx=2,pady=2)
exam_course_subject12 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject12.grid(row=13, column=2)
total_course_subject12 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject12.grid(row=13, column=3)
grade_course_subject12 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject12.grid(row=13, column=4)
point_course_subject12 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject12.grid(row=13, column=5)

test_course_subject13 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject13.grid(row=14, column=1,padx=2,pady=2)
exam_course_subject13 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject13.grid(row=14, column=2)
total_course_subject13 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject13.grid(row=14, column=3)
grade_course_subject13 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject13.grid(row=14, column=4)
point_course_subject13 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject13.grid(row=14, column=5)

test_course_subject14 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject14.grid(row=15, column=1,padx=2,pady=2)
exam_course_subject14 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject14.grid(row=15, column=2)
total_course_subject14 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject14.grid(row=15, column=3)
grade_course_subject14 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject14.grid(row=15, column=4)
point_course_subject14 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject14.grid(row=15, column=5)

test_course_subject15 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject15.grid(row=16, column=1,padx=2,pady=2)
exam_course_subject15 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject15.grid(row=16, column=2)
total_course_subject15 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject15.grid(row=16, column=3)
grade_course_subject15 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject15.grid(row=16, column=4)
point_course_subject15 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject15.grid(row=16, column=5)

test_course_subject16 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject16.grid(row=17, column=1,padx=2,pady=2)
exam_course_subject16 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject16.grid(row=17, column=2)
total_course_subject16 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject16.grid(row=17, column=3)
grade_course_subject16 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject16.grid(row=17, column=4)
point_course_subject16 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject16.grid(row=17, column=5)

test_course_subject17 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject17.grid(row=18, column=1,padx=2,pady=2)
exam_course_subject17 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject17.grid(row=18, column=2)
total_course_subject17 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject17.grid(row=18, column=3)
grade_course_subject17 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject17.grid(row=18, column=4)
point_course_subject17 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject17.grid(row=18, column=5)

test_course_subject18 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject18.grid(row=19, column=1,padx=2,pady=2)
exam_course_subject18 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject18.grid(row=19, column=2)
total_course_subject18 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject18.grid(row=19, column=3)
grade_course_subject18 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject18.grid(row=19, column=4)
point_course_subject18 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject18.grid(row=19, column=5)

test_course_subject19 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject19.grid(row=20, column=1,padx=2,pady=2)
exam_course_subject19 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject19.grid(row=20, column=2)
total_course_subject19 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject19.grid(row=20, column=3)
grade_course_subject19 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject19.grid(row=20, column=4)
point_course_subject19 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject19.grid(row=20, column=5)

test_course_subject20 = customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
test_course_subject20.grid(row=21, column=1,padx=2,pady=2)
exam_course_subject20 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
exam_course_subject20.grid(row=21, column=2)
total_course_subject20 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
total_course_subject20.grid(row=21, column=3)
grade_course_subject20 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
grade_course_subject20.grid(row=21, column=4)
point_course_subject20 =customtkinter.CTkEntry(scrollable_frame, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5,placeholder_text="0", placeholder_text_color="cyan")
point_course_subject20.grid(row=21, column=5)

#_____________________________________________ SECOND TERM_______________________________________________________________________

lbl_stud_class1 = Label(course_frame1, text="SECOND-TERM SCORE",font=("cambria", 15),bg='gray', fg='cyan')
lbl_stud_class1.grid(row=0, column=0)
scrollable_frame1 = customtkinter.CTkScrollableFrame(course_frame1,bg_color="gray", fg_color="gray", scrollbar_button_hover_color="green", width=450)
scrollable_frame1.grid(row=1, column=0)

sub_subject1 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject1.grid(row=2, column=0,padx=2,pady=2)
sub_subject2 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject2.grid(row=3, column=0,padx=2,pady=2)
sub_subject3 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject3.grid(row=4, column=0,padx=2,pady=2)
sub_subject4 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject4.grid(row=5, column=0,padx=2,pady=2)
sub_subject5 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject5.grid(row=6, column=0,padx=2,pady=2)
sub_subject6 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject6.grid(row=7, column=0,padx=2,pady=2)
sub_subject7 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject7.grid(row=8, column=0,padx=2,pady=2)
sub_subject8 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject8.grid(row=9, column=0,padx=2,pady=2)
sub_subject9 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject9.grid(row=10, column=0)
sub_subject10 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject10.grid(row=11, column=0)
sub_subject11 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject11.grid(row=12, column=0)
sub_subject12 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject12.grid(row=13, column=0)
sub_subject13 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject13.grid(row=14, column=0)
sub_subject14 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject14.grid(row=15, column=0)
sub_subject15 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject15.grid(row=16, column=0)
sub_subject16 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject16.grid(row=17, column=0)
sub_subject17 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject17.grid(row=18, column=0)
sub_subject18 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject18.grid(row=19, column=0)
sub_subject19 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject19.grid(row=20, column=0)
sub_subject20 = customtkinter.CTkEntry(scrollable_frame1, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
sub_subject20.grid(row=21, column=0)

lbl_sub_subject1 = Label(scrollable_frame1, text="SUBJECT",font=("cambria", 10), fg='cyan',bg='gray')
lbl_sub_subject1.grid(row=1, column=0)
lbl_test_subject1 = Label(scrollable_frame1, text="TEST", font=("cambria", 10), fg='cyan',bg='gray')
lbl_test_subject1.grid(row=1, column=1)
lbl_exam_subject1 = Label(scrollable_frame1, text="EXAM", font=("cambria", 10), fg='cyan',bg='gray')
lbl_exam_subject1.grid(row=1, column=2)
lbl_total_subject1 = Label(scrollable_frame1, text="TOTAL",font=("cambria", 10), fg='cyan',bg='gray')
lbl_total_subject1.grid(row=1, column=3)
lbl_grade_subject1 = Label(scrollable_frame1, text="GRADE",font=("cambria", 10), fg='cyan',bg='gray')
lbl_grade_subject1.grid(row=1, column=4)


test_sub_subject1 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject1.grid(row=2, column=1,padx=5)
exam_sub_subject1 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject1.grid(row=2, column=2)
total_sub_subject1 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject1.grid(row=2, column=3)
grade_sub_subject1 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject1.grid(row=2, column=4)


test_sub_subject2 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject2.grid(row=3, column=1,padx=2,pady=2)
exam_sub_subject2 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject2.grid(row=3, column=2)
total_sub_subject2 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject2.grid(row=3, column=3)
grade_sub_subject2 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject2.grid(row=3, column=4)

test_sub_subject3 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject3.grid(row=4, column=1,padx=2,pady=2)
exam_sub_subject3 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject3.grid(row=4, column=2)
total_sub_subject3 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject3.grid(row=4, column=3)
grade_sub_subject3 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject3.grid(row=4, column=4)

test_sub_subject4 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject4.grid(row=5, column=1,padx=2,pady=2)
exam_sub_subject4 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject4.grid(row=5, column=2)
total_sub_subject4 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject4.grid(row=5, column=3)
grade_sub_subject4 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject4.grid(row=5, column=4)

test_sub_subject5 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject5.grid(row=6, column=1,padx=2,pady=2)
exam_sub_subject5 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject5.grid(row=6, column=2)
total_sub_subject5 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject5.grid(row=6, column=3)
grade_sub_subject5 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject5.grid(row=6, column=4)

test_sub_subject6 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject6.grid(row=7, column=1,padx=2,pady=2)
exam_sub_subject6 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject6.grid(row=7, column=2)
total_sub_subject6 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject6.grid(row=7, column=3)
grade_sub_subject6 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject6.grid(row=7, column=4)

test_sub_subject7 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject7.grid(row=8, column=1,padx=2,pady=2)
exam_sub_subject7 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject7.grid(row=8, column=2)
total_sub_subject7 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject7.grid(row=8, column=3)
grade_sub_subject7 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject7.grid(row=8, column=4)

test_sub_subject8 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject8.grid(row=9, column=1,padx=2,pady=2)
exam_sub_subject8 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject8.grid(row=9, column=2)
total_sub_subject8 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject8.grid(row=9, column=3)
grade_sub_subject8 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject8.grid(row=9, column=4)

test_sub_subject9 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject9.grid(row=10, column=1,padx=2,pady=2)
exam_sub_subject9 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject9.grid(row=10, column=2)
total_sub_subject9 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject9.grid(row=10, column=3)
grade_sub_subject9 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject9.grid(row=10, column=4)

test_sub_subject10 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject10.grid(row=11, column=1,padx=2,pady=2)
exam_sub_subject10 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject10.grid(row=11, column=2)
total_sub_subject10 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject10.grid(row=11, column=3)
grade_sub_subject10 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject10.grid(row=11, column=4)

test_sub_subject11 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject11.grid(row=12, column=1,padx=2,pady=2)
exam_sub_subject11 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject11.grid(row=12, column=2)
total_sub_subject11 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject11.grid(row=12, column=3)
grade_sub_subject11 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject11.grid(row=12, column=4)

test_sub_subject12 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject12.grid(row=13, column=1,padx=2,pady=2)
exam_sub_subject12 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject12.grid(row=13, column=2)
total_sub_subject12 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject12.grid(row=13, column=3)
grade_sub_subject12 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject12.grid(row=13, column=4)

test_sub_subject13 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject13.grid(row=14, column=1,padx=2,pady=2)
exam_sub_subject13 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject13.grid(row=14, column=2)
total_sub_subject13 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject13.grid(row=14, column=3)
grade_sub_subject13 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject13.grid(row=14, column=4)

test_sub_subject14 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject14.grid(row=15, column=1,padx=2,pady=2)
exam_sub_subject14 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject14.grid(row=15, column=2)
total_sub_subject14 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject14.grid(row=15, column=3)
grade_sub_subject14 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject14.grid(row=15, column=4)

test_sub_subject15 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject15.grid(row=16, column=1,padx=2,pady=2)
exam_sub_subject15 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject15.grid(row=16, column=2)
total_sub_subject15 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject15.grid(row=16, column=3)
grade_sub_subject15 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject15.grid(row=16, column=4)

test_sub_subject16 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject16.grid(row=17, column=1,padx=2,pady=2)
exam_sub_subject16 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject16.grid(row=17, column=2)
total_sub_subject16 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject16.grid(row=17, column=3)
grade_sub_subject16 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject16.grid(row=17, column=4)

test_sub_subject17 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject17.grid(row=18, column=1,padx=2,pady=2)
exam_sub_subject17 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject17.grid(row=18, column=2)
total_sub_subject17 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject17.grid(row=18, column=3)
grade_sub_subject17 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject17.grid(row=18, column=4)

test_sub_subject18 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject18.grid(row=19, column=1,padx=2,pady=2)
exam_sub_subject18 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject18.grid(row=19, column=2)
total_sub_subject18 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject18.grid(row=19, column=3)
grade_sub_subject18 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject18.grid(row=19, column=4)

test_sub_subject19 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject19.grid(row=20, column=1,padx=2,pady=2)
exam_sub_subject19 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject19.grid(row=20, column=2)
total_sub_subject19 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject19.grid(row=20, column=3)
grade_sub_subject19 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject19.grid(row=20, column=4)

test_sub_subject20 = customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_sub_subject20.grid(row=21, column=1,padx=2,pady=2)
exam_sub_subject20 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_sub_subject20.grid(row=21, column=2)
total_sub_subject20 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_sub_subject20.grid(row=21, column=3)
grade_sub_subject20 =customtkinter.CTkEntry(scrollable_frame1, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_sub_subject20.grid(row=21, column=4)

# _______________________________________________________ third term__________________________________________________________________________
lbl_stud_class2 = Label(course_frame2, text="THIRD-TERM SCORE",font=("cambria", 15),bg='gray', fg='cyan')
lbl_stud_class2.grid(row=0, column=0)

scrollable_frame2 = customtkinter.CTkScrollableFrame(course_frame2,bg_color="gray", fg_color="gray", scrollbar_button_hover_color="green", width=450)
scrollable_frame2.grid(row=1, column=0)

lbl_subs_subject1 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject1.grid(row=2, column=0,padx=2,pady=2)
lbl_subs_subject2 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject2.grid(row=3, column=0,padx=2,pady=2)
lbl_subs_subject3 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject3.grid(row=4, column=0,padx=2,pady=2)
lbl_subs_subject4 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject4.grid(row=5, column=0,padx=2,pady=2)
lbl_subs_subject5 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject5.grid(row=6, column=0,padx=2,pady=2)
lbl_subs_subject6 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject6.grid(row=7, column=0,padx=2,pady=2)
lbl_subs_subject7 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject7.grid(row=8, column=0,padx=2,pady=2)
lbl_subs_subject8 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject8.grid(row=9, column=0,padx=2,pady=2)
lbl_subs_subject9 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject9.grid(row=10, column=0)
lbl_subs_subject10 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject10.grid(row=11, column=0)
lbl_subs_subject11 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject11.grid(row=12, column=0)
lbl_subs_subject12 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject12.grid(row=13, column=0)
lbl_subs_subject13 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject13.grid(row=14, column=0)
lbl_subs_subject14 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject14.grid(row=15, column=0)
lbl_subs_subject15 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject15.grid(row=16, column=0)
lbl_subs_subject16 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject16.grid(row=17, column=0)
lbl_subs_subject17 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject17.grid(row=18, column=0)
lbl_subs_subject18 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject18.grid(row=19, column=0)
lbl_subs_subject19 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject19.grid(row=20, column=0)
lbl_subs_subject20 = customtkinter.CTkEntry(scrollable_frame2, width= 200, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
lbl_subs_subject20.grid(row=21, column=0)

lbl_subs_subject1 = Label(scrollable_frame2, text="SUBJECT",font=("cambria", 10), fg='cyan',bg='gray')
lbl_subs_subject1.grid(row=1, column=0)
lbl_tests_subject1 = Label(scrollable_frame2, text="TEST", font=("cambria", 10), fg='cyan',bg='gray')
lbl_tests_subject1.grid(row=1, column=1)
lbl_exams_subject1 = Label(scrollable_frame2, text="EXAM", font=("cambria", 10), fg='cyan',bg='gray')
lbl_exams_subject1.grid(row=1, column=2)
lbl_totals_subject1 = Label(scrollable_frame2, text="TOTAL",font=("cambria", 10), fg='cyan',bg='gray')
lbl_totals_subject1.grid(row=1, column=3)
lbl_grades_subject1 = Label(scrollable_frame2, text="GRADE",font=("cambria", 10), fg='cyan',bg='gray')
lbl_grades_subject1.grid(row=1, column=4)


test_subs_subject1 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject1.grid(row=2, column=1,padx=5)
exam_subs_subject1 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject1.grid(row=2, column=2)
total_subs_subject1 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject1.grid(row=2, column=3)
grade_subs_subject1 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject1.grid(row=2, column=4)


test_subs_subject2 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject2.grid(row=3, column=1,padx=2,pady=2)
exam_subs_subject2 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject2.grid(row=3, column=2)
total_subs_subject2 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject2.grid(row=3, column=3)
grade_subs_subject2 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject2.grid(row=3, column=4)

test_subs_subject3 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject3.grid(row=4, column=1,padx=2,pady=2)
exam_subs_subject3 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject3.grid(row=4, column=2)
total_subs_subject3 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject3.grid(row=4, column=3)
grade_subs_subject3 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject3.grid(row=4, column=4)

test_subs_subject4 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject4.grid(row=5, column=1,padx=2,pady=2)
exam_subs_subject4 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject4.grid(row=5, column=2)
total_subs_subject4 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject4.grid(row=5, column=3)
grade_subs_subject4 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject4.grid(row=5, column=4)

test_subs_subject5 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject5.grid(row=6, column=1,padx=2,pady=2)
exam_subs_subject5 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject5.grid(row=6, column=2)
total_subs_subject5 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject5.grid(row=6, column=3)
grade_subs_subject5 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject5.grid(row=6, column=4)

test_subs_subject6 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject6.grid(row=7, column=1,padx=2,pady=2)
exam_subs_subject6 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject6.grid(row=7, column=2)
total_subs_subject6 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject6.grid(row=7, column=3)
grade_subs_subject6 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject6.grid(row=7, column=4)

test_subs_subject7 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject7.grid(row=8, column=1,padx=2,pady=2)
exam_subs_subject7 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject7.grid(row=8, column=2)
total_subs_subject7 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject7.grid(row=8, column=3)
grade_subs_subject7 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject7.grid(row=8, column=4)

test_subs_subject8 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject8.grid(row=9, column=1,padx=2,pady=2)
exam_subs_subject8 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject8.grid(row=9, column=2)
total_subs_subject8 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject8.grid(row=9, column=3)
grade_subs_subject8 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject8.grid(row=9, column=4)

test_subs_subject9 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject9.grid(row=10, column=1,padx=2,pady=2)
exam_subs_subject9 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject9.grid(row=10, column=2)
total_subs_subject9 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject9.grid(row=10, column=3)
grade_subs_subject9 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject9.grid(row=10, column=4)

test_subs_subject10 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject10.grid(row=11, column=1,padx=2,pady=2)
exam_subs_subject10 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject10.grid(row=11, column=2)
total_subs_subject10 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject10.grid(row=11, column=3)
grade_subs_subject10 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject10.grid(row=11, column=4)

test_subs_subject11 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject11.grid(row=12, column=1,padx=2,pady=2)
exam_subs_subject11 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject11.grid(row=12, column=2)
total_subs_subject11 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject11.grid(row=12, column=3)
grade_subs_subject11 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject11.grid(row=12, column=4)

test_subs_subject12 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject12.grid(row=13, column=1,padx=2,pady=2)
exam_subs_subject12 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject12.grid(row=13, column=2)
total_subs_subject12 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject12.grid(row=13, column=3)
grade_subs_subject12 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject12.grid(row=13, column=4)

test_subs_subject13 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject13.grid(row=14, column=1,padx=2,pady=2)
exam_subs_subject13 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject13.grid(row=14, column=2)
total_subs_subject13 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject13.grid(row=14, column=3)
grade_subs_subject13 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject13.grid(row=14, column=4)

test_subs_subject14 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject14.grid(row=15, column=1,padx=2,pady=2)
exam_subs_subject14 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject14.grid(row=15, column=2)
total_subs_subject14 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject14.grid(row=15, column=3)
grade_subs_subject14 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject14.grid(row=15, column=4)

test_subs_subject15 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject15.grid(row=16, column=1,padx=2,pady=2)
exam_subs_subject15 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject15.grid(row=16, column=2)
total_subs_subject15 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject15.grid(row=16, column=3)
grade_subs_subject15 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject15.grid(row=16, column=4)

test_subs_subject16 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject16.grid(row=17, column=1,padx=2,pady=2)
exam_subs_subject16 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject16.grid(row=17, column=2)
total_subs_subject16 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject16.grid(row=17, column=3)
grade_subs_subject16 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject16.grid(row=17, column=4)

test_subs_subject17 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject17.grid(row=18, column=1,padx=2,pady=2)
exam_subs_subject17 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject17.grid(row=18, column=2)
total_subs_subject17 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject17.grid(row=18, column=3)
grade_subs_subject17 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject17.grid(row=18, column=4)

test_subs_subject18 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject18.grid(row=19, column=1,padx=2,pady=2)
exam_subs_subject18 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject18.grid(row=19, column=2)
total_subs_subject18 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject18.grid(row=19, column=3)
grade_subs_subject18 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject18.grid(row=19, column=4)

test_subs_subject19 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject19.grid(row=20, column=1,padx=2,pady=2)
exam_subs_subject19 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject19.grid(row=20, column=2)
total_subs_subject19 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject19.grid(row=20, column=3)
grade_subs_subject19 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject19.grid(row=20, column=4)

test_subs_subject20 = customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
test_subs_subject20.grid(row=21, column=1,padx=2,pady=2)
exam_subs_subject20 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
exam_subs_subject20.grid(row=21, column=2)
total_subs_subject20 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
total_subs_subject20.grid(row=21, column=3)
grade_subs_subject20 =customtkinter.CTkEntry(scrollable_frame2, width= 50, height=25,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
grade_subs_subject20.grid(row=21, column=4)

btn_calculate = customtkinter.CTkButton(verification_frame, text="CALCULATE",font=("cambria",14),text_color="cyan", width=100, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="orange", command=r_cal)
btn_calculate.grid(row=0, column=0, padx=2)
btn_upload = customtkinter.CTkButton(verification_frame, text="UPLOAD",font=("cambria",14),text_color="cyan", width=100, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="green", command=r_reg)
btn_upload.grid(row=0, column=1, padx=2)
btn_clear = customtkinter.CTkButton(verification_frame, text="CLEAR",font=("cambria",14),text_color="cyan", width=100, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="orange", command=r_clear)
btn_clear.grid(row=0, column=2, padx=2)

btn_exit_result = customtkinter.CTkButton(verification_frame, text="EXIT",font=("cambria",14),text_color="cyan", width=100, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="red", command= close)
btn_exit_result.grid(row=0, column=3, padx=2)


#____________________________________________View Frame________________________________________________________________________

stud_view_frame = LabelFrame(result_view_frame,text= "VIEW STUDENT RESULT", font = ("cambria", 10), bg="gray", fg="cyan")
stud_view_frame.pack(pady=20)

# lbl_Stud_view = Label(stud_view_frame, text="VIEW RESULT", font=("arial black", 12),bg="gray", fg='cyan')
# lbl_Stud_view.grid(row=0, column=0)

search_view_frame = LabelFrame(stud_view_frame, bg="gray",fg="cyan")
search_view_frame.grid(row=0, column=0)
view_stud_info_frame = LabelFrame(stud_view_frame,bg="gray")
view_stud_info_frame.grid(row=1, column=0)
# view_course_frame = Frame(result_view_frame,bg="gray",highlightthickness=2)
# course_frame.grid_forget()
# course_frame1 = Frame(result_view_frame,bg="gray",highlightthickness=2)
# course_frame1.grid_forget()
# course_frame2 = Frame(result_view_frame,bg="gray",highlightthickness=2)
# course_frame2.grid_forget()
# view_stud_frame = Frame(stud_view_frame,bg="gray",highlightthickness=2)
# view_stud_frame.grid(row=3, column=0, pady=3,columnspan=2)
# view_pane = Label(stud_view_frame, width= 70, height=10,bg="gray",highlightthickness=2)
# view_pane.grid(row=3,column=0, pady=3)
# verification_frame1 = LabelFrame(stud_view_frame,bg="gray")
# verification_frame1.grid(row=1, column=1, pady=3)

def view_search_me():
    pass

txt_search_view = customtkinter.CTkEntry(search_view_frame,width=115, height= 20,font=("cambria", 12),bg_color="gray", fg_color="gray",placeholder_text="Enter Student I.D",placeholder_text_color="cyan",border_width=2,)
txt_search_view.focus_set()
txt_search_view.grid(row=0,column=0, padx=2)
btn_search_view = customtkinter.CTkButton(search_view_frame, text="SEARCH",font=("cambria",10),text_color="cyan", width=50, height=20, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="green", command= view_search_me)
btn_search_view.grid(row=0, column=1, padx=2)
btn_print = customtkinter.CTkButton(search_view_frame, text="PRINT",font=("cambria",10),text_color="cyan", width=50, height=20, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="cyan", command= view_search_me)
btn_print.grid(row=1, column=1, padx=2)
btn_view_clear = customtkinter.CTkButton(search_view_frame, text="CLEAR",font=("cambria",10),text_color="cyan", width=50, height=20, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="orange", command= r_clear)
btn_view_clear.grid(row=0, column=2, padx=2)
btn_view_exit = customtkinter.CTkButton(search_view_frame, text="EXIT",font=("cambria",10),text_color="cyan", width=50, height=20, bg_color="gray", fg_color="gray", corner_radius=10,hover_color="red", command= close)
btn_view_exit.grid(row=1, column=2, padx=2)


lbl_view_name = Label(view_stud_info_frame, text="FULL NAME",font=("cambria", 10),bg='gray', fg='cyan')
lbl_view_name.grid(row=0, column=0)
lbl_view_stud_gender = Label(view_stud_info_frame, text="GENDER",font=("cambria", 10),bg='gray', fg='cyan')
lbl_view_stud_gender.grid(row=0, column=1)
lbl_view_stud_class = Label(view_stud_info_frame, text="CLASS",font=("cambria", 10),bg='gray', fg='cyan')
lbl_view_stud_class.grid(row=0, column=2)
lbl_view_stud_reg_num = Label(view_stud_info_frame, text="REG. NO.",font=("cambria", 10),bg='gray', fg='cyan')
lbl_view_stud_reg_num.grid(row=0, column=3)


name_view = customtkinter.CTkEntry(view_stud_info_frame,width= 250, height= 20,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
name_view.grid(row=1, column=0, padx=2)
stud_gender_view = customtkinter.CTkEntry(view_stud_info_frame,width= 60, height= 20,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_gender_view.grid(row=1, column=1, padx=2)
stud_class_view =customtkinter.CTkEntry(view_stud_info_frame,width= 60, height= 20,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_class_view.grid(row=1, column=2,padx=2)
stud_reg_num_view = customtkinter.CTkEntry(view_stud_info_frame,width= 115, height= 20,font=("cambria", 10),bg_color='gray', fg_color='gray',text_color="cyan", corner_radius=5)
stud_reg_num_view.grid(row=1, column=3)

        
term1 =[
    "SELECT TERM",
    "FIRST TERM",
    "SECOND TERM",
    "THIRD TERM"
]

def pick_term1(e):
    if opt_term.get() == "FIRST TERM":
        course_frame1.grid_forget()
        course_frame2.grid_forget()
        course_frame.grid(row=3, column=0,pady=5)
        
        
    elif opt_term.get() == "SECOND TERM":
        course_frame.grid_forget()
        course_frame2.grid_forget()
        course_frame1.grid(row=3, column=0,pady=5)

        
    elif opt_term.get() == "THIRD TERM":
        course_frame.grid_forget()
        course_frame1.grid_forget()
        course_frame2.grid(row=3, column=0,pady=5)

    
    else:
        course_frame.grid_forget()
        course_frame1.grid_forget()
        course_frame2.grid_forget()
        

opt_term1 = ttk.Combobox(search_view_frame, value= term1 ,width=13, foreground="cyan",background="gray",font=("cambria", 10), height=20)
opt_term1.current(0)
opt_term1.bind("<<ComboboxSelected>>", pick_term1)
opt_term1.grid(row=1, column=0,pady=5)

style = ttk.Style()

style.theme_use("default")
style.configure("Treeview",
                background= "gray",
                foreground ="gray",
                rowheight = 20,
                )
style.map('Treeview',
          background=[('selected','green')])

result_view_tree = ttk.Treeview(stud_view_frame)
result_view_tree['columns'] = ("Subject","Test","Exam","Total","Grade","Point")
result_view_tree.column("#0", width=0, stretch=NO)
result_view_tree.column("Subject",anchor =W, width=150, minwidth=20)
result_view_tree.column("Test",anchor =W, width=50, minwidth=20)
result_view_tree.column("Exam",anchor =CENTER, width=50, minwidth=20)
result_view_tree.column("Total",anchor =CENTER, width=50, minwidth=20)
result_view_tree.column("Grade",anchor =W, width=50, minwidth=20)
result_view_tree.column("Point",anchor =W, width=50, minwidth=20)

# ___________________________________ HEADINGS_______________________________
result_view_tree.heading("#0", text= "", anchor= W)
result_view_tree.heading("Subject",text = "Subject",anchor =W)
result_view_tree.heading("Test",text = "Test",anchor =W)
result_view_tree.heading("Exam",text = "Exam",anchor =CENTER)
result_view_tree.heading("Total",text = "Total",anchor =CENTER)
result_view_tree.heading("Grade",text = "Grade",anchor =W)
result_view_tree.heading("Point",text = "Point",anchor =W)

result_view_tree.insert(parent = '', index= 'end', iid=0, values=())

result_view_tree.grid(row=2, column=0, pady=5)

me.mainloop()