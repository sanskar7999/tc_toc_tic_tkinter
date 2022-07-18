
from tkinter import *
from tkinter import messagebox as tmsg


root = Tk()
root.geometry("300x300")
root.resizable(False,False)
root.title("tic-toc-tic")

click = True
count = 0

b1_btn = StringVar()
b2_btn = StringVar()
b3_btn = StringVar()
b4_btn = StringVar()
b5_btn = StringVar()
b6_btn = StringVar()
b7_btn = StringVar()
b8_btn = StringVar()
b9_btn = StringVar()

frist = 'O'
second = 'X'



def play():
    b1 = Button(root, font=(' ' , 25 ,  'bold') , width=3 ,textvariable=b1_btn , command = lambda:bttn1(num=1 ,r=0 ,c=0) )
    b1.grid(row=0,column=0)
    b2 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b2_btn  , command =  lambda:bttn1(num=2 ,r=0 ,c=1))
    b2.grid(row=0,column=1)
    b3= Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b3_btn  , command =  lambda:bttn1(num=3 ,r=0 ,c=2))
    b3.grid(row=0,column=2)
    b4 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b4_btn  , command =  lambda:bttn1(num=4 ,r=1 ,c=0))
    b4.grid(row=1,column=0)
    b5 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b5_btn  , command =  lambda:bttn1(num=5 ,r=1 ,c=1))
    b5.grid(row=1,column=1)
    b6 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b6_btn  , command =  lambda:bttn1(num=6 ,r=1 ,c=2))
    b6.grid(row=1,column=2)
    b7 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b7_btn  , command =  lambda:bttn1(num=7 ,r=2 ,c=0))
    b7.grid(row=2,column=0)
    b8 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b8_btn  , command =  lambda:bttn1(num=8 ,r=2 ,c=1))
    b8.grid(row=2,column=1)
    b9 = Button(root, font=(' ' , 25 ,  'bold') , width=3,textvariable=b9_btn  , command =  lambda:bttn1(num=9 ,r=2 ,c=2 ))
    b9.grid(row=2,column=2)


def bttn1(num , r ,c):
    global click, count
    if click == True:
        frist1 = Label(root, text=frist)
        frist1.grid(row=r ,column=c)
        if num == 1:
                b1_btn.set(" O ")
        if num == 2:
                b2_btn.set(" O ")
        if num == 3:
                b3_btn.set(" O ")
        if num == 4:
                b4_btn.set(" O ")
        if num == 5:
                b5_btn.set(" O ")
        if num == 6:
                b6_btn.set(" O ")
        if num == 7:
                b7_btn.set(" O ")
        if num == 8:
                b8_btn.set(" O ")
        if num == 9:
                b9_btn.set(" O ")

        count+=1
        click = False
        checkwin()
        
    else:
        second1 = Label(root, text=second)
        second1.grid(row=0 ,column=0)
        if num == 1:
                b1_btn.set(" X")
        if num == 2:
                b2_btn.set(" X")
        if num == 3:
                b3_btn.set(" X")
        if num == 4:
                b4_btn.set(" X")
        if num == 5:
                b5_btn.set(" X")
        if num == 6:
                b6_btn.set(" X")
        if num == 7:
                b7_btn.set(" X")
        if num == 8:
                b8_btn.set(" X")
        if num == 9:
                b9_btn.set(" X")

        count+=1
        click = True
        checkwin()

def checkwin():
    global click , count
    if (b1_btn.get() == "X" and b2_btn.get() ==" X" and b3_btn.get() ==" X" or
        b4_btn.get() == "X" and b5_btn.get() ==" X" and b6_btn.get() ==" X" or
        b7_btn.get() == "X" and b8_btn.get() ==" X" and b9_btn.get() ==" X" or
        b1_btn.get() == "X" and b5_btn.get() ==" X" and b9_btn.get() ==" X" or
        b2_btn.get() == "X" and b5_btn.get() ==" X" and b8_btn.get() ==" X" or
        b3_btn.get() == "X" and b6_btn.get() ==" X" and b9_btn.get() ==" X" or
        b3_btn.get() == "X" and b5_btn.get() ==" X" and b7_btn.get() ==" X" or
        b1_btn.get() == "X" and b4_btn.get() ==" X" and b7_btn.get() ==" X" ):
        tmsg.showinfo("Winner" , " congresulation X  is winer")
        click = True

        count = 0
        clear()
        play()

    elif(b1_btn.get() == "O" and b2_btn.get() ==" O" and b3_btn.get() ==" O" or
        b4_btn.get() == "O" and b5_btn.get() ==" O" and b6_btn.get() ==" O" or
        b7_btn.get() == "O" and b8_btn.get() ==" O" and b9_btn.get() ==" O" or
        b1_btn.get() == "O" and b5_btn.get() ==" O" and b9_btn.get() ==" O" or
        b2_btn.get() == "O" and b5_btn.get() ==" O" and b8_btn.get() ==" O" or
        b3_btn.get() == "O" and b6_btn.get() ==" O" and b9_btn.get() ==" O" or
        b3_btn.get() == "O" and b5_btn.get() ==" O" and b7_btn.get() ==" O" or
        b1_btn.get() == "O" and b4_btn.get() ==" O" and b7_btn.get() ==" O" ):


        tmsg.showinfo("Winner" , " congresulation O  is winer")
        count = 0
        clear
        play()
    elif(count == 9):
        tmsg.showinfo("Winner" , "Tir ")
        click = True
        count = 0
        clear()
        play()

def clear():
    b1_btn.set("")
    b2_btn.set("")
    b3_btn.set("")
    b4_btn.set("")
    b5_btn.set("")
    b6_btn.set("")
    b7_btn.set("")
    b8_btn.set("")
    b9_btn.set("")

    
play()           



root.mainloop()
