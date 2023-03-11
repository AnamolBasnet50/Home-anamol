from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox


def clear():
    emailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or UsernameEntry.get()=='' or PasswordEntry.get()=='' or ConfirmEntry.get()=='':
        messagebox.showerror('Error','All are required')
    elif PasswordEntry.get() != ConfirmEntry.get():
        messagebox.showerror('Error','password mis match') 
    elif check.get()==0:
        messagebox.showerror('error','please accept condations ')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('error','database connection issue try again')
            return
        
        try:
            query='create database Appdata'
            mycursor.execute(query)
            query='use Appdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
               mycursor.execute('use Appdata')
        
        query='select *from data where username=%s'
        mycursor.execute(query,(UsernameEntry.get()))
        
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('error','user Name already exist ')
        else:   
             query='insert into data(email,username,password)values(%s,%s,%s)'
             mycursor.execute(query,(emailEntry.get(),UsernameEntry.get(),PasswordEntry.get()))
             con.commit()
             con.close()
             messagebox.showinfo('sucess','registration is successful')
             clear()
             singup_window.destroy()
             import singin


def login_page():
    singup_window.destroy()
    import singin






singup_window=Tk()
singup_window.title('Smart Home singup  Page')
singup_window.resizable(False,False)
background = ImageTk.PhotoImage(file='naruto.png')

bgLabel = Label(singup_window,image=background)
bgLabel.grid()

frame = Frame(singup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE ACCOUNT',font=('Microsoft yahel UI Light',18,'bold')
,bg='white',fg='maroon')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel = Label(frame,text='Email',font=('Microsoft yahel UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft yahel UI Light',10,'bold'))
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

UsernameLabel = Label(frame,text='Username',font=('Microsoft yahel UI Light',10,'bold'),bg='white',fg='firebrick1')
UsernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

UsernameEntry=Entry(frame,width=30,font=('Microsoft yahel UI Light',10,'bold'))
UsernameEntry.grid(row=4,column=0,sticky='w',padx=25)

PasswordLabel = Label(frame,text='Password',font=('Microsoft yahel UI Light',10,'bold'),bg='white',fg='firebrick1')
PasswordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

PasswordEntry=Entry(frame,width=30,font=('Microsoft yahel UI Light',10,'bold'))
PasswordEntry.grid(row=6,column=0,sticky='w',padx=25)

ConfirmLabel = Label(frame,text='Confirm Password',font=('Microsoft yahel UI Light',10,'bold'),bg='white',fg='firebrick1')
ConfirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

ConfirmEntry=Entry(frame,width=30,font=('Microsoft yahel UI Light',10,'bold'))
ConfirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()

termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft yahel UI Light',9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',
cursor='hand2',variable=check)

termsandconditions.grid(row=9,column=0,pady=10,padx=15)

singupButton=Button(frame,text='Singup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
singupButton.grid(row=10,column=0,pady=10)

alreadyaccount = Label(frame, text="Don't Have", font=('Open Sans','9','bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginbutton = Button(frame,text='Login',font=('Open Sans','9','bold underline'),fg='blue',bg='white',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginbutton.place(x=100,y=378)

singup_window.mainloop()