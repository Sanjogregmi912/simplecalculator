from tkinter import *

root=Tk()
#title of the project
root.title("calculator")
#geometry of the GUI
root.geometry("400x400")
#number entry box
e1=Entry(root,width=60)
e1.grid(row=0,column=0,padx=10,pady=10)
def button_click(number):
    current=e1.get()
    e1.delete=(0,End)
    e1.insert(0,str(current)+str(number))
def button_clear():
    e1.delete(0,END)
def button_add():
    first_number=e1.get()
    global f_num
    f_num=int(first_number)
    e1.delete(0,END)
def button_equal():
    second_number=e1.get()
    e1.delete(0,END)
    e1.insert(0,f_num +int(second_number))
    e1.insert(0,f_num*int(second_number))
    e1.insert(0,f_num/int(second_number))
    e1.insert(0,f_num-second_number)



root.mainloop()