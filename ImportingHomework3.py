from tkinter import *
import time as t

global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, status, callBack, clicked
window = Tk()
window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("400x400") #width x height

Questions = ['Hello, what should I call you?', #textbox - Done
            'How old are you?', #slider - Done
            'What is your favorite sport?', #dropdown/option menu - Done
            'How many brothers and sisters do you have?', #spinbox
            'Do you like classical music?', #yes/no buttons
            'Have you studied at University?',  #seperator
            'Which flavors of ice cream do you like?', #Checkboxes?
            'How are you feeling today?'] #radio 

x = 0
Qcount = Questions[x]
b=0
lbl1 = Label(window,text=Qcount)
lbl1.place(x=20, y=20)
lbl1.pack(pady=10)

e = Entry(window, width=50, fg='blue')
e.pack(pady=10)

status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
status.pack()
#dropdown
#This needs to be put into case 3
#btn click cycles through questions. Just need to add widgets, store values and display answers.

def btnClick():
    global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, b, status, callBack, clicked, dropDown
    if b == 0:
        e.get()
        name = e.get()
        e.pack_forget()
        print(name)
        lbl1.pack_forget()
        x+=1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        slider = Scale(window,from_=0, to=100)
        slider.pack()
        btn1.pack_forget()
        #btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
        btn1.pack()
        b += 1

    elif b ==1:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x+=1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        clicked = StringVar()
        clicked.set("Football")
        dropDown = OptionMenu(window, clicked, "Football", "Hockey", "Baseball", "Basketball")
        dropDown.pack()
        btn1.pack_forget()
        btn1.pack()
        b += 1

    elif b == 2:
        sport = clicked.get()
        dropDown.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)

        btn1.pack_forget()
        btn1.pack()

        b += 1

    elif b == 3:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()

        b += 1

    elif b == 4:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()

        b += 1

    elif b == 5:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x += 1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()

        b += 1

    elif b == 6:
        #b5 .pack_forget()
        def feel(value):
                feelings = Label(window, text=value)
                feelings.pack()

        x += 1
        status.pack_forget()
        status = Label(window, text="Question " + str(x+1) + " of " + str(len(Questions)), bd=1, relief=SUNKEN )
        status.pack()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        
        r = IntVar()
        r.set(1)
        Radiobutton(window, text="Happy", variable=r, value=1, command=lambda: feel(r.get())).pack()
        Radiobutton(window, text="So-So", variable=r, value=2, command=lambda: feel(r.get())).pack()
        Radiobutton(window, text="Sad", variable=r, value=3, command=lambda: feel(r.get())).pack()
        Radiobutton(window, text="Angry", variable=r, value=4, command=lambda: feel(r.get())).pack()    
        feelings = Label(window, text=r.get())   
        btn1.pack_forget()
        newbutton = Button(window, text="Submit", command=lambda: feel(r.get())).pack()

        b += 1

    elif b == 7:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        x += 1
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()

        b += 1



btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
btn1.pack()

window.mainloop()