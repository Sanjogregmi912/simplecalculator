from tkinter import *
root=Tk()
#font for the calculator
font="vandana",22
#title of the window
root.title("simple calculator")
#size of the calculator
root.geometry('430x500')
#heading
heading_label=Label(root,text="My calculator",font="vandana")
heading_label.pack(side=TOP)
#entry box
entry=Entry(root,borderwidth=5,justify=CENTER)
entry.pack(side=TOP,pady=10,padx=10,fill=X)
#buttom frame
buttom_frame=Frame(root)
buttom_frame.pack(side=TOP)
#function
def click_button(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))
def add():
    firstnumber=entry.get()
    global f_num
    global math
    math="addition"
    f_num=float(firstnumber)
    entry.delete(0,END)
def subtract():
    firstnumber=entry.get()
    global f_num
    global math
    math="subtraction"
    f_num=float(firstnumber)
    entry.delete(0,END)
def multiply():
    firstnumber=entry.get()
    global f_num
    global math
    math="multiplication"
    f_num=float(firstnumber)
    entry.delete(0,END)
def divide():
    firstnumber=entry.get()
    global f_num
    global math
    math="division"
    f_num=float(firstnumber)
    entry.delete(0,END)
def square():
    firstnumber=entry.get()
    global f_num
    global math
    math="square"
    f_num=float(firstnumber)
    entry.delete(0,END)
def clear():
    entry.delete(0,END)
def Equal():
    secondnumber=entry.get()
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0,f_num + float(secondnumber))
    elif math=="subtraction":
        entry.insert(0,f_num - float(secondnumber))
    elif math=="multiplication":
        entry.insert(0,f_num * float(secondnumber))
    elif math=="division":
        entry.insert(0,f_num / int(secondnumber))
    elif math=="square":
        entry.insert(0,f_num ** int(secondnumber))






#adding buttons
button_1=Button(buttom_frame,text=1,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(1))
button_2=Button(buttom_frame,text=2,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(2))
button_3=Button(buttom_frame,text=3,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(3))
button_4=Button(buttom_frame,text=4,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(4))
button_5=Button(buttom_frame,text=5,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(5))
button_6=Button(buttom_frame,text=6,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(6))
button_7=Button(buttom_frame,text=7,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(7))
button_8=Button(buttom_frame,text=8,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(8))
button_9=Button(buttom_frame,text=9,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(9))
button_0=Button(buttom_frame,text=0,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=lambda :click_button(0))
button_dot=Button(buttom_frame,text=".",font=font,padx=5,pady=5,width=5,borderwidth=2,command=lambda :click_button("."))
button_equal=Button(buttom_frame,text="=",font=font,padx=6,pady=5,width=11,borderwidth=2,relief="solid",command=Equal
                    ,fg="white",bg="black")
button_add=Button(buttom_frame,text="+",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=add)
button_subtract=Button(buttom_frame,text="-",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=subtract)
button_multiply=Button(buttom_frame,text="*",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command= multiply)
button_divide=Button(buttom_frame,text="/",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=divide)
button_clear=Button(buttom_frame,text="Clear",font=font,padx=7,pady=5,width=11,borderwidth=2,relief="solid",command=clear,
                    bg="blue",fg="white")
buttom_Square=Button(buttom_frame,text="x^",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="solid",command=square)


#adding button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_subtract.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_multiply.grid(row=1,column=3)



button_divide.grid(row=0,column=3)
buttom_Square.grid(row=0,column=0)
button_clear.grid(row=0,column=1,columnspan=2)

button_0.grid(row=4,column=1)
button_equal.grid(row=4,column=2,columnspan=2)
button_dot.grid(row=4,column=0)

root.mainloop()
