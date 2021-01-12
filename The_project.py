import mysql.connector
import tkinter.messagebox
from tkinter import *
from tkinter import ttk


mydb = mysql.connector.connect(host = "localhost",
                               user ="root",
                               )

db = mydb.cursor()
db.execute("show databases")
lst = db.fetchall()
if ("school_project",) in lst :
    db.execute("use school_project")
    print("Databasse exists")
else :
    db.execute("""create database school_project""")
    db.execute("use school_project")

db.execute("show tables")
tbls = db.fetchall()
if ("inventory",) in tbls :

    print("Table is present")
    pass
else :
    db.execute("""create table inventory ( 
    Product_ID int(5) primary key,
    Product_Name varchar(20),
    Price varchar(10),
    Quantity varchar(10),
    Company varchar(20),
    Contact varchar(10),
    address varchar(30))""")
    print("Table is created")


def clear_button_2_is_clicked():
    Field.delete(*Field.get_children())


def search_button_is_clicked():
    cur = mydb.cursor()
    select = ("select * from inventory where "+str(Search.get()) +" = '" + str(Entry1.get())+"'")
    cur.execute(select)
    rows = cur.fetchall()
    if len(rows) != 0:
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()

    else :
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()



def update_2_is_clicked():
    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row =content['values']
    Product_ID.set(row[0])
    Product_Name.set(row[1])
    Price.set(row[2])
    Quantity.set(row[3])
    Company.set(row[4])
    Contact.set(row[5])
    ADDRESS_txt.delete("1.0", END)
    ADDRESS_txt.insert(END,row[6])

def add_btn():
    ADDRESS = ADDRESS_txt.get('1.0',END)
    cur = mydb.cursor()
    insert = "INSERT INTO Inventory values (%s,%s,%s,%s,%s,%s,%s)"
    values =(Product_ID.get(),
             Product_Name.get(),
             Price.get(),
             Quantity.get(),
             Company.get(),
             Contact.get(),
             ADDRESS.rstrip()
             )
    cur.execute(insert,values)
    mydb.commit()


    cur = mydb.cursor()
    select = "select * from inventory"
    cur.execute(select)
    rows = cur.fetchall()
    if len(rows) != 0:
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()

def search_all_bth():
    cur = mydb.cursor()
    select = "select * from inventory "
    cur.execute(select)
    rows = cur.fetchall()
    Field.delete(* Field.get_children())
    for row in rows :
        Field.insert('',END,values = row)
        mydb.commit()

def delete_button_is_clicked():

    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row = content['values']
    cur = mydb.cursor()
    select = (f"delete from inventory where Product_ID = {row[0]}")
    cur.execute(select)
    mydb.commit()
    search_all_bth()

def clear_button_is_clicked():
    ID_txt.delete(0,END)
    NAME_txt.delete(0, END)
    PRICE_txt.delete(0, END)
    CONTACT_txt.delete(0, END)
    COMPANY_txt.delete(0, END)
    QUANTITY_txt.delete(0, END)
    ADDRESS_txt.delete("1.0",END)

def update_button_is_clicked():

    ADDRESS = ADDRESS_txt.get('1.0', END)
    cur = mydb.cursor()
    insert = '''UPDATE Inventory set
     Product_Name=%s,
     Price=%s,
     Quantity = %s,
     Company=%s,
     Contact=%s,
     address=%s 
     where Product_ID=%s '''
    values = (
              Product_Name.get(),
              Price.get(),
              Quantity.get(),
              Company.get(),
              Contact.get(),
              ADDRESS.rstrip(),
              Product_ID.get()
    )
    cur.execute(insert, values)
    mydb.commit()
    cur = mydb.cursor()
    select = "select * from inventory"
    cur.execute(select)
    rows = cur.fetchall()
    if len(rows) != 0:
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()




def product_details():
    pop = Toplevel()
    pop.title("Prodcut Details ")
    ws = pop.winfo_screenwidth()
    hs = pop.winfo_screenheight()
    w = 630
    h = 280
    x = int(ws / 2 - w / 2 - 20)
    y = int(hs / 2 - h / 2 - 30)
    data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
    pop.geometry(data)
    pop.configure(bg="#ffffff")
    pop.resizable(0, 0)
    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row = content['values']
    label1 = Label(pop, text=(f"Product ID "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label1.grid(row=0, column=0, sticky="w", padx=30)

    label2 = Label(pop, text=(f"Product Name"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label2.grid(row=1, column=0, sticky="w", padx=30)

    label3 = Label(pop, text=(f"Price "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label3.grid(row=2, column=0, sticky="w", padx=30)

    label4 = Label(pop, text=(f"Quantity"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label4.grid(row=3, column=0, sticky="w", padx=30)

    label5 = Label(pop, text=(f"Mfg Company "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label5.grid(row=4, column=0, sticky="w", padx=30)

    label6 = Label(pop, text=(f"Phone No"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label6.grid(row=5, column=0, sticky="w", padx=30, pady=(0, 0))

    label7 = Label(pop, text=(f"Address"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))
    label7.grid(row=6, column=0, sticky="w", padx=30, pady=(0, 0))



    label8 = Label(pop, text=(f":    {row[0]}"), bg="#ffffff",fg = "#676767", anchor=W,
                   font=("Times New Roman", 19, "bold"))
    label8.grid(row=0, column=1, sticky="w")

    label9 = Label(pop, text=(f":    {row[1]}"), bg="#ffffff",fg = "#676767", anchor=W,
                   font=("Times New Roman", 19, "bold"))
    label9.grid(row=1, column=1, sticky="w")

    label10 = Label(pop, text=(f":    {row[2]}"), bg="#ffffff",fg = "#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label10.grid(row=2, column=1, sticky="w")

    label11 = Label(pop, text=(f":    {row[3]}"), bg="#ffffff",fg = "#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label11.grid(row=3, column=1, sticky="w")

    label12 = Label(pop, text=(f":    {row[4]}"), bg="#ffffff",fg = "#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label12.grid(row=4, column=1, sticky="w")

    label13 = Label(pop, text=(f":    {row[5]}"), bg="#ffffff",fg = "#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label13.grid(row=5, column=1, sticky="w")

    label14 = Label(pop, text=(f":    {row[6]}"), bg="#ffffff",fg = "#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label14.grid(row=6, column=1, sticky="w", )


    label15 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                   font=("Times New Roman", 22, "bold"))
    label15.grid(row=0, column=1, sticky="w")
    label16 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                   font=("Times New Roman", 22, "bold"))
    label16.grid(row=1, column=1, sticky="w")
    label17 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                    font=("Times New Roman", 22, "bold"))
    label17.grid(row=2, column=1, sticky="w")
    label18 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                    font=("Times New Roman", 22, "bold"))
    label18.grid(row=3, column=1, sticky="w")
    label19 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                    font=("Times New Roman", 22, "bold"))
    label19.grid(row=4, column=1, sticky="w")
    label20 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                    font=("Times New Roman", 22, "bold"))
    label20.grid(row=5, column=1, sticky="w")
    label21 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,
                    font=("Times New Roman", 22, "bold"))
    label21.grid(row=6, column=1, sticky="w", )


root = tkinter.Tk()
root.title("Warehouse Inventory Sales Purchase Management System   \U0001f130 \U0001f131 \U0001f137")
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 1350
h = 703
x = int(ws / 2 - w / 2 - 20)
y = int(hs / 2 - h / 2 - 30)
data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
root.geometry(data)
root.configure(bg="#ffffff")
root.resizable(0, 0)

#*************************************Frame 1  (Title)**************

title_frame = LabelFrame()
title_frame.pack(fill="x")

title = Label(title_frame,
              text="Warehouse Inventory Purchase Management System",
              font=("Comic Sans MS", 25, "bold"),
              bg="#00e6a1",
              fg="#ffffff",
              anchor="center",
              bd=4)
title.pack(expand=True, fil="x")

# ************************************ Frame 2 (Border Line)*****

f2 = Label(root, text=" ", font=("Comic Sans MS", 15, "bold", "italic"), bg="#cacaca", bd=1)
f2.place(x=0, y=55, relwidth=50)

# ************************************ Frame 3 (Entry)*****

Manage_Frame_canvas = Frame(root, bd=2, relief=GROOVE, )
Manage_Frame_canvas.place(x=13, y=95, width=459, height=545)

Manage_Frame = Frame(root, bd=1, bg="#fff000", relief=GROOVE, )
Manage_Frame.place(x=13, y=95, width=457, height=470)

Manage_Frame3 = LabelFrame(Manage_Frame, text=" Put the Details", font=("Comic Sans MS", 22, "bold", "italic"),
                           fg="#ffffff", bd=0, bg="#fff000", relief=SUNKEN, )
Manage_Frame3.place(y=0, x=0, width=457, height=545)

# ***************************************** Variables For Entering Data **********

Product_ID =StringVar()
Product_Name =StringVar()
Price =StringVar()
Quantity =StringVar()
Contact =StringVar()
Company =StringVar()

# **********************  Labels and Entries_____________

ID_lbl = Label(Manage_Frame, text="Product ID", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
ID_lbl.grid(row=1, column=0, pady=(50, 0), padx=20, sticky="w")

ID_txt = Entry(Manage_Frame,textvariable =Product_ID, width=18, font=("Comic Sans MS", 15), fg="#000000", bd=1, relief=GROOVE, )
ID_txt.grid(row=1, column=2, sticky="w", pady=(50, 0))

NAME_lbl = Label(Manage_Frame, text="Product Name", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
NAME_lbl.grid(row=2, column=0, pady=10, padx=20, sticky="w")

NAME_txt = Entry(Manage_Frame,textvariable =Product_Name ,width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
NAME_txt.grid(row=2, column=2, sticky="w")

PRICE_lbl = Label(Manage_Frame, text="Product Price", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
PRICE_lbl.grid(row=3, column=0, pady=10, padx=20, sticky="w")

PRICE_txt = Entry(Manage_Frame,textvariable =Price, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
PRICE_txt.grid(row=3, column=2, sticky="w")

QUANTITY_lbl = Label(Manage_Frame, text="Quantity", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
QUANTITY_lbl.grid(row=4, column=0, pady=10, padx=20, sticky="w")

QUANTITY_txt = Entry(Manage_Frame,textvariable =Quantity, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
QUANTITY_txt.grid(row=4, column=2, sticky="w")

COMPANY_lbl = Label(Manage_Frame, text="Mfg Company", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
COMPANY_lbl.grid(row=5, column=0, pady=10, padx=20, sticky="w")
COMPANY_txt = Entry(Manage_Frame,textvariable =Company, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
COMPANY_txt.grid(row=5, column=2, sticky="w")

CONTACT_lbl = Label(Manage_Frame, text="Phone.No", bg="#fff000", fg="#ffffff",font=("Comic Sans MS", 19, "bold"))
CONTACT_lbl.grid(row=6, column=0, pady=10, padx=20, sticky="w")

CONTACT_txt = Entry(Manage_Frame,textvariable =Contact , width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
CONTACT_txt.grid(row=6, column=2, sticky="w")

ADDRESS_lbl = Label(Manage_Frame, text="Mfg Address", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
ADDRESS_lbl.grid(row=7, column=0, pady=10, padx=20, sticky="w")

ADDRESS_txt = Text(Manage_Frame, width=27, height=2, fg="#000000", bd=1 / 2, relief=GROOVE, )
ADDRESS_txt.grid(row=7, column=2, sticky="w")


# ***************************************** Frame 3 (Button Frame 1)*****

button_frame1 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")
button_frame1.place(x=13, y=575, width=455, height=54, )

# ******************************************* Buttons (For Frame 3 ) _______________

add_btn = Button(button_frame1, width=10, text="Add", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                         fg="#000000", relief=SUNKEN,command = add_btn).grid(row=0, column=0, padx=4, pady=7)

update_btn = Button(button_frame1, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                            bg="#ffffff", fg="#000000", relief=SUNKEN,command = update_button_is_clicked).grid(row=0, column=1, padx=1, pady=7)

clear_btn = Button(button_frame1, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                            bg="#ffffff", fg="#000000", relief=SUNKEN,command = clear_button_is_clicked).grid(row=0, column=2, padx=2, pady=7)

cancel_btn = Button(button_frame1, width=10, text="Cancel", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                           fg="#000000", relief=SUNKEN,command =clear_button_is_clicked).grid(row=0, column=3, padx=2, pady=7)

#*********************************************Frame 4 ( For Management ) ************************

Main_Frame = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Main_Frame.place(x=480, y=95, width=856, height=544)

#**********************************************Frame 5 (For Searching)**************************

Searching_Frame = Frame(root, bd=1, relief=RIDGE, )
Searching_Frame.place(x=480, y=95, width=856, height=54)

Search_By_Label = Label(Searching_Frame, text="Search By", fg="#676767", font=("Comic Sans MS", 17, "bold"))
Search_By_Label.grid(row=0, column=0, pady=10, padx=20, sticky="w")

Search =StringVar()
Combo_Search = ttk.Combobox(Searching_Frame,textvariable = Search, font=("Comic Sans MS", 14), width=11, state="readonly")

Combo_Search["values"] = ("Product_ID", "Product_Name","Price","Company","Contact","Quantity","Address")
Combo_Search.grid(row=0, column=1)


Entry1 = StringVar()
Search_Bar = Entry(Searching_Frame,textvariable = Entry1, width=16, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
Search_Bar.grid(row=0, column=2, sticky="w", padx=27)

Search_Button = Button(Searching_Frame, width=10, text="Search", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,bg="#ffffff",
                    fg="#000000", relief=SUNKEN,command = search_button_is_clicked).grid(row=0, column=3, padx=(10, 0), pady=7, sticky="e")

Search_All_Button = Button(Searching_Frame, width=10, text="Search All", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                            bg="#ffffff",
                            fg="#000000", relief=SUNKEN,command =search_all_bth).grid(row=0, column=4, padx=20, pady=7, sticky="e")

#*******************************************************Frame 6 (Database Window)*********************

Database_Window = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Database_Window.place(x=480, y=148, width=856, height=415)

#********************************************************* Scrrollbars () *****************************

Horizontal_Scrollbar = Scrollbar(Database_Window, orient=HORIZONTAL)
Vertical_Scrollbar = Scrollbar(Database_Window, orient=VERTICAL)
Field = ttk.Treeview(Database_Window,columns=("Product ID", "Product Name", "Product Price", "Product Quantity",
                   "Mfg Company", "Phone.No" ,"Mfg Address"),
                   yscrollcommand=Vertical_Scrollbar.set,
                     xscrollcommand=Horizontal_Scrollbar.set)
Horizontal_Scrollbar.pack(side=BOTTOM, fill=X)
Vertical_Scrollbar.pack(side=RIGHT, fill=Y)
Horizontal_Scrollbar.config(command=Field.xview, )
Vertical_Scrollbar.config(command=Field.yview, )

#************************************************ Field Headings of  the Table ()******************************

Field.heading("Product ID", text="Product ID")
Field.heading("Product Name", text="Name")
Field.heading("Product Price", text="Price")
Field.heading("Product Quantity", text="Quantity")
Field.heading("Mfg Company", text="Mfg Company")
Field.heading("Phone.No", text="Phone.No")
Field.heading("Mfg Address", text="Mfg Address")
Field['show'] = "headings"

Field.column("Product Name", width=200)
Field.column("Mfg Address", width=300)
Field.pack(expand=True, fill=BOTH)

#************************************************Frame 7 (Button Frame 2)*************************

button_frame2 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")
button_frame2.place(x=492, y=575, width=830, height=54, )

# *********************************************** Buttons (For Frame 7)***************************

Show_button = Button(button_frame2, width=10, text="Show", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                    fg="#000000",
                    relief=SUNKEN,command = product_details).grid(row=0, column=0, padx=(180, 0), pady=7)

Update_button = Button(button_frame2, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                    bg="#ffffff", fg="#000000",
                    relief=SUNKEN,command =update_2_is_clicked).grid(row=0, column=1, padx=10, pady=7)

delete_button = Button(button_frame2, width=10, text="Delete", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                    bg="#ffffff", fg="#000000", relief=SUNKEN,command =delete_button_is_clicked).grid(row=0, column=2, padx=(0, 0), pady=7)

Clear_button = Button(button_frame2, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                   fg="#000000", relief=SUNKEN,command =clear_button_2_is_clicked).grid(row=0, column=3, padx=(9, 0), pady=7)

# ***************************************************Frame 8 (For Credit) ****************

Credit_Frame = Frame(root, bg="#ff0000", bd=0)
Credit_Frame.place(x=0, y=643, relwidth=1, relheight=0.08, )

Credit_Label = Label(Credit_Frame,
                     text="Developed By : Himangshu and team ,,,",
                     font=("times new roman", 20, "bold"),
                     fg="#ffffff",
                     bg="#ff0000"
                     )
Credit_Label.grid(row=0, column=0, padx=870, pady=10, sticky="w")

root.mainloop()