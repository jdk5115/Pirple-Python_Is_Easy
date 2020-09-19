from tkinter import *
import time as t

global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, status, callBack, clicked, dropDown, chkbx, chkbx2, chkbx3, feelings, r, feelingslbl, name, age
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
    global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, b, status, callBack, clicked, dropDown, chkbx, chkbx2, chkbx3, feelings, r, feelingslbl, name, age
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
        chkbx = Checkbutton(window, text="Chocolate", variable=var, onvalue="Chocolate", offvalue="")
        chkbx.deselect()
        chkbx.pack(anchor=W)
        chkbx2 = Checkbutton(window, text="Vanilla", variable=var, onvalue="Vanilla", offvalue="")
        chkbx2.deselect()
        chkbx2.pack(anchor=W)
        chkbx3 = Checkbutton(window, text="Strawberry", variable=var, onvalue="Strawberry", offvalue="")
        chkbx3.deselect()
        chkbx3.pack(anchor=W)
        chkbxlbl = Label(window, text=var.get()).pack()

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
            global b, feelingslbl,lbl1, name, age

            feelingslbl = Label(window, text=value)
            b+=1
            lbl1.pack_forget()
            lbl1 = Label(window, text="You are" + str(name) + "your age is" + str(age))
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