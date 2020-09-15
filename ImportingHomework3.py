from tkinter import *
import time as t

global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1
window = Tk()
window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("400x400") #width x height

Questions = ['Hello, what should I call you?',
            'How old are you?', 
            'What is your favorite sport?', 
            'How many brothers and sisters do you have?',
            'Do you like classical music?', 
            'Have you studied at University?',  
            'Do you like ice cream?', 
            'How are you feeling today?']

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

clicked = StringVar()
clicked.set("Football")
dropDown = OptionMenu(window, clicked, "Football", "Hockey", "Baseball", "Basketball")
dropDown.pack()


def btnClick():
    global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1, b
    if b == 0:
        e.get()
        name = e.get()
        e.pack_forget()
        print(name)
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        slider = Scale(window,from_=0, to=100)
        slider.pack()
        btn1.pack_forget()
        #btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
        btn1.pack()
        x += 1
        b += 1

    elif b ==1:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 2:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 3:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 4:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 5:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 6:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1

    elif b == 7:
        age = slider.get()
        slider.pack_forget()
        lbl1.pack_forget()
        lbl1 = Label(window, text=Questions[x])
        lbl1.pack(pady=10)
        '''this is where the next widget goes'''
        btn1.pack_forget()
        btn1.pack()
        x += 1
        b += 1



btn1 = Button(window, text="Submit", command= lambda: btnClick() , fg= 'black', bg='#33FFC4', padx=10)
btn1.pack()

window.mainloop()