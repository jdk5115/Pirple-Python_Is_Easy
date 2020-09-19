from tkinter import *
import time as t

global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, status, callBack, clicked, dropDown, chkbx, chkbx2, chkbx3, feelings, var, var2, var3, r, feelingslbl, name, age, chkbxlbl, sport, iceCream, iceCream2, iceCream3, chkbxlbl2, chkbxlbl3
window = Tk()
window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("400x400") #width x height

Questions = ['Hello, what should I call you?', #textbox - Done
            'How old are you?', #slider - Done
            'What is your favorite sport?', #dropdown/option menu - Done
            'Which flavor of ice cream is your favorite?', #Checkboxes - Done
            'How are you feeling today?'] #radio 

x = 0
Qcount = Questions[x]
b=0
lbl1 = Label(window,text=Qcount)
lbl1.place(x=20, y=20)
lbl1.pack(pady=10)

e = Entry(window, width=50, fg='blue')
e.pack(pady=10)


#dropdown
#This needs to be put into case 3
#btn click cycles through questions. Just need to add widgets, store values and display answers.

def btnClick():
    global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, b, status, callBack, clicked, dropDown, chkbx, var, var2, var3, chkbx2, chkbx3, feelings, r, feelingslbl, name, age, chkbxlbl, sport, iceCream, iceCream2, iceCream3, chkbxlbl2, chkbxlbl3
    if b == 0:
        e.get()
        name = e.get()
        e.pack_forget()
        print(name)
        lbl1.pack_forget()
        x+=1
        status.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        slider = Scale(window,from_=0, to=100)
        slider.pack()
        btn1.pack_forget()
        #btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
        btn1.pack()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN, pady=5 )
        status.pack()
        b += 1

    elif b ==1:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x+=1
        status.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        clicked = StringVar()
        clicked.set("Football")
        dropDown = OptionMenu(window, clicked, "Football", "Hockey", "Baseball", "Basketball")
        dropDown.pack()
        btn1.pack_forget()
        btn1.pack()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN, pady=5 )
        status.pack()
        b += 1

    elif b == 2:
        sport = clicked.get()
        dropDown.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)

        var = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        chkbx = Checkbutton(window, text="Chocolate", variable=var, onvalue="Chocolate", offvalue="")
        chkbx.deselect()
        chkbx.pack(anchor=W)
        chkbx2 = Checkbutton(window, text="Vanilla", variable=var2, onvalue="Vanilla", offvalue="")
        chkbx2.deselect()
        chkbx2.pack(anchor=W)
        chkbx3 = Checkbutton(window, text="Strawberry", variable=var3, onvalue="Strawberry", offvalue="")
        chkbx3.deselect()
        chkbx3.pack(anchor=W)



        btn1.pack_forget()
        btn1.pack()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN,pady=5 )
        status.pack()

        b += 1

    elif b == 3:
        chkbx.pack_forget()
        chkbx2.pack_forget()
        chkbx3.pack_forget()
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        btn1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)


        MODES = [
                ("Happy", "Happy"),
                ("So-So", "So-So"),
                ("Sad", "Sad", ),
                ("Angry","Angry")
        ]

        r = StringVar()
        r.set("Happy")
        


        for text, mode in MODES:
            Radiobutton(window, text=text, variable=r, value=mode).pack(anchor=W)        

        feelings = Label(window, text=r.get())   
        feelings.pack()

        newbtn = Button(window, text="Submit", command= lambda: clicked(r.get()), fg= 'black', bg='#33FFC4', padx=10)
        newbtn.pack()

        def clicked(value):
            global b, feelingslbl,lbl1, name, age, sport, chkbxlbl, feelings, hey, iceCream, iceCream2, iceCream3, chkbxlbl2, chkbxlbl3, var, var2, var3
            chkbxlbl = Label(window, text=var.get())
            chkbxlbl2 = Label(window, text=var2.get())
            chkbxlbl3 = Label(window, text=var3.get())
            iceCream = var.get() #chkbxlbl.cget('text')
            iceCream2 = var2.get() #chkbxlbl2.cget('text')
            iceCream3 = var3.get() #chkbxlbl3.cget('text')
            feelingslbl = Label(window, text=value)
            b+=1
            lbl1.pack_forget()
            lbl1 = Label(window, text="You are " + str(name) + ".\nYour age is " + str(age) + "\nYour favorite sport is " + str(sport) + ".\nYour favorite flavor of ice cream is " + str(iceCream)+ str(iceCream2)+ str(iceCream3) + ".\nAnd you are feeling " + str(feelings) + ".\nThanks for playing! Have a great day =)")
            lbl1.pack(pady=10)

        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN,pady=5 )
        status.pack()


    elif b == 4:


        btn1.pack_forget()
        status.pack_forget()


        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN,pady=5 )
        status.pack()

        b += 1
        exit()




btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
btn1.pack()

status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN, pady=5 )
status.pack()

window.mainloop()