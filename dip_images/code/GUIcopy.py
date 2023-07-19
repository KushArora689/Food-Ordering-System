from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk


def openNewWindow():

    global img_label2
    global img_label_pass2
    global render2
    # Toplevel object which will
    # be treated as a new window
    root2 = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    root2.title("New Window")

    # sets the geometry of toplevel
    root2.geometry("500x300")

    load2 = Image.open('new-dip-project\\registerscreen3.jpg')
    render2 = ImageTk.PhotoImage(load2)
    img2 = Label(root2, image = render2)
    img2.place(x = -2, y =0)

    img_label2 = PhotoImage(file = 'new-dip-project\\label-image.png')
    name = Label(root2, image = img_label, bg = '#292929').place(x = 130,y = 86)

    img_label_pass2 = PhotoImage(file = 'new-dip-project\\label_pass.png')
    name = Label(root2, image = img_label_pass, bg = '#292929').place(x = 120,y = 173)



    email = Entry(root2).place(x = 290, y = 180)
    password = Entry(root2).place(x = 290, y = 90)






root = Tk()

root.geometry('670x466')
load = Image.open('new-dip-project\\food.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = -26, y =0)
img_login = PhotoImage(file = 'new-dip-project\\button (3).png')
b1 = Button(root,image = img_login,bd = 0, bg = '#3b353b', activebackground = '#3b353b')
b1.place(x = 275, y = 310)



img_register = PhotoImage(file = 'new-dip-project\\register.png')
b2 = Button(root,image = img_register, command = openNewWindow, bd = 0, bg = '#3b353b', activebackground = '#3b353b')
b2.place(x = 265, y = 400)

canvas = Canvas(root, width = 400, height = 120)
canvas.pack()
img4 = ImageTk.PhotoImage(Image.open('new-dip-project\\goode.png'))
canvas.create_image(20, 20, anchor=NW, image=img4)



email = Entry(root).place(x = 340, y = 180)
password = Entry(root).place(x = 340, y = 250)

img_label = PhotoImage(file = 'new-dip-project\\label-image.png')
name = Label(root, image = img_label, text = "Email:", bg = '#3c3a3b').place(x = 197,y = 178)

img_label_pass = PhotoImage(file = 'new-dip-project\\label_pass.png')
name = Label(root, image = img_label_pass, text = "Password:", bg = '#3c3a3b').place(x = 177,y = 245)




def create_newuser():
    global email
    global password
    global user_name

    user_name = str(email.get()) #this code is getting the users input from the username entry box

    if len(user_name) >= 1: #if user has inputted a letter or number it will allow it to go to the next function
        create_newpass()
        username_length.destroy()
    else:
        username_length.configure(text="""Please enter a username""", font=("12"), bg="skyblue", fg="red")



def create_newpass():
    global email
    global password_entry
    global pass_word

    pass_word = str(password.get()) #this code is getting the users input from the password entry box

    if len(pass_word) >= 8: #if the characters gotten from the pasword entry is less than 8, an erorr message will appear

        password_length.configure(text="", font=("2"), bg="skyblue", fg="white")
        password_length.grid(row=40, column=2)
        age_check()
    else:
        password_length.configure(text="""Your password must
be atleast eight characters long. Please try
again""", font=("bold", "12"), bg="skyblue", fg="red")



root.mainloop()
