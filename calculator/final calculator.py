from tkinter import *
root=Tk()
root.title("calculator")
#font used in the calculator
font="vandana",22,"bold"


#for geometry
root.geometry("400x600")

#for heading
toplabel=Label(root,text=" Simple Calculator",font=font)
toplabel.pack(side=TOP)

#for dispaly
e1 = Entry(root,font=font,justify=CENTER)
e1.pack(side=TOP,pady=10,fill=X,padx=10)

# for buttoms
buttomframe=Frame(root)
buttomframe.pack(side=TOP)
# buttom in frame
variable=1
for i in range(0,3):
    for j in range(0,3):
        buttom=Button(buttomframe,text=str(variable),font=font,relief="solid")
        buttom.grid(row=i,column=j,padx=5,pady=5)
        variable=variable+1
buttom_zero=Button(buttomframe,text="0",font=font,width=2,relief="solid")
buttom_zero.grid(row=3,column=0,padx=5,pady=5)

buttom_dot=Button(buttomframe,text=".",font=font,width=2,relief="solid")
buttom_dot.grid(row=3,column=1,padx=5,pady=5)

buttom_equal=Button(buttomframe,text="=",font=font,width=2,relief="solid")
buttom_equal.grid(row=3,column=2,padx=5,pady=5)
buttom_clear=Button(buttomframe,text="clear",font=font,width=5,relief="solid")
buttom_clear.grid(row=0,column=3)
buttom_divide=Button(buttomframe,text="/",font=font,w)



root.mainloop()
