##importing all the models needed to create the program
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
        self.login_button = Button(parent,image = self.img_login, command = self.read_info, bd = 0, cursor = "hand2", bg = '#3b353b', activebackground = '#3b353b')
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
        self.button_register = Button(self.root2,image = self.img_register2, command = self.create_email, cursor = "hand2", bd = 0, bg = '#0d0d0d', activebackground = '#0d0d0d')
        self.button_register.place(x = 180, y = 250)

        ## creating a label as an image so the new window looks visually appealing
        self.img_reg2 = PhotoImage(file = 'dip_images\\regtitle.png')
        self.reg_label = Label(self.root2, image = self.img_reg2, bg = '#131313')
        self.reg_label.place(x = 109, y = 10)


    ## creating a function for creating password
    def create_pass(self):

        ## creating a label
        self.password_length = Label(self.root2, text = '')
        self.password_length.place(x = 80, y = 140)

        ## getting what the user entered
        self.pass_word = str(self.password2.get())

        ## if password is equal to or greater than 8 characters then the next function will run
        if len(self.pass_word) >= 8:
            self.save_info()
            self.registered = Label(self.root2, text = 'You have successfully registered, this window will now automatically close', font=("open sans", "8"))
            self.registered.place(x = 80, y = 140)
            ## the window will close automatically after 1.5 seconds
            self.root2.after(1500, self.root2.destroy)
        else:
            ## if conditions are not satisfied then program will ask to retry
            self.password_length.configure(text="""Your password must be atleast eight characters long. Please try again""", font=("open sans", "8"))


    ## creating a function for creating email
    def create_email(self):

        ## creating a label
        self.username_length = Label(self.root2, text = '', font = '40')
        self.username_length.place(x = 165, y = 140)

        ## getting what the user entered
        self.email_reg = str(self.email2.get())

        ## if email is equal to or greater than 1 character then the next function will run
        if len(self.email_reg) >= 1:
            self.create_pass()
            self.username_length.destroy()
        else:
            ## if conditions are not satisfied then program will ask to retry
            self.username_length.configure(text='Please enter your username or password', font=("open sans", "8"))
            self.username_length.after(3000, self.username_length.destroy)




    ## creating a function
    def save_info(self):

        ## getting what the user entered for email and password
         self.email_reg = str(self.email2.get())
         self.pass_word = str(self.password2.get())
         print(self.email2)
         ## opening the text file where credentials will be stored
         file = open('emails.txt', 'a+')
         ## writing the user credentials first email and the password, seprerating with a comma
         file.write(self.email_reg + ', ' + self.pass_word + '\n')


    ## creating a function
    def read_info(self):

        ##opening file in which details are stored
        with open("emails.txt") as read_ep:
            for line in read_ep:
                ##appending the details in a list
                accounts.append(line.strip().split(", "))
        ## getting what the user entered for email and password
        credential = [self.email.get(), self.password.get()]
        ## if what the user entered is in the list then user can continue
        if credential in accounts:
            self.open_menu()
        else:
            ## if the above conditions are not satisfied then user has th=o retry and this function will repeat until logged in
            self.ep_notexist = Label(root, text = "Your Email or Password is incorrect, Please try again", font=("open sans", "8"))
            self.ep_notexist.place(x = 210, y = 300)
            self.ep_notexist.after(4000, self.ep_notexist.destroy)
            self.email.delete(0, END)
            self.password.delete(0, END)


    ## creating a function for home page
    def open_menu(self):

        ## destroying the widgets
        for wid in root.winfo_children():
            wid.destroy()
        ## destroying the previous frame
        self.my_frame.destroy()
        ## creating a new frame, packing it and expanding it to the size of the window
        self.my_frame2 = Frame(root)
        self.my_frame2.pack(fill = "both", expand = 1)

        ## creation a label as an image for the title so the some page looks visually appelaing
        self.title_home = PhotoImage(file = 'dip_images\\goode.png')
        self.title2 = Label(self.my_frame2, image = self.title_home).pack()

        ## creating a button as an image to make the home page look modern
        self.img_menu = PhotoImage(file = 'dip_images\\menu_button.png')
        self.button_menu = Button(self.my_frame2,image = self.img_menu,  command = self.view_menu, cursor = "hand2", bd  = 0)
        self.button_menu.place(x = 246, y = 140)

        ## creating a button as an image to make the home page look modern
        self.img_order = PhotoImage(file = 'dip_images\\order_button.png')
        self.button_order = Button(self.my_frame2,image = self.img_order, command = self.order_menu, cursor = "hand2", bd  = 0)
        self.button_order.place(x = 239, y = 228)

        ## creating a button as an image to make the home page look modern
        self.img_checkout = PhotoImage(file = 'dip_images\\checkout.png')
        self.button_checkout = Button(self.my_frame2,image = self.img_checkout, command = self.cart_order, cursor = "hand2", bd  = 0)
        self.button_checkout.place(x = 250, y = 316)



        ## creating a function for viewing menu
    def view_menu(self):

            ## forgetting the previous frame
        self.my_frame2.pack_forget()
            ## creating a new frame and packing it
        self.my_frame3 = LabelFrame(root, height = 700)
        self.my_frame3.place(x = 115, y = 40)


        ## creating a function for ordering
    def order_menu(self):


            ## destroing the previous frame
        self.my_frame2.destroy()
            ## creating a new frame and packing it
        self.my_frame4 = Frame(root)
        self.my_frame4.pack(fill = "both", expand = 1)


    def cart_order(self):
            ##creating a new window
        self.root3 = Toplevel(root)
        self.root3.geometry("600x400")

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
