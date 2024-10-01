from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_eggpuff.delete(0,END)
    entry_donut.delete(0,END)
    entry_biscut.delete(0,END)
    entry_rose.delete(0,END)
    entry_badam.delete(0,END)
    entry_cake.delete(0,END)
    entry_vegpuff.delete(0,END)

def Total():
    try:a1=int(eggpuff.get())
    except: a1=0

    try:a2=int(donut.get())
    except: a2=0

    try:a3=int(biscut.get())
    except: a3=0

    try:a4=int(rose.get())
    except: a4=0

    try:a5=int(badam.get())
    except: a5=0

    try:a6=int(cake.get())
    except: a6=0

    try:a7=int(vegpuff.get())
    except: a7=0


    #define cost of each time per quantity
    c1=5*a1
    c2=5*a2
    c3=10*a3
    c4=5*a4
    c5=5*a5
    c6=5*a6
    c7=5*a7


    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)



Label(text="Bill Management",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menu Card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=315,height=370)
f.place(x=10,y=118) 

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Egg Puff........Rs.5/Piece",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Donut........Rs.5/Piece",fg="black",bg="lightgreen").place(x=10,y=120)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Biscuts........Rs.10/Packet",fg="black",bg="lightgreen").place(x=10,y=160)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Rose Milk......Rs.5/Cup",fg="black",bg="lightgreen").place(x=10,y=200)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Badam Juice....Rs.5/Cup",fg="black",bg="lightgreen").place(x=10,y=240)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cake........Rs.5/Piece",fg="black",bg="lightgreen").place(x=10,y=280)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Veg Puff........Rs.5/Piece",fg="black",bg="lightgreen").place(x=10,y=320)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)  

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)

#Entry Work
f1=Frame(root,bd=5,height=370,width=300, relief=RAISED)
f1.pack()

eggpuff=StringVar()
donut=StringVar()

biscut=StringVar()
rose=StringVar()

badam=StringVar()
cake=StringVar()

vegpuff=StringVar()
Total_bill=StringVar()

#Label
lbl_eggpuff=Label(f1,font=("arial",20,'bold'),text="Egg Puff",width=12,fg="blue4")
lbl_donut=Label(f1,font=("arial",20,'bold'),text="Donut",width=12,fg="blue4")

lbl_biscut=Label(f1,font=("arial",20,'bold'),text="Biscut",width=12,fg="blue4")
lbl_rose=Label(f1,font=("arial",20,'bold'),text="Rose Milk",width=12,fg="blue4")

lbl_badam=Label(f1,font=("arial",20,'bold'),text="Badam Milk",width=12,fg="blue4")
lbl_cake=Label(f1,font=("arial",20,'bold'),text="Cake",width=12,fg="blue4")

lbl_vegpuff=Label(f1,font=("arial",20,'bold'),text="Veg Puff",width=12,fg="blue4")

lbl_eggpuff.grid(row=1,column=0)
lbl_donut.grid(row=2,column=0)

lbl_biscut.grid(row=3,column=0)
lbl_rose.grid(row=4,column=0)

lbl_badam.grid(row=5,column=0)
lbl_cake.grid(row=6,column=0)

lbl_vegpuff.grid(row=7,column=0)

#Entry
entry_eggpuff=Entry(f1,font=("arial",20,'bold'),textvariable=eggpuff,bd=6,width=8,bg="lightpink")
entry_donut=Entry(f1,font=("arial",20,'bold'),textvariable=donut,bd=6,width=8,bg="lightpink")

entry_biscut=Entry(f1,font=("arial",20,'bold'),textvariable=biscut,bd=6,width=8,bg="lightpink")
entry_rose=Entry(f1,font=("arial",20,'bold'),textvariable=rose,bd=6,width=8,bg="lightpink")

entry_badam=Entry(f1,font=("arial",20,'bold'),textvariable=badam,bd=6,width=8,bg="lightpink")
entry_cake=Entry(f1,font=("arial",20,'bold'),textvariable=cake,bd=6,width=8,bg="lightpink")

entry_vegpuff=Entry(f1,font=("arial",20,'bold'),textvariable=vegpuff,bd=6,width=8,bg="lightpink")
entry_eggpuff.grid(row=1,column=1)

entry_donut.grid(row=2,column=1)
entry_biscut.grid(row=3,column=1)

entry_rose.grid(row=4,column=1)
entry_badam.grid(row=5,column=1)

entry_cake.grid(row=6,column=1)
entry_vegpuff.grid(row=7,column=1)

#buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
