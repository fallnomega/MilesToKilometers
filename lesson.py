
# #unlimited arguements
#
# def add(*args):
#     total = 0
#     for n in args:
#         total+=n
#     print(total)
#
# add(1,2,3,4)

# # how to reference **kwargs aka key word arguments (unlimited number of args)
# def calculate(n, **kwargs):
#     # n is 2 in the function call below
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#         print(kwargs["add"])
#         n += kwargs["add"]
#         n *= kwargs["multiply"]
#         print(n)
#
#
# calculate(2, add=3, multiply=5)  # these kwargs pretty much make a dictionary like add <key> and 3 <value>
#
#
# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#         self.colour = kw.get("colour")
#         # if you dont supply values for make and model, then it will error
#         # to bypass it do something like
#         # self.make = kw.get("make")
#         # self.model = kw.get("model")
#         # this will return None instead if nothing is supplied to it
#
#
# my_car = Car(make="BMW", model="435i")
#
# print(my_car.make)
# print(my_car.model)
# print(my_car.colour)
#
#
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)


import tkinter

def change_text():
    my_label['text'] = input.get()

def button_clicked():
    print("I got clicked!")

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

# Labels

my_label = tkinter.Label(text= "I am a Label",font=("Arial",24,"bold","italic","underline"))
#show on screen and where in the window
# my_label.pack() #auto centers it on screen if () left blank
# my_label.pack(side="left") # put on left side of screen
# my_label.pack(expand=True) #take up the screen
# my_label.pack()

# Place is positioning it on x,y layout
# my_label.place(x=200,y=200)

# Grid, another way of locating a label to somewhere on the window.
# Guess think of it like a spreadsheet or 2d array and moving around that way

#NOTe you cant mix grid and pack, errors arise from it.

my_label.grid(column=0,row=1)

#change label text
my_label['text'] = "My new text"
# or
my_label.config(text="My new new text")



#Buttons
# button = tkinter.Button(text="Click Me",command=button_clicked)
button = tkinter.Button(text="Click Me",command=change_text)
# button.pack()
button.grid(row=2,column=1)
#Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(row=3,column=2)


#pack packs widgets together and on top of one another. side parameter will adjust it to where it packs (left,right, etc)
#keep window running instead of auto exit when script run.

# needs to be at end of program
window.mainloop()