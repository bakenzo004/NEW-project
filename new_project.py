import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.messagebox import showwarning,showinfo
from tkinter import colorchooser

COLOR = "orange"
def colorchoose():
    global COLOR
    rgb,hx = colorchooser.askcolor()
    COLOR = hx 
    frame3.config(background=COLOR)
    frame2.config(background=COLOR)
    frame1.config(background=COLOR)
    date_lb.config(background=COLOR)
    discr_lb.config(background=COLOR)
    date_lb.config(background=COLOR)
    amount_lb.config(background=COLOR)
    pay_lb.config(background=COLOR)
    mode_lb.config(background=COLOR)
    lb1.config(background=COLOR)
    sum_lb.config(background=COLOR)



win = tk.Tk()
win.title("Проектная работа")
win.geometry("1200x700")
gtr = PhotoImage(file="C:/Users/Baubek Tolepbergenov/Desktop/gtr.png")

# style1 = ttk.Style()
# style1.configure("frame_st",font="helvetica 14",padding=10,backgraund="orange")

frame3 = tk.Frame(win,borderwidth=5,relief="groove",background="Orange")
frame3.pack(side=TOP,fill=X)
frame1 = tk.Frame(win,borderwidth=5,background="Orange")
frame1.pack(side=LEFT,fill=Y)
frame2 = tk.Frame(win,background="orange")
frame2.pack(side=RIGHT,fill=BOTH)

variable = StringVar()
entry_cal = DateEntry(frame1,date_pattern="dd/mm/YYYY",textvarriable = variable)

date_lb = tk.Label(frame1,text="Date:",font=("Arial",16),padx=10,background="orange")
date_lb.grid(column=0,row=0)
entry_cal.grid(column=1,row=0)

discr_lb = tk.Label(frame1,text="Discription:",font=("Arial",16),padx=10,background="orange")
discr_lb.grid(column=0,row=3)

discr_entry = ttk.Entry(frame1)
discr_entry.grid(column=0,row=4,columnspan=2,sticky="we",pady=10)

amount_lb = ttk.Label(frame1,text="Amount:",font=("Arial",16),background="orange")
amount_lb.grid(column=0,row=5,pady=10)
amount_entry = ttk.Entry(frame1)
amount_entry.grid(column=1,row=5,pady=10)

pay_lb = ttk.Label(frame1,text="Payee:",font=("Arial",16),padding=10,background="orange")
pay_lb.grid(column=0,row=6)

pay_entry = ttk.Entry(frame1)
pay_entry.grid(column=0,row=7,columnspan=2,sticky="we")

mode_lb = ttk.Label(frame1,text="Mode of pay:",font=("Ariel",16),padding=10,background="orange")
mode_lb.grid(column=0,row=8)

list_box = ["Cash","Kaspi","Halyk","KaspiRED","Kredit"]
list_box_var = StringVar(value=list_box[1])

mode_box = ttk.Combobox(frame1,textvariable=list_box_var,values=list_box,font=("Arial",14),width=7)
mode_box.grid(column=1,row=8,pady=10)

column = ("ID","Date","Payee","Discription","Amount","Mode of payment")
tree = ttk.Treeview(frame2,columns=column,show="headings")
tree.pack()

tree.heading('ID',text="№",anchor=tk.CENTER)
tree.heading('Date',text="DATE",anchor=tk.CENTER)
tree.heading('Payee',text="Payee",anchor=tk.CENTER)
tree.heading('Discription',text="Discription",anchor=tk.CENTER)
tree.heading('Amount',text="Amount",anchor=tk.CENTER)
tree.heading('Mode of payment',text="Mode of payment",anchor=tk.CENTER)

tree.column("#0",width=0,stretch=tk.NO)
tree.column("#1",width=50,stretch=tk.NO)
tree.column("#2",width=95,stretch=tk.NO)
tree.column("#3",width=150,stretch=tk.NO)
tree.column("#4",width=325,stretch=tk.NO)
tree.column("#5",width=135,stretch=tk.NO)

lb1 = tk.Label(frame3,text="AKWA KAIDA?",font=("Ariel",24,"bold"),justify=LEFT,background="Orange",foreground="BLACK")
lb1.pack()

def sum_money():
    sum = 0
    for i in tree.get_children():
        sum += tree.item(i)["values"][4]
        sum_lb.config(text=f"Потрачено: {sum} tg")
    # showinfo(title="SUM",message=sum)

sum_btn = tk.Button(frame2,text="SUM:",font=("helvetica 14",16),pady=10,background="black",foreground="white",relief="groove",width=10,command=sum_money,padx=10)
sum_btn.pack(side=TOP)
sum_lb = ttk.Label(frame2,text="",font=("Arial",16),background="orange")
sum_lb.pack(side=TOP)

def save():
    with open ("new,project.txt",mode="w") as file:
        for i in tree.get_children():
            file.write(str(*tree.item(i)["values"]))

mmenu = tk.Menu()
mmenu.add_cascade(label="Change color",command=colorchoose)
mmenu.add_cascade(label="SAVE",command=save)
mmenu.add_cascade(label="Exit",command=lambda:win.destroy())



id = 0
def add():
    global id
    id += 1
    if not pay_entry == "" or discr_entry == "" or amount_entry == "":
        tree.insert('',tk.END,values=(id,entry_cal.get(),pay_entry.get(),discr_entry.get(),amount_entry.get(),mode_box.get()))
    else:
        showwarning(title="WARNING!!!",message="Empty entryes!!!")
    pay_entry.delete(0,END)
    discr_entry.delete(0,END)
    amount_entry.delete(0,END)

add_btn = tk.Button(frame1,text="ADD Expense",font=("helvetica 14",16),pady=10,background="black",foreground="white",relief="groove",width=10,command=add)
add_btn.grid(column=0,row=10,columnspan=2,sticky="we",pady=10)

def edit():
    tree_selected = tree.selection()
    if tree_selected:
        column = tree.item(tree_selected,"values")
    
    entry_cal.delete(0,END)
    entry_cal.insert(0,column[1])

    pay_entry.delete(0,END)
    pay_entry.insert(0,column[2])

    discr_entry.delete(0,END)
    discr_entry.insert(0,column[3])

    amount_entry.delete(0,END)
    amount_entry.insert(0,column[4])

    mode_box.delete(0,END)
    mode_box.insert(0,column[5])

    tree.delete(tree.focus())

btn_edit = tk.Button(frame1,text="EDIT",font=("Arial",16),pady=10,background="black",foreground="white",command=edit)
btn_edit.grid(column=0,row=11,columnspan=2,sticky="we",pady=10)

def delet():
    tree.delete(tree.focus())

btn_del = tk.Button(frame1,text="DELETE",font=("Arial",16),pady=10,background="black",foreground="white",command=delet)
btn_del.grid(column=0,row=12,columnspan=2,sticky="we",pady=10)

def delall():
    tree.delete(*tree.get_children())
btn_delall = tk.Button(frame1,text="DELETE ALL",font=("Arial",16),pady=10,background="black",foreground="white",command=delall)
btn_delall.grid(column=0,row=13,columnspan=2,sticky="we",pady=10)


win.config(menu=mmenu)
win.mainloop()
