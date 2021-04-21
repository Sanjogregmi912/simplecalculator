from tkinter import *
root=Tk()
#font for the calculator
font="vandana",22
#title of the window
root.title("simple calculator")
#size of the calculator
#root.geometry('150x300')
#heading
heading_label=Label(root,text="My calculator",font="vandana")
heading_label.grid(row=0,column=0,columnspan=2)
#entry box
entry=Entry(root,width=35,borderwidth=5,justify=CENTER)
entry.grid(row=1,column=0,columnspan=3)
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
        entry.insert(0,f_num / float(secondnumber))






#adding buttons
button_1=Button(root,text=1,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(1))
button_2=Button(root,text=2,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(2))
button_3=Button(root,text=3,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(3))
button_4=Button(root,text=4,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(4))
button_5=Button(root,text=5,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(5))
button_6=Button(root,text=6,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(6))
button_7=Button(root,text=7,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(7))
button_8=Button(root,text=8,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(8))
button_9=Button(root,text=9,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(9))
button_0=Button(root,text=0,font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                ,activebackground="red",activeforeground="white",command=lambda :click_button(0))
button_dot=Button(root,text=".",font=font,padx=5,pady=5,width=5,borderwidth=2
                  ,activebackground="purple",activeforeground="white",command=lambda :click_button("."))
button_equal=Button(root,text="=",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                    ,activebackground="blue",activeforeground="white",command=Equal)
button_add=Button(root,text="+",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                  ,activebackground="green",activeforeground="white",command=add)
button_subtract=Button(root,text="-",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                       ,activebackground="green",activeforeground="white",command=subtract)
button_multiply=Button(root,text="*",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                       ,activebackground="green",activeforeground="white",command= multiply)
button_divide=Button(root,text="/",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                     ,activebackground="green",activeforeground="white",command=divide)
button_clear=Button(root,text="Clear",font=font,padx=5,pady=5,width=5,borderwidth=2,relief="ridge"
                     ,activebackground="black",activeforeground="white",command=clear)


#adding button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_subtract.grid(row=4,column=3)

button_7.grid(row=5,column=0)
button_8.grid(row=5,column=1)
button_9.grid(row=5,column=2)
button_multiply.grid(row=5,column=3)

button_0.grid(row=6,column=1)
button_divide.grid(row=6,column=3)

button_clear.grid(row=7,column=1)
button_equal.grid(row=7,column=2)
button_dot.grid(row=7,column=0)

root.mainloop()
