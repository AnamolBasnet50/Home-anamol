from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql


#funcation part

def forget_pass():
    def change_password():
        if user_enter.get()=='' or newpass_enter.get()=='' or conpass_enter.get()=='':
           messagebox.showerror('error','all field are empty',parent=window)
        elif newpass_enter.get() != conpass_enter.get():
            messagebox.showerror('error','passwor dont match ',parent=window)

        else:
              con =pymysql.connect(host='localhost',user='root',password='1234',database='appdata')
              mycurser =con.cursor()
              query = 'select * from data where username =%s'
              mycurser.execute(query,(user_enter.get()))
              row = mycurser.fetchone()
              if row == None:
                messagebox.showerror('error','incorrect name',parent = window)
              else:
                query='update data set password=%s where username=%s'
                mycurser.execute(query,(newpass_enter.get(),user_enter.get()))
                con.commit()
                con.close()
                messagebox.showinfo('sucess','pasword changed',parent = window)
                window.destroy()




    window = Toplevel() 
    window.title('change pasword')

    bgpic = ImageTk.PhotoImage(file='naruto.png')
    bglable = Label(window,image=bgpic)
    bglable.grid()

    
    heading_label=Label(window,text='RESET PASSWORD',font=('Microsoft yahel UI Light',23,'bold')
    ,bg='white',fg='maroon')
    heading_label.place(x=350, y=30)

    USERLABEL = Label(window,text='username',font=('arial','18','bold'),bg='white',fg='maroon')
    USERLABEL.place(x=350,y=150)

    user_enter = Entry(window,width=25,fg='magenta2',font=('aial',14,'bold'),bd=0)
    user_enter.place(x =350, y=200)

    Frame(window,width=280,height=2,bg='orchid1').place(x=350,y=225)

    PASSWORDLABEL = Label(window,text=' NEW PASSWORD',font=('arial','18','bold'),bg='white',fg='maroon')
    PASSWORDLABEL.place(x=350,y=250)

    newpass_enter = Entry(window,width=25,fg='magenta2',font=('aial',14,'bold'),bd=0)
    newpass_enter.place(x =350, y=300)

    Frame(window,width=280,height=2,bg='orchid1').place(x=350,y=325)

    CONPASSWORDLABEL = Label(window,text=' Conform PASSWORD',font=('arial','18','bold'),bg='white',fg='maroon')
    CONPASSWORDLABEL.place(x=350,y=350)

    conpass_enter = Entry(window,width=25,fg='magenta2',font=('aial',14,'bold'),bd=0)
    conpass_enter.place(x =350, y=400)

    Frame(window,width=280,height=2,bg='orchid1').place(x=350,y=424)

    submitbutton = Button(window, text='Submit',bd =0,bg='magenta2',fg='white',font=('Open sans','16','bold'),width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_password)
    submitbutton.place(x=350,y=490)


    

   

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or password.get()=='':
        messagebox.showerror('error','all field are empty')
    
    else:
        try:
            con =pymysql.connect(host='localhost',user='root',password='1234')
            mycurser =con.cursor()
        except:
            messagebox.showerror('error','connection is not estiblished try again')
            return
        query='use Appdata'
        mycurser.execute(query)
        query='select * from data where username=%s and password=%s'
        mycurser.execute(query,(usernameEntry.get(),password.get()))
        row =mycurser.fetchone()
        if row == None:
            messagebox.showerror('Error','invalid password or user')
        else:
            messagebox.showinfo('sucess','welcome')
        loginWindow.destroy()
        import mainwin


def Monitor():
    loginWindow.destroy()
    import monitoring

def face():
    loginWindow.destroy()
    import FaceRecognition


def singup_page():
    loginWindow.destroy()
    import singup

def hide():
    openeye.config(file='closeye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)


def password_enter(event):
    if password.get()=='password':
        password.delete(0,END)

#GUI part

loginWindow = Tk()
loginWindow.geometry('700x600+50+50')
loginWindow.resizable(0,0)
loginWindow.title('Smart Home Log in Page')

bgimage = ImageTk.PhotoImage(file='naruto.png')
bglable = Label(loginWindow,image=bgimage)
bglable.grid()


heading=Label(loginWindow,text='USER LOGIN',font=('Microsoft yahel UI Light',23,'bold')
,bg='white',fg='maroon')
heading.place(x=350, y=30)

usernameEntry =Entry(loginWindow,width=20,font=('Microsoft yahel UI Light',23,'bold'),bd=0,fg='maroon')
usernameEntry.place(x=350, y=100)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)


frame1 = Frame(loginWindow,width=350,height=2,background='firebrick1')
frame1.place(x=348,y=140)



password =Entry(loginWindow,width=20,font=('Microsoft yahel UI Light',23,'bold'),bd=0,fg='maroon')
password.place(x=350, y=210)
password.insert(0,'password')

password.bind('<FocusIn>',password_enter)

frame2 = Frame(loginWindow,width=350,height=2,background='firebrick1')
frame2.place(x=348,y=250)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(loginWindow,image=openeye,bd=0,bg='white',activebackground='white'
,cursor='hand2',command=hide)
eyeButton.place(x=650, y=255)

forgetButton=Button(loginWindow,text='Forget password?',bd=0,bg='white',activebackground='white'
,cursor='hand2',font=('Microsoft yahel UI Light',9,'bold'),fg='maroon',activeforeground='maroon',command=forget_pass)
forgetButton.place(x=600, y=290)

loginButton=Button(loginWindow,text='LOG IN',font=('Open Sans',16,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=10,command=login_user)

loginButton.place(x=350, y=300)

orlabel=Label(loginWindow,text='----------------0r---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orlabel.place(x=370, y=350)

facebook_logo=PhotoImage(file='facebook.png')
fblabel=Label(loginWindow,image=facebook_logo,bg='white')
fblabel.place(x=370, y=400)

google_logo=PhotoImage(file='google.png')
googlelabel=Label(loginWindow,image=google_logo,bg='white')
googlelabel.place(x=430, y=400)

twitter_logo=PhotoImage(file='twitter.png')
twitterlabel=Label(loginWindow,image=twitter_logo,bg='white')
twitterlabel.place(x=490, y=400)

signuplabel=Label(loginWindow,text='Dont have account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signuplabel.place(x=370, y=500)

newaccountButton=Button(loginWindow,text='Create new one',font=('Open Sans',9,'bold'),
fg='black',bg='white',activeforeground='blue'
,activebackground='white',cursor='hand2',bd=0,command=singup_page)

newaccountButton.place(x=500,y=500)

MonitorButton=Button(loginWindow,text='Monitor',font=('Open Sans',16,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=10,command=Monitor)

MonitorButton.place(x=550, y=400)


faceButton=Button(loginWindow,text='face',font=('Open Sans',16,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=10,command=face)

faceButton.place(x=200, y=400)

loginWindow.mainloop()
