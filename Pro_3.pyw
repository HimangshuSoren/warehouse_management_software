import tkinter
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk
import mysql.connector
import os

mydb = mysql.connector.connect(host = "localhost",
                               user ="root")
db1 = mydb.cursor()
db1.execute("use accounts")

def login_page():
    root.destroy()
    try:
        os.startfile("Pro_1.pyw")
    except Exception as e:
        print("s")

def enter_new_usr():
    cur = mydb.cursor()
    insert = "INSERT INTO users values (%s,%s,%s,%s,%s,%s)"
    values = (
              FName.get()+""+LName.get(),
              USRName.get(),
              E_mail.get(),
              Pass.get(),
              Security_Q.get(),
              Security_A.get(),
              )
    cur.execute(insert,values)
    mydb.commit()
    print("Done")
    messagebox.showinfo("Information",message ="Your account has been created now you will be redirected to the Login Page")
    login_page()

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
# root.resizable(0,0)
background = ImageTk.PhotoImage(file = r"image5.jpg")
bgmage_label = Label(root,image = background).place(x = 0,y = 0,relwidth =1,relheight = 1)

back = ImageTk.PhotoImage(file = r"image4.jpg")
frame_login1 = Label(root,image =back )
frame_login1.place(x = 112,y = 120 ,height = 470,width = 400)

frame_login = Frame(root,bg = "#ffffff" )
frame_login.place(x = 512,y = 120 ,height = 470,width = 700)

title_login= Label (frame_login,text = "Create an account",bg = "#ffffff",fg = "#00d30b",font =("Times New Roman",25,"bold"))
title_login.place(x = 35,y = 15)

FName = StringVar()
LName = StringVar()
USRName = StringVar()
E_mail = StringVar()
Pass = StringVar()
Security_Q= StringVar()
Security_A = StringVar()

FName_Label= Label (frame_login,text = "First Name",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
FName_Label.place(x = 35,y = 80)
FName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =FName ,bg = "#ffffff",cursor = "hand2")
FName_Entry.place(x = 35,y = 110,width =300 , height = 35)

LName_Label= Label (frame_login,text = "Last Name",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
LName_Label.place(x = 35,y = 160)
LName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =LName,bg = "#ffffff",cursor = "hand2")
LName_Entry.place(x = 35,y = 190,width =300 , height = 35)

USRName_Label= Label (frame_login,text = "Username",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
USRName_Label.place(x = 35,y = 240)
USRName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =USRName,bg = "#ffffff",cursor = "hand2")
USRName_Entry.place(x = 35,y = 270,width =300 , height = 35)

E_mail_Label= Label (frame_login,text = "E-mail",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
E_mail_Label.place(x = 35,y = 320)
E_mail_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =E_mail,bg = "#ffffff",cursor = "hand2")
E_mail_Entry.place(x = 35,y = 350,width =300 , height = 35)

Pass_Label= Label (frame_login,text = "Enter Password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Pass_Label.place(x = 355,y = 80)
Pass_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Pass,show = "*",bg = "#ffffff",cursor = "hand2")
Pass_Entry.place(x = 355,y = 110,width =300 , height = 35)

Pass_2_Label= Label (frame_login,text = "Re-enter Password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Pass_2_Label.place(x = 355,y = 160)
Pass_2_Entry= Entry (frame_login,font =("Times New Roman",15,),bg = "#ffffff",cursor = "hand2")
Pass_2_Entry.place(x = 355,y = 190,width =300 , height = 35)

Security_Q_Label= Label (frame_login,text = "Security Question",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Security_Q_Label.place(x = 355,y = 240)
Security_Q_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Security_Q,bg = "#ffffff",cursor = "hand2")
Security_Q_Entry.place(x = 355,y = 270,width =300 , height = 35)

Security_A_Label= Label (frame_login,text = "Security Answer",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Security_A_Label.place(x = 355,y = 320)
Security_A_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Security_A,bg = "#ffffff",cursor = "hand2")
Security_A_Entry.place(x = 355,y = 350,width =300 , height = 35)

Create_btn= Button(frame_login, text = "Create account",bd =0,fg = "#ffffff",bg = "#00d30b" ,font =("Times New Roman",20,"bold"),relief =SUNKEN,cursor = "hand2",command = enter_new_usr)
Create_btn.place(x =395,y =400,width = 230,height = 40 )

Sign_up_btn_2= Button(frame_login1, text = "Log In",bd =0,fg = "#000000",bg = "#ffffff" ,font =("Times New Roman",25,),relief =SUNKEN,cursor = "hand2",command =login_page)
Sign_up_btn_2.place(x =90,y =350,width = 200,height = 50,)

root.mainloop()