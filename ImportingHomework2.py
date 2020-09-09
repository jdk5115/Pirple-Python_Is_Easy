#tkinter
import tkinter as tk
import time as t
window = tk.Tk()

window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("500x500") #width x height

Questions = ['Hello, what should I call you1?','How old are you2?', 'What is your favorite sport?3', 
            'How many brothers and sisters do you have4?',
            'Do you like classical music5?', 'Have you studied at University6?',  
            'Do you like ice cream7?', 'How are you feeling today8?']

x = 0
Qcount = Questions[x]

global lbl1, e, slider, btn1
lbl1 = tk.Label(window, text='Hello! What should I call you?')
lbl1.pack(pady=10)

e = tk.Entry(window, width=50, fg='black')
e.pack(pady=10)

slider = tk.Scale(window,from_=0, to=100)

#status = tk.Label(window, text= "Question 1" of 8")


def lbl1Erase():
    lbl1.pack_forget()
    click1()

def click1():
    global name
    global lbl1
    global btn1
    global x
    global Qcount

    name = e.get()
    lbl1 = tk.Label(window, text='Welcome to the program ' + e.get() +"\n" + Qcount)
    lbl1.pack(pady=20)
    x += 1
    e.delete(0, 'end')
    e.destroy()
    btn1.pack_forget()
    slider.pack()
    btn1 = tk.Button(window, text="Submit", command= click2, fg= 'black', bg='#33FFC4', padx=40, pady=20)
    btn1.pack()



def click2():
    global lbl1
    global age
    lbl1.pack_forget()
    lbl1 = tk.Label(window, text=Qcount)
    lbl1.pack(pady=20)
    age = slider.get()
    if age < 18:
        print("Sorry, you're not old enough to use this program. Please try again after you've turned 18.")
        exit()
    else:
        slider.pack_forget()
        btn1.pack_forget()
        lbl1.pack_forget()
        lbl1 = tk.Label(window, text="Good to see that you are old enough.  Let's get started")
        lbl1.pack(pady=20)
        btn1 = tk.Button(window, text="Submit", command= click3, fg= 'black', bg='#33FFC4', padx=40, pady=20)
        btn1.pack()

def click3():
    x = 'cool'


btn1 = tk.Button(window, text="Submit", command= lbl1Erase, fg= 'black', bg='#33FFC4', padx=40, pady=20)
btn1.pack()

window.mainloop()
