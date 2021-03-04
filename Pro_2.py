import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import datetime
import mysql.connector
import os

now = datetime.datetime.now()
tm = (now.strftime("%y-%m-%d "))
dt = (now.strftime("%H:%M:%S"))
print(dt)

clickedm = 0
clickede = 0

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               )

db = mydb.cursor()
db.execute("show databases")
lst = db.fetchall()
if ("school_project",) in lst:
    db.execute("use school_project")
    print("Database exists")
else:
    db.execute("""create database school_project""")
    db.execute("use school_project")
    print("Database created")

db.execute("show tables")
tbls = db.fetchall()
if ("inventory",) in tbls:

    print("Table is present")
    pass
else:
    db.execute("""create table inventory ( 
    Product_ID int(5) primary key,
    Product_Name varchar(20),
    Price varchar(10),
    Quantity int(40),
    Company varchar(20),
    Contact varchar(10),
    Mfg_Date Date,
    Expiry_Date Date,
    address varchar(30))""")
    print("Table is created")


db.execute("show tables")
tbls = db.fetchall()
if ("sale_history",) in tbls:

    print("Table is present")
    pass
else:
    db.execute("""create table sale_history (
    Customer_Name varchar(50),
    Product_Name varchar(20),
    Product_ID int(5),
    Quantity varchar(10),
    Price varchar(10),
    Contact varchar(10),
    Date Date,
    Time varchar(30))""")
    print("Table is created")


def clear_button_2_is_clicked():
    Field.delete(*Field.get_children())

def search_button_is_clicked():
    c = str(Entry1.get())
    cur = mydb.cursor()
    select = ("select * from inventory where " + str(Search.get()) + " = '" + c + "'")
    cur.execute(select)
    rows = cur.fetchall()
    if len(rows) != 0:
        Field.delete(*Field.get_children())
        for row in rows:
            if row[7] == None :
                print(row[7])
            Field.insert('', END, values=row)
            mydb.commit()

    else:
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()


def update_2_is_clicked():
    global clickedm
    global clickede
    clickedm += 1
    clickede += 1
    MANU_txt.config(state=NORMAL)
    EXPIRY_txt.config(state=NORMAL)
    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row = content['values']
    Product_ID.set(row[0])
    Product_Name.set(row[1])
    Price.set(row[2][:-3])
    Quantity.set(row[3])
    Company.set(row[4])
    Contact.set(row[5])
    Manufacture.set(row[6])
    Expiry.set(row[7])
    ADDRESS_txt.delete("1.0", END)
    ADDRESS_txt.insert(END, row[8])


def add_btn():
    if Product_ID.get() == 0 or Product_Name.get() == "":
        messagebox.showerror("Error", message="Please enter correct details")

    else:

        Invalid_Price = Price.get()
        Invalid_No = Contact.get()
        lprice = len(Invalid_Price)
        lnumb = len(Invalid_No)
        a = 0
        b = 0
        for i in range(0, lprice):
            c = Invalid_Price[i]
            if c.isalpha() == True:
                a += 1

        for i in range(0, lnumb):
            c = Invalid_No[i]
            if c.isalpha() == True:
                b += 1

        if a > 0 or Invalid_Price.strip() == "":
            messagebox.showerror("Error", message="Please enter a valid price !", parent=root)

        elif b > 0 or lnumb != 10:
            messagebox.showerror("Error", message="Please enter a valid Phone.No !", parent=root)
        else:

            cur = mydb.cursor()
            cur.execute("select Product_ID from inventory")
            f = cur.fetchall()
            c = str(f)
            sp = c.split()
            list = []
            for i in range(0, len(sp)):
                st = str(sp[i])
                rep1 = st.replace("(", "")
                rep2 = rep1.replace(",", "")
                rep3 = rep2.replace(")", "")
                rep4 = rep3.replace("[", "")
                rep5 = rep4.replace("]", "")
                list.append(rep5)

            if Product_ID.get() in list:
                messagebox.showerror("Error", message="Record already exists with same ID")
            else:
                ADDRESS = ADDRESS_txt.get('1.0', END)
                cur = mydb.cursor()
                insert = "INSERT INTO Inventory values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (Product_ID.get(),
                          Product_Name.get(),
                          Price.get() + " Rs",
                          Quantity.get(),
                          Company.get(),
                          Contact.get(),
                          Manufacture.get(),
                          Expiry.get(),
                          ADDRESS.rstrip()
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


def search_all_bth():
    cur = mydb.cursor()
    select = "select * from inventory "
    cur.execute(select)
    rows = cur.fetchall()
    Field.delete(*Field.get_children())
    for row in rows:
        Field.insert('', END, values=row)
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

def selling():
    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row = content['values']
    selling_data = f'''
    Product ID   : {row[0]}
    Product Name : {row[1]}
    Price        : {row[2]}
    Mfg Company  : {row[4]}
    Mfg Date     : {row[6]}
    Expiry Date  : {row[7]}
    Mfg Address  : {row[8]}
    '''
    def add_his():
        a = 0
        b = 0
        c = 0
        inv1 = PHONE_TXT.get()
        inv2 = QTY_TXT.get()
        var = str(QTY_TXT.get())
        numl = len(inv1)
        qtl = len(inv2)
        print(var)
        for i in range (0,numl) :
            if inv1[i].isalpha() == True :
                a += 1

        for i in range (0,qtl) :
            if var[i].isalpha() == True :
                b += 1

        for i in range (0,len(CUST_NAME_TXT.get().replace(" ",""))) :
            if CUST_NAME_TXT.get().replace(" ","")[i].isalpha() == False :
                c += 1

        if b > 0 :
            messagebox.showerror("Error", message="Please Enter a valid quantity", parent=rot)

        elif   int(inv2) > int(str(row[3])) or int(inv2) == 0 :
            messagebox.showinfo("sorry", message="Sorry we do not have enough stock", parent=rot)
            rot.destroy()

        elif numl != 10 or a > 0 :
            messagebox.showerror("Error",message = "Please Enter a valid number",parent = rot)
        elif CUST_NAME_TXT.get().replace(" ","") == ""  or c > 0 :

            messagebox.showerror("Error", message="Please Enter the correct name", parent=rot)
        else :
            cur = mydb.cursor()
            insert = "INSERT INTO sale_history values (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (CUST_NAME_TXT.get(),
                      row[1],
                      row[2],
                      QTY_TXT.get(),
                      AMT_TXT.get()+" Rs",
                      PHONE_TXT.get(),
                      tm,
                      dt
                      )
            cur.execute(insert, values)
            cur.execute(f"update inventory set Quantity = Quantity - {QTY_TXT.get()} where Product_ID = {row[0]}")
            mydb.commit()
            messagebox.showinfo("Done",message = "Selling Successful",parent = rot)
            rot.destroy()


    rot = tkinter.Tk()
    rot.title("   sell ")
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 500
    h = 595
    x = int(ws / 2 - w / 2 - 20)
    y = int(hs / 2 - h / 2 - 30)
    data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
    rot.geometry(data)
    rot.configure(bg="#ffffff")
    rot.resizable(0, 0)

    title_frame = LabelFrame(rot)
    title_frame.pack(fill="x")

    title = Label(title_frame,
                  text="Selling Product",
                  font=("Comic Sans MS", 25, "bold"),
                  bg="#00e6a1",
                  fg="#ffffff",
                  anchor="center",
                  bd=4)
    title.pack(expand=True, fil="x")

    Main_Frame = Frame(rot, bd=1, relief=RIDGE, bg="#ffffff")
    Main_Frame.place(x=2, y=60, width=500, height=539)

    Searching_Frame = Frame(rot, bd=1, relief=RIDGE)
    Searching_Frame.place(x=2, y=60, width=500, height=54)

    Search_By_Label = Label(Searching_Frame, text="Selling Information", fg="#676767",
                            font=("Comic Sans MS", 17, "bold"))
    Search_By_Label.grid(row=0, column=0, pady=10, padx=20, sticky="n")

    sell_info_txt = Text(Main_Frame, width=27, height=2, fg="#000000", bd=1 / 2, relief=GROOVE, )
    sell_info_txt.insert(END,selling_data)
    sell_info_txt.config(state = DISABLED)
    sell_info_txt.place(x=2, y=55, width=490, height=170)

    button_frame2 = Frame(Main_Frame, bd=2, relief=RIDGE, bg="#fff000")  # bg="#00a6ff"
    button_frame2.place(x=2, y=230, width=490, height=235, )

    QTY_1 = StringVar()
    Customer_Name = StringVar()
    Amount_Payable = StringVar()
    Phone = StringVar()

    QTY_LBL = Label(button_frame2, text="Quantity", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
    QTY_LBL.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="w")

    QTY_TXT = Entry(button_frame2, textvariable=QTY_1, width=18, font=("Comic Sans MS", 15), fg="#000000", bd=1,
                    relief=GROOVE, )
    QTY_TXT.grid(row=1, column=2, sticky="w", pady=(20, 0))

    AMT_LBL = Label(button_frame2, text="Payable Amount", bg="#fff000", fg="#ffffff",
                    font=("Comic Sans MS", 19, "bold"))
    AMT_LBL.grid(row=2, column=0, pady=10, padx=20, sticky="w")

    AMT_TXT = Entry(button_frame2, textvariable=Amount_Payable, width=18, fg="#000000", font=("Comic Sans MS", 15),
                    bd=1,
                    relief=GROOVE, )
    # p = int(row[2][:-4])
    # print(p)
    # AMT_TXT.insert(int(QTY_TXT.get()) * int(str(row[2][:-3])))
    AMT_TXT.grid(row=2, column=2, sticky="w")

    CUST_NAMELBL = Label(button_frame2, text="Customer Name", bg="#fff000", fg="#ffffff",
                         font=("Comic Sans MS", 19, "bold"))
    CUST_NAMELBL.grid(row=3, column=0, pady=5, padx=20, sticky="w")

    CUST_NAME_TXT = Entry(button_frame2, textvariable=Customer_Name, width=18, fg="#000000", font=("Comic Sans MS", 15),
                          bd=1,
                          relief=GROOVE, )
    CUST_NAME_TXT.grid(row=3, column=2, sticky="w")

    PHONE_LBL = Label(button_frame2, text="Phone.no", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
    PHONE_LBL.grid(row=4, column=0, pady=5, padx=20, sticky="w")

    PHONE_TXT = Entry(button_frame2, textvariable=Phone, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                      relief=GROOVE, )
    PHONE_TXT.grid(row=4, column=2, sticky="w")

    AD_his_btn = Button(Main_Frame, text="Proceed", bd=0, fg="#ffffff", bg="#00d30b",
                        font=("Times New Roman", 20, "bold"), relief=SUNKEN, cursor="hand2",command = add_his)

    AD_his_btn.place(x=123, y=479, width=230, height=40)


def clear_button_is_clicked():
    ID_txt.delete(0, END)
    NAME_txt.delete(0, END)
    PRICE_txt.delete(0, END)
    CONTACT_txt.delete(0, END)
    COMPANY_txt.delete(0, END)
    QUANTITY_txt.delete(0, END)
    MANU_txt.delete(0, END)
    EXPIRY_txt.delete(0, END)
    ADDRESS_txt.delete("1.0", END)


def update_button_is_clicked():
    Invalid_Price = Price.get()
    Invalid_No = Contact.get()
    lprice = len(Invalid_Price)
    lnumb = len(Invalid_No)
    a = 0
    b = 0
    for i in range(0, lprice):
        c = Invalid_Price[i]
        if c.isalpha() == True:
            a += 1

    for i in range(0, lnumb):
        c = Invalid_No[i]
        if c.isalpha() == True:
            b += 1

    if a > 0 or Invalid_Price.strip() == "":
        messagebox.showerror("Error", message="Please enter a valid price !", parent=root)

    elif b > 0 or lnumb != 10:
        messagebox.showerror("Error", message="Please enter a valid Phone.No !", parent=root)

    else:
        ADDRESS = ADDRESS_txt.get('1.0', END)
        cur = mydb.cursor()
        insert = '''UPDATE Inventory set
        Product_Name=%s,
        Price=%s,
        Quantity = %s,
        Company=%s,
        Contact=%s,
        Mfg_Date=%s,
        Expiry_Date=%s,
        address=%s 
        where Product_ID=%s '''
        values = (
            Product_Name.get(),
            Price.get() + " Rs",
            Quantity.get(),
            Company.get(),
            Contact.get(),
            Manufacture.get(),
            Expiry.get(),
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


def logout_button_is_clicked():
    root.destroy()
    try:
        os.startfile("Pro_1.py")
    except Exception as e:
        print("s")


def Expiry_click(event):
    global clickede
    if clickede <= 0:
        EXPIRY_txt.config(state=NORMAL)
        EXPIRY_txt.delete(0, END)
        clickede += 1
def sell():
    try:
        os.startfile("Pro_5.py")

    except Exception as e:
        print("s")

def Manu_click(event):
    global clickedm
    if clickedm <= 0:
        MANU_txt.config(state=NORMAL)
        MANU_txt.delete(0, END)
        clickedm += 1
def history_button_clicked():
    try:
        os.startfile("Pro_5.py")
    except Exception as e:
        print("s")

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
    print()
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

    label8 = Label(pop, text=(f":    {row[0]}"), bg="#ffffff", fg="#676767", anchor=W,
                   font=("Times New Roman", 19, "bold"))
    label8.grid(row=0, column=1, sticky="w")

    label9 = Label(pop, text=(f":    {row[1]}"), bg="#ffffff", fg="#676767", anchor=W,
                   font=("Times New Roman", 19, "bold"))
    label9.grid(row=1, column=1, sticky="w")

    label10 = Label(pop, text=(f":    {row[2]}"), bg="#ffffff", fg="#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label10.grid(row=2, column=1, sticky="w")

    label11 = Label(pop, text=(f":    {row[3]}"), bg="#ffffff", fg="#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label11.grid(row=3, column=1, sticky="w")

    label12 = Label(pop, text=(f":    {row[4]}"), bg="#ffffff", fg="#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label12.grid(row=4, column=1, sticky="w")

    label13 = Label(pop, text=(f":    {row[5]}"), bg="#ffffff", fg="#676767", anchor=W,
                    font=("Times New Roman", 19, "bold"))
    label13.grid(row=5, column=1, sticky="w")

    label14 = Label(pop, text=(f":    {row[6]}"), bg="#ffffff", fg="#676767", anchor=W,
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
root.title("Warehouse Inventory Sales Purchase Management System  ")
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

# *************************************Frame 1  (Title)**************

title_frame = LabelFrame(root)
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
Manage_Frame_canvas.place(x=13, y=95, width=463, height=545)

Manage_Frame = Frame(root, bd=1, bg="#fff000", relief=GROOVE)
Manage_Frame.place(x=13, y=95, width=462, height=470)

Entrycanvas = Canvas(Manage_Frame, bg="#fff000")

Entrycanvas.place(x=0, y=0, width=858, height=470)

yscrollbar = ttk.Scrollbar(Manage_Frame, orient="vertical", command=Entrycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

Entrycanvas.configure(yscrollcommand=yscrollbar.set)

Entrycanvas.bind('<Configure>', lambda e: Entrycanvas.configure(scrollregion=Entrycanvas.bbox('all')))

frame1 = Frame(Entrycanvas, bg="#fff000")
Entrycanvas.create_window((0, 0), window=frame1, anchor="nw")

Manage_Frame3 = LabelFrame(frame1, text=" Put the Details", font=("Comic Sans MS", 22, "bold", "italic"),
                           fg="#ffffff", bd=0, bg="#fff000", relief=SUNKEN, )
Manage_Frame3.place(y=0, x=0, width=457, height=545)

# ***************************************** Variables For Entering Data **********

Product_ID = StringVar()
Product_Name = StringVar()
Price = StringVar()
Quantity = StringVar()
Contact = StringVar()
Company = StringVar()
Manufacture = StringVar()
Expiry = StringVar()

# __________________________Entries_________________________#


ID_lbl = Label(frame1, text="Product ID", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
ID_lbl.grid(row=1, column=0, pady=(50, 0), padx=20, sticky="w")

ID_txt = Entry(frame1, textvariable=Product_ID, width=18, font=("Comic Sans MS", 15), fg="#000000", bd=1,
               relief=GROOVE, )
ID_txt.grid(row=1, column=2, sticky="w", pady=(50, 0))

NAME_lbl = Label(frame1, text="Product Name", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
NAME_lbl.grid(row=2, column=0, pady=10, padx=20, sticky="w")

NAME_txt = Entry(frame1, textvariable=Product_Name, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                 relief=GROOVE, )
NAME_txt.grid(row=2, column=2, sticky="w")

PRICE_lbl = Label(frame1, text="Product Price", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
PRICE_lbl.grid(row=3, column=0, pady=10, padx=20, sticky="w")

PRICE_txt = Entry(frame1, textvariable=Price, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )
PRICE_txt.grid(row=3, column=2, sticky="w")

QUANTITY_lbl = Label(frame1, text="Quantity", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
QUANTITY_lbl.grid(row=4, column=0, pady=10, padx=20, sticky="w")

QUANTITY_txt = Entry(frame1, textvariable=Quantity, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                     relief=GROOVE, )
QUANTITY_txt.grid(row=4, column=2, sticky="w")

COMPANY_lbl = Label(frame1, text="Mfg Company", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
COMPANY_lbl.grid(row=5, column=0, pady=10, padx=20, sticky="w")
COMPANY_txt = Entry(frame1, textvariable=Company, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                    relief=GROOVE, )
COMPANY_txt.grid(row=5, column=2, sticky="w")

CONTACT_lbl = Label(frame1, text="Phone.No", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
CONTACT_lbl.grid(row=6, column=0, pady=10, padx=20, sticky="w")

CONTACT_txt = Entry(frame1, textvariable=Contact, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                    relief=GROOVE, )
CONTACT_txt.grid(row=6, column=2, sticky="w")

MANU_lbl = Label(frame1, text="Mfg Date", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
MANU_lbl.grid(row=7, column=0, pady=10, padx=20, sticky="w")
MANU_txt = Entry(frame1, textvariable=Manufacture, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                 relief=GROOVE, )

MANU_txt.insert(0, "YYYY-MM-DD")
MANU_txt.config(state=DISABLED, bg="#ffffff")
MANU_txt.bind("<Button-1>", Manu_click)
MANU_txt.grid(row=8, column=2, stick="w")
MANU_txt.grid(row=7, column=2, stick="w")

EXPIRY_lbl = Label(frame1, text="Expiry Date", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
EXPIRY_lbl.grid(row=8, column=0, pady=10, padx=20, sticky="w")

EXPIRY_txt = Entry(frame1, textvariable=Expiry, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                   relief=GROOVE, )
EXPIRY_txt.insert(0, "YYYY-MM-DD")
EXPIRY_txt.config(state=DISABLED, bg="#ffffff")
EXPIRY_txt.bind("<Button-1>", Expiry_click)
EXPIRY_txt.grid(row=8, column=2, sticky="w")

ADDRESS_lbl = Label(frame1, text="Mfg Address", bg="#fff000", fg="#ffffff", font=("Comic Sans MS", 19, "bold"))
ADDRESS_lbl.grid(row=9, column=0, pady=10, padx=20, sticky="w")

ADDRESS_txt = Text(frame1, width=27, height=2, fg="#000000", bd=1 / 2, relief=GROOVE, )
ADDRESS_txt.grid(row=9, column=2, sticky="w")

# ***************************************** Frame 3 (Button Frame 1)*****

button_frame1 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")
button_frame1.place(x=13, y=575, width=462, height=54)

# ******************************************* Buttons (For Frame 3 ) _______________

add_btn = Button(button_frame1, width=10, text="Add", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                 fg="#000000", relief=SUNKEN, command=add_btn).grid(row=0, column=0, padx=4, pady=7)

update_btn = Button(button_frame1, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                    bg="#ffffff", fg="#000000", relief=SUNKEN, command=update_button_is_clicked).grid(row=0, column=1,
                                                                                                      padx=1, pady=7)

clear_btn = Button(button_frame1, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                   bg="#ffffff", fg="#000000", relief=SUNKEN, command=clear_button_is_clicked).grid(row=0, column=2,
                                                                                                    padx=2, pady=7)

Logout_btn = Button(button_frame1, width=10, text="Logout", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                    fg="#000000", relief=SUNKEN, command=logout_button_is_clicked).grid(row=0, column=3, padx=3, pady=7)

# *********************************************Frame 4 ( For Management ) ************************

Main_Frame = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Main_Frame.place(x=480, y=95, width=856, height=544)

# **********************************************Frame 5 (For Searching)**************************

Searching_Frame = Frame(root, bd=1, relief=RIDGE, )
Searching_Frame.place(x=480, y=95, width=856, height=54)

Search_By_Label = Label(Searching_Frame, text="Search By", fg="#676767", font=("Comic Sans MS", 17, "bold"))
Search_By_Label.grid(row=0, column=0, pady=10, padx=20, sticky="w")

Search = StringVar()
Combo_Search = ttk.Combobox(Searching_Frame, textvariable=Search, font=("Comic Sans MS", 14), width=11,
                            state="readonly")

Combo_Search["values"] = (
"", "Product_ID", "Product_Name", "Price", "Company", "Contact", "Quantity", "Mfg_Date", "Expiry_Date", "Address")
Combo_Search.grid(row=0, column=1)

Entry1 = StringVar()
Search_Bar = Entry(Searching_Frame, textvariable=Entry1, width=16, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                   relief=GROOVE, )
Search_Bar.grid(row=0, column=2, sticky="w", padx=27)

Search_Button = Button(Searching_Frame, width=10, text="Search", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff",
                       fg="#000000", relief=SUNKEN, command=search_button_is_clicked).grid(row=0, column=3,
                                                                                           padx=(10, 0), pady=7,
                                                                                           sticky="e")

Search_All_Button = Button(Searching_Frame, width=10, text="Search All", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                           bg="#ffffff",
                           fg="#000000", relief=SUNKEN, command=search_all_bth).grid(row=0, column=4, padx=20, pady=7,
                                                                                     sticky="e")

# *******************************************************Frame 6 (Database Window)*********************

Database_Window = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Database_Window.place(x=480, y=148, width=856, height=415)

# ********************************************************* Scrrollbars () *****************************

Horizontal_Scrollbar = Scrollbar(Database_Window, orient=HORIZONTAL)
Vertical_Scrollbar = Scrollbar(Database_Window, orient=VERTICAL)
Field = ttk.Treeview(Database_Window, columns=("Product ID", "Product Name", "Product Price", "Product Quantity",
                                               "Mfg Company", "Phone.No", "Mfg Date", "Expiry Date", "Mfg Address"),
                     yscrollcommand=Vertical_Scrollbar.set,
                     xscrollcommand=Horizontal_Scrollbar.set)
Horizontal_Scrollbar.pack(side=BOTTOM, fill=X)
Vertical_Scrollbar.pack(side=RIGHT, fill=Y)
Horizontal_Scrollbar.config(command=Field.xview, )
Vertical_Scrollbar.config(command=Field.yview, )

# ************************************************ Field Headings in  the Table ()******************************

Field.heading("Product ID", text="Product ID")
Field.heading("Product Name", text="Name")
Field.heading("Product Price", text="Price (INR)")
Field.heading("Product Quantity", text="Quantity")
Field.heading("Mfg Company", text="Mfg Company")
Field.heading("Phone.No", text="Phone.No")
Field.heading("Mfg Date", text="Mfg Date")
Field.heading("Expiry Date", text="Expiry Date")

Field.heading("Mfg Address", text="Mfg Address")
Field['show'] = "headings"


Field.column("Product ID", width=150)
Field.column("Product Name", width=200)
Field.column("Mfg Address", width=300)
Field.pack(expand=True, fill=BOTH)

# ************************************************Frame 7 (Button Frame 2)*************************

button_frame2 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")
button_frame2.place(x=492, y=575, width=830, height=54, )

# *********************************************** Buttons (For Frame 7)***************************

Sell_button = Button(button_frame2, width=10, text="Sell", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                     fg="#000000",
                     relief=SUNKEN, command=selling).grid(row=0, column=0, padx=(60, 0), pady=7)

Show_button = Button(button_frame2, width=10, text="Show", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff", fg="#000000",
                       relief=SUNKEN, command=product_details).grid(row=0, column=1, padx=7, pady=7)

Update_button = Button(button_frame2, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff", fg="#000000",
                       relief=SUNKEN, command=update_2_is_clicked).grid(row=0, column=2, padx=(7,7), pady=7)

delete_button = Button(button_frame2, width=10, text="Delete", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff", fg="#000000", relief=SUNKEN, command=delete_button_is_clicked).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=(0, 0),
                                                                                                         pady=7)

Clear_button = Button(button_frame2, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                      fg="#000000", relief=SUNKEN, command=clear_button_2_is_clicked).grid(row=0, column=4, padx=(9, 0),
                                                                                           pady=7)
History_Button = Button(button_frame2, width=10, text="History", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                      fg="#000000", relief=SUNKEN, command=history_button_clicked).grid(row=0, column=5, padx=(9, 0),
                                                                                           pady=7)

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
