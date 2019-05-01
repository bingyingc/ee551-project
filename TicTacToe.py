from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x250")

lable1=Label(window,text="Tic-Tac-Toe",font=('Helvetica','15'))
lable1.grid(row=0,column=0)
turn=1

def clicked1():
    global turn
    if button1["text"] =="" :
        if turn == 1 :
            turn = 2
            button1["text"]="X"
        elif turn ==2 :
            turn = 1
            button1["text"]="O"
        check()

def clicked2():
    global turn
    if button2["text"] =="" :
        if turn == 1 :
            turn = 2
            button2["text"]="X"
        elif turn ==2 :
            turn = 1
            button2["text"]="O"
        check()

def clicked3():
    global turn
    if button3["text"] =="" :
        if turn == 1 :
            turn = 2
            button3["text"]="X"
        elif turn ==2 :
            turn = 1
            button3["text"]="O"
        check()

def clicked4():
    global turn
    if button4["text"] =="" :
        if turn == 1 :
            turn = 2
            button4["text"]="X"
        elif turn ==2 :
            turn = 1
            button4["text"]="O"
        check()


def clicked5():
    global turn
    if button5["text"] =="" :
        if turn == 1 :
            turn = 2
            button5["text"]="X"
        elif turn ==2 :
            turn = 1
            button5["text"]="O"
        check()

def clicked6():
    global turn
    if button6["text"] =="" :
        if turn == 1 :
            turn = 2
            button6["text"]="X"
        elif turn ==2 :
            turn = 1
            button6["text"]="O"
        check()

def clicked7():
    global turn
    if button7["text"] =="" :
        if turn == 1 :
            turn = 2
            button7["text"]="X"
        elif turn ==2 :
            turn = 1
            button7["text"]="O"
        check()

def clicked8():
    global turn
    if button8["text"] =="" :
        if turn == 1 :
            turn = 2
            button8["text"]="X"
        elif turn ==2 :
            turn = 1
            button8["text"]="O"
        check()

def clicked9():
    global turn
    if button9["text"] =="" :
        if turn == 1 :
            turn = 2
            button9["text"]="X"
        elif turn ==2 :
            turn = 1
            button9["text"]="O"
        check()

flag=0
def check():
    b1 = button1["text"]
    b2 = button2["text"]
    b3 = button3["text"]
    b4 = button4["text"]
    b5 = button5["text"]
    b6 = button6["text"]
    b7 = button7["text"]
    b8 = button8["text"]
    b9 = button9["text"]
    global  flag
    flag+=1
    if b1==b2==b3 and b1!="":   #across the top
        win(button1["text"])
    if b4==b5==b6 and b4!="":   #across the middle
        win(button4["text"])
    if b7==b8==b9 and b7!="":   #across the bottom
        win(button7["text"])
    if b1==b4==b7 and b1!="":   #down the left side
        win(button1["text"])
    if b2==b5==b8 and b2!="":   #down the middle side
        win(button1["text"])
    if b3==b6==b9 and b3!="":   #down the right side
        win(button1["text"])
    if b1==b5==b9 and b3!="":   # diagonal
        win(button1["text"])
    if b7==b5==b3 and b3!="":   # diagonal
        win(button7["text"])
    if flag==9:
        messagebox.showinfo("Tie","Match Tied")
        window.destroy()
        
def win(player):
    ans = "player "+player+" wins"
    messagebox.showinfo("Congratulations",ans)
    window.destroy()

button1= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked1
)
button1.grid(row=1,column=1)

button2= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked2
)
button2.grid(row=2,column=1)

button3= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked3
)
button3.grid(row=3,column=1)

button4= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked4
)
button4.grid(row=1,column=2)

button5= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked5
)
button5.grid(row=2,column=2)

button6= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked6
)
button6.grid(row=3,column=2)

button7= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked7
)
button7.grid(row=1,column=3)

button8= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked8
)
button8.grid(row=2,column=3)

button9= Button(
    window,
    text="",
    bg="gray",
    fg="black",
    width=3,
    height=1,
    font=('Helvetica','20'),
    command=clicked9
)
button9.grid(row=3,column=3)

window.mainloop()
