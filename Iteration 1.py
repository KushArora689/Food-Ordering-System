from tkinter import*
from PIL import Image, ImageTk
import tkinter as ttk
import os

## creating lists where data is stored and where data is appended
accounts = []



##creating and defining a class called Goode_brothers
class Goode_brothers:

##creating an innit function
    def __init__(self, parent):

        ## creating a frame for the window
        self.my_frame = Frame(parent)
        ##packing the frame
        self.my_frame.pack()

        ## defining and making an image as a background
        self.background = Image.open('dip_images\\food.jpg')
        self.background_image = ImageTk.PhotoImage(self.background)
        self.img = Label(parent, image = self.background_image)
        self.img.place(x = -26, y =0)

        ## creating a login button as an image so it looks visually appealing
        self.img_login = PhotoImage(file = 'dip_images\\button (3).png')
        self.login_button = Button(parent,image = self.img_login, bd = 0, cursor = "hand2", bg = '#3b353b', activebackground = '#3b353b')
        self.login_button.place(x = 275, y = 340)

        ## creating a register button as an image so it looks visually appealing
        self.img_register = PhotoImage(file = 'dip_images\\register.png')
        self.register_button = Button(parent,image = self.img_register, command = self.open_register, cursor = "hand2", bd = 0, bg = '#3b353b', activebackground = '#3b353b')
        self.register_button.place(x = 265, y = 400)

        ## creating a canvas and packing it, this canvas is the the title called "Goode brothers"
        self.canvas = Canvas(parent, width = 400, height = 120)
        self.canvas.pack()
        self.goode_img = ImageTk.PhotoImage(Image.open('dip_images\\goode.png'))
        self.canvas.create_image(20, 20, anchor=NW, image=self.goode_img)

        ## creating an entry where the user types in their email
        self.email = Entry(parent)
        self.email.place(x = 340, y = 180)

        ## creating an entry where the user types in their password, the password will show as '●' instead of letters
        self.password = Entry(parent, show = '●')
        self.password.place(x = 354, y = 250)

        ##creating a label for email as an image to make the page look visually appealing
        self.email_label = PhotoImage(file = 'dip_images\\label-image.png')
        self.e_label = Label(parent, image = self.email_label, text = "Email:", bg = '#3c3a3b').place(x = 197,y = 178)

        ##creating a label for password as an image to make the page look visually appealing
        self.password_label = PhotoImage(file = 'dip_images\\label_pass.png')
        self.p_label = Label(parent, image = self.password_label, text = "Password:", bg = '#3c3a3b').place(x = 177,y = 245)


    ## creating and defining the function as "open_register(self)"
    def open_register(self):

        # Toplevel object which will
        # be treated as a new window
        self.root2 = Toplevel(root)

        # sets the title of the
        # Toplevel widget
        self.root2.title("Register")

        # sets the geometry of toplevel
        self.root2.geometry("500x300")

        ## creating a label as an image so the new window looks visually appealing
        self.load_register = Image.open('dip_images\\registerscreen3.jpg')
        self.register_render2 = ImageTk.PhotoImage(self.load_register)
        self.register_img = Label(self.root2, image = self.register_render2)
        self.register_img.place(x = -2, y =0)

        ## creating a label as an image so the new window looks visually appealing
        self.user_label = PhotoImage(file = 'dip_images\\label-image.png')
        self.user_label2 = Label(self.root2, image = self.user_label, bg = '#292929').place(x = 130,y = 102)

        ## creating a label as an image so the new window looks visually appealing
        self.img_label_pass2 = PhotoImage(file = 'dip_images\\label_pass.png')
        self.pass_label = Label(self.root2, image = self.img_label_pass2, bg = '#292929').place(x = 120,y = 173)

        ##creating an entry for email
        self.email2 = Entry(self.root2)
        self.email2.place(x = 280, y = 104)

        ##creating an entry for password
        self.password2 = Entry(self.root2)
        self.password2.place(x = 280, y = 180)

        ## creating a register button as an image so it looks visually appealing
        self.img_register2 = PhotoImage(file = 'dip_images\\register.png')
        self.button_register = Button(self.root2,image = self.img_register2, cursor = "hand2", bd = 0, bg = '#0d0d0d', activebackground = '#0d0d0d')
        self.button_register.place(x = 180, y = 250)

        ## creating a label as an image so the new window looks visually appealing
        self.img_reg2 = PhotoImage(file = 'dip_images\\regtitle.png')
        self.reg_label = Label(self.root2, image = self.img_reg2, bg = '#131313')
        self.reg_label.place(x = 109, y = 10)





## main routine
if __name__ == "__main__":
    root = Tk()
    ## size of window
    root.geometry('670x466')
    FoodSystem = Goode_brothers(root)
    ## title of window
    root.title('Goode brothers')
    ## running the program
    root.mainloop()
