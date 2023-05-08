from calendar import month
from cgitb import text
from email.errors import MessageError
from msilib.schema import Font
from multiprocessing import parent_process
from os import stat
# from sys import last_traceback 
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tokenize import String
from turtle import heading
from click import password_option
# from numpy import var
from platformdirs import user_config_path
import pymysql
from requests import head

def clear():
    userentry.delete(0,END)
    passentry.delete(0,END)

def close():
    win.destroy()

def login():
    if user_name.get()=="" or password.get=="":
        messagebox.showerror("Error","Enter user name and password",parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="",database="doctor")
            cur=con.cursor()

            cur.execute("select * from user_information where username =%s and password=%s",(user_name.get(),password.get()))
            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid user name and password",parent=win)
            else:
                messagebox.showinfo("Success","Successfylly Login",parent=win)

                close()
                deshboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Error Dui to:{str(es)}",parent=win)

#--------------------------------------------Desh board panel---------------------------------------------------
def deshboard():
    def book():
        if doctor_var.get()=="" or day.get()=="" or month.get=="" or year.get=="":
            messagebox.showerror("Error","All Fields are required",parent=des)
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="doctor")

            cur=con.cursor()
            cur.execute("update user_information set doctor='" + doctor_var.get()+ "',day='" +day.get() + 
            "',month='" + month.get()+ "' ,year = '" + year.get() + "' where username='" +user_name.get() +"'")
            messagebox.showinfo("Success","Appointment fixed",parent=des)
            con.commit()
            con.close()
        
    des=Tk()
    des.title("Admin panel Doctor App")
    des.maxsize(width=800,height=500)
    des.minsize(width=800 ,height=500)

    #heading label

    heading =Label(des,text=f"User Name:{user_name.get()}",font='verdana 20 bold ',bg='red')
    heading.place(x=220,y=50)
    f=Frame(des,height=1,width=800,bg="green")
    f.place(x=0,y=95)
    con = pymysql.connect(host="localhost",user="root",password="",database="doctor")
    cur=con.cursor()
    cur.execute("select * from user_information where username ='"+user_name.get()+"'")
    row=cur.fetchall()

    a=Frame(des,height=1,width=400,bg="green")
    a.place(x=0,y=195)

    b=Frame(des,height=100,width=1,bg="green")
    b.place(x=400,y=97)

    for data in row:
        first_name=Label(des,text=f"first_name:{data[0]}",font="Verdana 10 bold")
        first_name.place(x=20,y=100)

        last_name=Label(des,text=f"Last name:{data[1]}" , font="Verdana 10 bold")
        last_name.place(x=20,y=130)

        age=Label(des ,text=f"Age :{data[2]}",font="verdana 10 bold")
        age.place(x=20,y=160)

        gender=Label(des,text=f"ID:{data[6]}",font="Verdana 10 bold")
        gender.place(x=250,y=100)

        city=Label(des,text=f"City :{data[4]}",font="Verdana 10 bold")
        city.place(x=250,y=130) 

        add=Label(des,text=f"Address:{data[5]}",font="Verdana 10 bold")
        add.place(x=250,y=160)

#book doctor appointment
    heading=Label(des,text="Book appointment" ,font="Verdana 10 bold")
    heading.place(x=470,y=100)

#book doctorLabel
    doctor=Label(des,text="doctor:",font=" verdana 10 bold")
    doctor.place(x=480,y=145)

    Day=Label(des,text="Day:",font="Verdana 10 bold") 
    Day.place(x=480,y=165)

    Month=Label(des,text="Month:",font="Verdana 10 bold")
    Month.place(x=480,y=185)

    Year=Label(des,text="Year:" ,font="Verdana 10 bold")
    Year.place(x=480,y=205)


# Book doctor entry box

    doctor_var=tk.StringVar()
    day=StringVar() 
    year=StringVar()
    month=tk.StringVar()

    doctor_box=ttk.Combobox(des,width=30,textvariable=doctor_var,state='readonly')
    doctor_box['values']=('Andy','Charlie','Shetal','Danosh','Sunil')
    doctor_box.current(0)
    doctor_box.place(x=550,y=145)  

    Day=Entry(des,width=33,textvariable=day)
    Day.place(x=550,y=168)    

    Month_Box=ttk.Combobox(des,width=30,textvariable=month,state='readonly')
    Month_Box['values']=('January','February','March','April','May','Jun','July','Agust','Sepember','October','November','December')

    Month_Box.current(0)
    Month_Box.place(x=550,y=188)

    Year=Entry(des,width=33,textvariable=year)
    Year.place(x=550,y=208)

    #button
    btn=Button(des,text="Seacrch",font='Verdana 10 bold',width=20,command=book)
    btn.place(x=553,y=230)

    con=pymysql.connect(host="localhost",user="root",password="",database="doctor")
    cur=con.cursor()

    cur.execute("select * from user_information where username='"+user_name.get()+"'")
    rows=cur.fetchall()

    #book appointment details
    heading=Label(des,text=f"{user_name.get()} Appointment",font="Verdana 10 bold")
    heading.place(x=20,y=250)

    for book in rows:
        d1=Label(des,text=f"doctor:{book[8]}",font="Verdana 10 bold")
        d1.place(x=20,y=280)

        d2=Label(des,text=f"day:{book[9]}",font="Verdana 10 bold")
        d2.place(x=20,y=300)

        d3=Label(des,text=f"year:{book[10]}",font="Verdana 10 bold")
        d3.place(x=20,y=320)
    
        d4=Label(des,text=f"month:{book[11]}",font="Verdana 10 bold")
        d4.place(x=20,y=340)


#------------------Sign up window----------------
def signup():
    def action():
        if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name=="" or password.get()=="" or very_pass.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error","Password and confirm password shoud be same",parent=winsignup)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="doctor")
                cur=con.cursor()
                cur.execute("select * from user_information where username =%s",user_name.get())
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","User name already exits",parent=winsignup)
                else:
                    cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        first_name.get(),
                        last_name.get(),
                        age.get(),
                        var.get(),
                        city.get(),
                        add.get(),
                        user_name.get(),
                        password.get()
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Ragistration Successfull",parent=winsignup)
                clear()
                switch()
            except Exception as es:
                messagebox.showerror("Error",f"Error Dui to:{str(es)}",parent=winsignup)

    #close signup function
    def switch():
        winsignup.destroy()

    #clear data function
    def clear():
        first_name.delete(0,END)
        last_name.delete(0,END)
        age.delete(0,END)
        var.set("Male")
        city.delete(0,END)
        add.delete(0,END)
        user_name.delete(0,END)
        password.delete(0,END)
        very_pass.delete(0,END)

    #strt signup window
    winsignup=Tk()
    winsignup.title("Doctor appintment app")
    winsignup.maxsize(width=500,height=600)
    winsignup.minsize(width=500,height=600)

    #heading label
    heading=Label(winsignup,text="Signup",font="Verdana 20 bold")
    heading.place(x=80,y=60)

    #from data label
    first_name=Label(winsignup,text="First Name",font="Verdana 10 bold")
    first_name.place(x=80,y=130)

    last_name=Label(winsignup,text="Last Name",font="Verdana 10 bold")
    last_name.place(x=80,y=160)

    age=Label(winsignup,text="Age",font="Verdana 10 bold")
    age.place(x=80,y=190)

    Gender=Label(winsignup,text="Gender",font="Verdana 10 bold")
    Gender.place(x=80,y=220)

    city=Label(winsignup,text="City",font="Verdana 10 bold")
    city.place(x=80,y=260)

    add=Label(winsignup,text="Address",font="Verdana 10 bold")
    add.place(x=80,y=290)

    user_name=Label(winsignup,text="User Name",font="Verdana 10 bold")
    user_name.place(x=80,y=320)

    password=Label(winsignup,text="Password",font="Verdana 10 bold")
    password.place(x=80,y=350)

    very_pass=Label(winsignup,text="Verify password",font="Verdana 10 bold")
    very_pass.place(x=80,y=380)

    #Entry box
    first_name=StringVar()
    last_name=StringVar()
    age=IntVar(winsignup,value='0')
    var=StringVar()
    city=StringVar()
    add=StringVar()
    user_name=StringVar()
    password=StringVar()
    very_pass=StringVar()


    first_name=Entry(winsignup,width=40,textvariable=first_name)
    first_name.place(x=200,y=135)

    last_name=Entry(winsignup,width=40,textvariable=last_name)
    last_name.place(x=200,y=163)

    age=Entry(winsignup,width=40,textvariable=age)
    age.place(x=200,y=193)

    Radio_button_male=ttk.Radiobutton(winsignup,text='Male',value="Male",variable=var).place(x=200,y=220)
    Radio_button_female=ttk.Radiobutton(winsignup,text='Female',value="female",variable=var).place(x=200,y=238)

    city=Entry(winsignup,width=40,textvariable=city)
    city.place(x=200,y=263)

    add=Entry(winsignup,width=40,textvariable=add)
    add.place(x=200,y=293)

    user_name=Entry(winsignup,width=40,textvariable=user_name)
    user_name.place(x=200,y=323)

    password=Entry(winsignup,width=40,textvariable=password)
    password.place(x=200,y=353)

    very_pass=Entry(winsignup,width=40,textvariable=very_pass)
    very_pass.place(x=200,y=383)

    #button login and clear

    btn_signup=Button(winsignup,text="Signup",font="Verdana 10 bold",command=action)
    btn_signup.place(x=200,y=413)

    btn_login=Button(winsignup,text="Clear",font="Verdana 10 bold",command=clear)
    btn_login.place(x=280,y=413)

    sign_up_btn=Button(winsignup,text="Switch to Login",font="Verdana 10 bold",command=switch)
    sign_up_btn.place(x=350,y=20)

    # win.signup.mainloop()

    #------------Login Window-------------

win=Tk()

#app title
win.title( "Doctor Appointment App")

#window size----------
win.maxsize(width=500,height=500)
win.minsize(width=500,height=500)

#heading lavel
heading=Label(win,text="Login",font="Veradana 25 bold")
heading.place(x=80,y=150)

username=Label(win,text="User Name:",font="Verdana 10 bold")
username.place(x=80,y=220)

userpass=Label(win,text="User Password:",font="Verdana 10 bold")
userpass.place(x=80,y=260)

#Entry box

user_name=StringVar()
password=StringVar()

userentry=Entry(win,width=40,textvariable=user_name)
userentry.focus()
userentry.place(x=200,y=223)

passentry=Entry(win,width=40,show="*",textvariable=password)
passentry.place(x=200,y=260)

#button and login clear
btn_login=Button(win,text="LOGIN",font="Verdana 10 bold",command=login)
btn_login.place(x=200,y=293)

btn_login=Button(win,text="CLEAR",font="Verdana 10 bold",command=clear)
btn_login.place(x=300,y=293)

#signup button
sign_up_btn=Button(win,text="Switch to Sihn Up",command=signup)
sign_up_btn.place(x=350,y=20)

win.mainloop()