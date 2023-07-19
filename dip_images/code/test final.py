from tkinter import*
from PIL import Image, ImageTk
import tkinter as tk


accounts = []
food = ['Pizza','Burger','Nachos', 'French Toast']
foodprice=['20','9.50','7.50', '17']
drinks = ['Pepsi','Lemonade','Tea', 'Aperitivo Spritz']
drinksprice = ['3','4','3', '15.50']
orderlist = []



class Goode_brothers:


    def __init__(self, parent):

        self.myFrame = Frame(parent)
        self.myFrame.pack()

        self.background = Image.open('dip-project-kush\\food2.jpg')
        self.background_image = ImageTk.PhotoImage(self.background)
        self.img = Label(parent, image = self.background_image)
        self.img.place(x = -26, y =0)

        self.img_login = PhotoImage(file = 'dip-project-kush\\button (3).png')
        self.login_button = Button(parent,image = self.img_login, command = self.read_info, bd = 0, bg = '#3b353b', activebackground = '#3b353b')
        self.login_button.place(x = 275, y = 340)

        self.img_register = PhotoImage(file = 'dip-project-kush\\register.png')
        self.register_button = Button(parent,image = self.img_register, command = self.openNewWindow, bd = 0, bg = '#3b353b', activebackground = '#3b353b')
        self.register_button.place(x = 265, y = 400)

        self.canvas = Canvas(parent, width = 400, height = 120)
        self.canvas.pack()
        self.goode_img = ImageTk.PhotoImage(Image.open('dip-project-kush\\goode.png'))
        self.canvas.create_image(20, 20, anchor=NW, image=self.goode_img)

        self.email = Entry(parent)
        self.email.place(x = 340, y = 180)

        self.password = Entry(parent)
        self.password.place(x = 354, y = 250)

        self.email_label = PhotoImage(file = 'dip-project-kush\\label-image.png')
        self.e_label = Label(parent, image = self.email_label, text = "Email:", bg = '#3c3a3b').place(x = 197,y = 178)

        self.password_label = PhotoImage(file = 'dip-project-kush\\label_pass.png')
        self.p_label = Label(parent, image = self.password_label, text = "Password:", bg = '#3c3a3b').place(x = 177,y = 245)




    def openNewWindow(self):

        # Toplevel object which will
        # be treated as a new window
        self.root2 = Toplevel(root)

        # sets the title of the
        # Toplevel widget
        self.root2.title("New Window")

        # sets the geometry of toplevel
        self.root2.geometry("500x300")

        self.load2 = Image.open('dip-project-kush\\registerscreen3.jpg')
        self.render2 = ImageTk.PhotoImage(self.load2)
        self.img2 = Label(self.root2, image = self.render2)
        self.img2.place(x = -2, y =0)

        self.img_label2 = PhotoImage(file = 'dip-project-kush\\label-image.png')
        self.name = Label(self.root2, image = self.img_label2, bg = '#292929').place(x = 130,y = 102)

        self.img_label_pass2 = PhotoImage(file = 'dip-project-kush\\label_pass.png')
        self.name = Label(self.root2, image = self.img_label_pass2, bg = '#292929').place(x = 120,y = 173)

        self.email2 = Entry(self.root2)
        self.email2.place(x = 280, y = 104)

        self.password2 = Entry(self.root2)
        self.password2.place(x = 280, y = 180)

        self.img_register2 = PhotoImage(file = 'dip-project-kush\\register.png')
        self.b3 = Button(self.root2,image = self.img_register2, command = self.create_email, bd = 0, bg = '#0d0d0d', activebackground = '#0d0d0d')
        self.b3.place(x = 180, y = 250)

        self.img_reg2 = PhotoImage(file = 'dip-project-kush\\regtitle.png')
        self.name9 = Label(self.root2, image = self.img_reg2, bg = '#131313')
        self.name9.place(x = 109, y = 10)



    def create_pass(self):

        self.password_length = Label(self.root2, text = '')
        self.password_length.place(x = 80, y = 140)

        self.pass_word = str(self.password2.get())

        if len(self.pass_word) >= 8:
            self.save_info()
            self.registered = Label(self.root2, text = 'You have successfully registered, this window will now automatically close', font=("open sans", "8"))
            self.registered.place(x = 80, y = 140)
            self.root2.after(3000, self.root2.destroy)
        else:
            self.password_length.configure(text="""Your password must be atleast eight characters long. Please try again""", font=("open sans", "8"))



    def create_email(self):

        self.username_length = Label(self.root2, text = '', font = '40')
        self.username_length.place(x = 165, y = 140)

        self.email_reg = str(self.email2.get())

        if len(self.email_reg) >= 1:
            self.create_pass()
            self.username_length.destroy()
        else:
            self.username_length.configure(text='Please enter your username or password', font=("open sans", "8"))
            self.username_length.after(3000, self.username_length.destroy)




    def save_info(self):

         self.email_reg = str(self.email2.get())
         self.pass_word = str(self.password2.get())
         print(self.email2)
         file = open('emails.txt', 'a+')
         file.write(self.email_reg + ', ' + self.pass_word + '\n')



    def read_info(self):

        with open("emails.txt") as read_ep:
            for line in read_ep:
                accounts.append(line.strip().split(", "))

        credential = [self.email.get(), self.password.get()]
        if credential in accounts:
            self.openMenu()
        else:
            self.ep_notexist = Label(root, text = "Your Email or Password is incorrect, Please try again", font=("open sans", "8"))
            self.ep_notexist.place(x = 210, y = 300)
            self.ep_notexist.after(4000, self.ep_notexist.destroy)




    def openMenu(self):

        for wid in root.winfo_children():
            wid.destroy()
        self.myFrame.destroy()

        self.myFrame2 = Frame(root)
        self.myFrame2.pack(fill = "both", expand = 1)

        self.title_home = PhotoImage(file = 'dip-project-kush\\goode.png')
        self.title2 = Label(self.myFrame2, image = self.title_home).pack()

        self.img_menu = PhotoImage(file = 'dip-project-kush\\menu_button.png')
        self.button_menu = Button(self.myFrame2,image = self.img_menu, command = self.view_menu, bd  = 0)
        self.button_menu.place(x = 246, y = 140)

        self.img_order = PhotoImage(file = 'dip-project-kush\\order_button.png')
        self.button_order = Button(self.myFrame2,image = self.img_order, command = self.order_menu, bd  = 0)
        self.button_order.place(x = 239, y = 228)

        self.img_checkout = PhotoImage(file = 'dip-project-kush\\checkout.png')
        self.button_checkout = Button(self.myFrame2,image = self.img_checkout, bd  = 0, command = self.cart_order)
        self.button_checkout.place(x = 250, y = 316)



    def view_menu(self):

        self.myFrame2.pack_forget()
        self.myFrame3 = LabelFrame(root, height = 700)
        self.myFrame3.pack()

        self.myFrame3.columnconfigure(0, weight=1)
        self.myFrame3.columnconfigure(1, weight=2)

        self.food_title = Label(self.myFrame3, font=("Impact", "23"), text = 'Food').grid(row = 0, column = 4)
        self.food_space = Label(self.myFrame3, text = '').grid(row = 1, column = 4)
        self.drinks_title = Label(self.myFrame3, font=("Impact", "23"), text = 'Drinks').grid(row = 8, column = 4)

        self.price = Label(self.myFrame3, font=("Impact", "23"), text = 'Price($)').grid(row = 0, column = 8)


        for x in range (len(food)):
            self.foodop = Label(self.myFrame3, font=("Impact", "15"), text = food[x]).grid(row = 3+x, column = 4)
            self.fprice = Label(self.myFrame3, font=("Impact", "15"), text = foodprice[x]).grid(row = 3+x, column = 8)

        for x in range (len(drinks)):
            self.drinksop = Label(self.myFrame3, font=("Impact", "15"), text = drinks[x]).grid(row = 5+(len(food))+x, column = 4)
            self.drinksp = Label(self.myFrame3, font=("Impact", "15"), text = drinksprice[x]).grid(row = 5+(len(food))+x, column = 8)


        self.img_back = PhotoImage(file = 'dip-project-kush\\back_button.png')
        self.back_button = Button(self.myFrame3,image = self.img_back, command = self.openMenu, bd  = 0)
        self.back_button.grid(row = 38, column = 7)




    def callback(self):

        self.info_label.configure(text=self.tkvar.get(), font=("Courier New","12"))
        self.info_label2.configure(text=self.tkvar2.get(), font=("Courier New","12"))
        self.position2 = drinks.index(self.tkvar2.get())
        self.position = food.index(self.tkvar.get())
        self.tkvar.trace('w', self.food_optionmenu)
        self.tkvar2.trace('w', self.drink_optionmenu)
        self.total_price = 0
        self.total_price = float(foodprice[self.position]) + float(drinksprice[self.position2])
        orderlist.insert(0,[self.tkvar.get(),self.tkvar2.get(), self.total_price])
        Label(self.myFrame4, text = str(self.total_price)).place(x=20, y = 50)
        print (orderlist)




    def cart_order(self):


        self.root3 = Toplevel(root)
        self.root3.geometry("600x400")


        self.img_back2 = PhotoImage(file = 'dip-project-kush\\bbutton.png')
        self.back_button2 = Button(self.root3, image = self.img_back2, bd = 0, command = self.openMenu)
        self.back_button2.grid(column=0, row = 1)

        self.img_cart = PhotoImage(file = 'dip-project-kush\\your_cart.png')
        self.y_cart = Label(self.root3, image = self.img_cart).grid(column=3, row = 1)

        Label(self.root3, text = "",font=("Courier New","12")).grid(column = 1, row = 1)
        Label(self.root3, text = "",font=("Courier New","12")).grid(column = 1, row = 2)
        Label(self.root3, text = "Food",font=("Courier New","12")).grid(column = 2, row = 3)
        Label(self.root3, text = "Drinks",font=("Courier New","12")).grid(column = 3, row = 3)
        Label(self.root3, text = "Price($)",font=("Courier New","12")).grid(column = 4, row = 3)
        Label(self.root3, text = "",font=("Courier New","12")).grid(column = 1, row = 4)

        for x in range (len(orderlist)):
            Label(self.root3, text = (str(x+1)),font=("Courier New","12")).grid(column =0, row= x+5)
            Label(self.root3, text = (orderlist[x][0]), font=("Courier New","12")).grid(column=2, row = x+5)
            Label(self.root3, text = (orderlist[x][1]), font=("Courier New","12")).grid(column=3, row = x+5)
            Label(self.root3, text = (orderlist[x][2]), font=("Courier New","12")).grid(column=4, row = x+5)


            self.totalorderprice = 0

            for x in range (len(orderlist)):
                self.totalorderprice = self.totalorderprice + (orderlist[x][2])

            Label(self.root3, text = "",font=("Courier New","12")).grid(column = 3, row = x+8)
            Label(self.root3, text = self.totalorderprice,font=("Courier New","12")).grid(column = 3, row = x+10)
            Label(self.root3, text = "Total Price ($)",font=("Courier New","12")).grid(column = 3, row = x+9)



    def order_menu(self):

        self.myFrame2.destroy()
        self.myFrame4 = Frame(root)
        self.myFrame4.pack(fill = "both", expand = 1)

        self.info_label = Label(self.myFrame4, text="")
        self.info_label.place(x = 260, y = 260)

        self.info_label2 = Label(self.myFrame4, text="")
        self.info_label2.place(x = 258, y = 240)

        self.tkvar = StringVar(self.myFrame4)
        self.tkvar.set("Food")
        self.tkvar.trace_add('write', lambda *args: print(self.tkvar.get()))

        self.tkvar2 = StringVar(self.myFrame4)
        self.tkvar2.set("Drinks")
        self.tkvar2.trace_add('write', lambda *args: print(self.tkvar2.get()))

        self.img_odmenu = PhotoImage(file = 'dip-project-kush\\od_menu.png')
        self.order_menu_message = Label(self.myFrame4, image = self.img_odmenu).place(x = 220)

        self.foodMenu = OptionMenu(self.myFrame4, self.tkvar, *['Pizza','Burger','Nachos', 'French Toast'])
        self.foodMenu.place(x = 160, y = 110)

        self.Foodlabel = Label(self.myFrame4, text="Choose Your Food", font=("Courier New","12"))
        self.Foodlabel.place(x = 145, y = 83)

        self.drinklabel = Label(self.myFrame4, text="Choose Your Drink", font=("Courier New","12"))
        self.drinklabel.place(x = 370, y = 83)

        self.drinkMenu = OptionMenu(self.myFrame4, self.tkvar2, *['Pepsi','Lemonade','Tea', 'Aperitivo Spritz'])
        self.drinkMenu.place(x = 385, y = 110)

        self.pricelabel = Label(self.myFrame4, text = "In your cart:", font=("Courier New","12"))
        self.pricelabel.place(x = 286, y = 208)

        self.order_btn1 = PhotoImage(file = 'dip-project-kush\\orderb.png')
        self.order_button2 = Button(self.myFrame4, text = "SHOW", image = self.order_btn1, command = self.calculate_order, bd = 0)
        self.order_button2.place(x = 302, y = 160)

        self.check_btn = PhotoImage(file = 'dip-project-kush\\checkpay.png')
        self.checkout_btn = Button(self.myFrame4, image = self.check_btn, bd = 0, command = self.cart_order)
        self.checkout_btn.place(x = 267, y = 410)

        self.img_back3 = PhotoImage(file = 'dip-project-kush\\bbutton.png')
        self.back_button3 = Button(self.myFrame4, image = self.img_back3, bd = 0, command = self.openMenu)
        self.back_button3.place(x = 50, y = 410)



    def calculate_order(self):
        self.position2 = drinks.index(self.tkvar2.get())
        self.position = food.index(self.tkvar.get())
        self.tkvar.trace('w', self.food_optionmenu)
        self.tkvar2.trace('w', self.drink_optionmenu)
        self.total_price = 0
        self.total_price = float(foodprice[self.position]) + float(drinksprice[self.position2])
        orderlist.insert(0,[self.tkvar.get(),self.tkvar2.get(), self.total_price])
        print (orderlist)




    def food_optionmenu(self, *args):
        self.position = food.index(self.tkvar.get())


    def drink_optionmenu(self, *args):
        self.position2 = drinks.index(self.tkvar2.get())
        self.tkvar.trace('w', self.food_optionmenu)
        self.tkvar2.trace('w', self.drink_optionmenu)








if __name__ == "__main__":
    root = Tk()
    root.geometry('670x466')
    FoodSystem = Goode_brothers(root)
    root.title('Goode brothers')
    root.mainloop()
