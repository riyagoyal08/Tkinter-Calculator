from tkinter import *

root=Tk()


def show():
        
    pass


root.geometry("500x500")


e1=Entry(root)
e1.grid(row=0,columnspan=4)



b1=Button(root,text='1',command=show(),height=2,width=4)
b2=Button(root,text='2',command=show(),height=2,width=4)
b3=Button(root,text='3',command=show(),height=2,width=4)
b4=Button(root,text='4',command=show(),height=2,width=4)
b5=Button(root,text='5',command=show(),height=2,width=4)
b6=Button(root,text='6',command=show(),height=2,width=4)
b7=Button(root,text='7',command=show(),height=2,width=4)
b8=Button(root,text='8',command=show(),height=2,width=4)
b9=Button(root,text='9',command=show(),height=2,width=4)
b0=Button(root,text='0',command=show(),height=2,width=4)
bc=Button(root,text='C',command=show(),height=2,width=4)
bplus=Button(root,text='+',command=show(),height=2,width=4)
bminus=Button(root,text='-',command=show(),height=2,width=4)
bbracketl=Button(root,text='(',command=show(),height=2,width=4)
bbracketr=Button(root,text=')',command=show(),height=2,width=4)
bdot=Button(root,text='.',command=show(),height=2,width=4)
bequal=Button(root,text='=',command=show(),height=2,width=4)
bmod=Button(root,text='%',command=show(),height=2,width=4)
bmul=Button(root,text='X',command=show(),height=2,width=4)
bdiv=Button(root,text='/',command=show(),height=2,width=4)
bbackspace=Button(root,text='<',command=show(),height=2,width=4)


bc.grid(row=1,column=0)
bbackspace.grid(row=1,column=1)
bbracketl.grid(row=1,column=2)
bbracketr.grid(row=1,column=3)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
bplus.grid(row=2,column=3)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
bminus.grid(row=3,column=3)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
bmul.grid(row=4,column=3)
bdot.grid(row=5,column=0)
b0.grid(row=5,column=1)
bequal.grid(row=5,column=2)
bdiv.grid(row=5,column=3)

root.mainloop()