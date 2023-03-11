from tkinter import*
import tkinter as tk
import cv2
import tkinter.filedialog as filedialog
from tkinter import messagebox
import pyfirmata
import time
from pyfirmata import Arduino,util

port = "COM5"
board = pyfirmata.Arduino(port)


Main_window = Tk()
Main_window.title('Smart Home singup  Page')
Main_window.geometry('700x700+50+50')


led = board.get_pin('d:13:o')
pin_number = 7
relay_pin = board.get_pin('d:{}:o'.format(pin_number))




def back():
    Main_window.destroy()
    import singin

def on():
    led.write(1)

def off():
    led.write(0)

def fanon():
    relay_pin.write(0)
    time.sleep(5)

def fanoff():
   relay_pin.write(1)
        





# Create a function to select the save location
def select_location():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")

# initialize the camera
cap = cv2.VideoCapture(0)

# specify the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = None

def start_recording():
    global out
    file_path = filedialog.asksaveasfilename(defaultextension=".avi")
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

    while True:
        # capture the frame from the camera
        ret, frame = cap.read()

        # write the frame to the video file
        out.write(frame)

        # display the frame
        cv2.imshow("frame", frame)

        # break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Create a function to take a picture
def take_picture():
     global file_path
     file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
  
    # Start the camera
     cap = cv2.VideoCapture(0)

    # Read a single frame from the camera
     ret, frame = cap.read()

    # Save the frame as an image file
     cv2.imwrite(file_path, frame)

    # Release the camera
     cap.release()

    # Update the GUI with a message
     label.config(text="Picture taken and saved!")



# Create a label to show messages
label = tk.Label(text="")
label.pack()




heading=Label(Main_window,text='welcome owner',font=('Microsoft yahel UI Light',16,'bold')
,bg='white',fg='maroon')
heading.place(x=350, y=30)


TakepicButton=Button(Main_window,text='TAKE_PICTURE',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command =take_picture,)

TakepicButton.place(x=500, y=400)


RecordButton=Button(Main_window,text='RECORD_VIDEO',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command =start_recording)

RecordButton.place(x=500, y=450)

soundButton=Button(Main_window,text='FANON',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command= fanon)

soundButton.place(x=500, y=500)

soundButton=Button(Main_window,text='FAN OFF',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command= fanoff)

soundButton.place(x=50, y=500)

exitButton=Button(Main_window,text='Exit',font=('Open Sans',20,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command= back)

exitButton.place(x=50, y=550)



lightonButton=Button(Main_window,text='LIGHT_ON',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12,command= on)

lightonButton.place(x=500, y=550)

lightoffButton=Button(Main_window,text='LIGHT_OFF',font=('Open Sans',18,'bold'),
fg='white',bg='firebrick1',activeforeground='maroon'
,activebackground='white',cursor='hand2',bd=0,width=12, command= off)

lightoffButton.place(x=300, y=550)




Main_window.mainloop()