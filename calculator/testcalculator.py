from tkinter import *

root=Tk()
#title of the project
root.title("calculator")
#geometry of the GUI
#root.geometry("450x600")
#number entry box
e1=Entry(root,width=35,borderwidth=5)
e1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e1.insert(0,"enter any number:  ")
def button_click(number):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))
def button_clear():
    e1.delete(0,END)
def button_add():
    first_number=e1.get()
    global f_num
    f_num=int(first_number)
    e1.delete(0,END)
def button_subtract():
    first_number=e1.get()
    global f_num
    f_num=int(first_number)
    e1.delete(0,END)
def button_multiply():
    first_number=e1.get()
    global f_num
    f_num=int(first_number)
    e1.delete(0,END)
def button_equal():
    second_number=e1.get()
    e1.delete(0,END)
    e1.insert(0,f_num + int(second_number))
    e1.insert(0,f_num - int(second_number))
    e1.insert(0,f_num * int(second_number))

#defing the buttoms
buttom_1=Button(root, text="1",padx=40,pady=20,command=lambda : button_click(1))
buttom_2=Button(root,text="2",padx=40,pady=20,command=lambda : button_click(2))
buttom_3=Button(root,text="3",padx=40,pady=20,command=lambda : button_click(3))
buttom_4=Button(root,text="4",padx=40,pady=20,command=lambda : button_click(4))
buttom_5=Button(root,text="5",padx=40,pady=20,command=lambda : button_click(5))
buttom_6=Button(root,text="6",padx=40,pady=20,command=lambda : button_click(6))
buttom_7=Button(root,text="7",padx=40,pady=20,command=lambda : button_click(7))
buttom_8=Button(root,text="8",padx=40,pady=20,command=lambda : button_click(8))
buttom_9=Button(root,text="9",padx=40,pady=20,command=lambda : button_click(9))
buttom_0=Button(root,text="0",padx=40,pady=20,command=lambda : button_click(0))
buttom_add=Button(root,text="+",padx=39,pady=20,command=button_add)
buttom_equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
buttom_clear=Button(root,text="clear",padx=79,pady=20,command=button_clear)
button_subtract=Button(root,text="-",padx=39,pady=20,command=button_subtract)
button_multiply=Button(root,text="*",padx=39,pady=20,command=button_multiply)
#putting buttons on the screen
buttom_1.grid(row=3,column=0)
buttom_2.grid(row=3,column=1)
buttom_3.grid(row=3,column=2)

buttom_4.grid(row=2,column=0)
buttom_5.grid(row=2,column=1)
buttom_6.grid(row=2,column=2)

buttom_7.grid(row=1,column=0)
buttom_8.grid(row=1,column=1)
buttom_9.grid(row=1,column=2)

buttom_0.grid(row=4,column=0)
buttom_clear.grid(row=4,column=1,columnspan=2)

buttom_add.grid(row=5,column=0)
buttom_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)






root.mainloop()