#tkinter
import tkinter as tk
import time as t
window = tk.Tk()

window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("500x500") #width x height

Questions = ['How old are you?', 'What is your favorite sport?', 
            'How many brothers and sisters do you have?',
            'Do you like classical music?', 'Have you studied at University?',  
            'Do you like ice cream?', 'How are you feeling today?']

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

    name = e.get()
    lbl1 = tk.Label(window, text='Welcome to the program ' + e.get() +"\n" + Questions[0])
    lbl1.pack(pady=20)
    e.delete(0, 'end')
    e.destroy()
    btn1.pack_forget()
    slider.pack()
    btn1 = tk.Button(window, text="Submit", command= lbl1Erase, fg= 'black', bg='#33FFC4', padx=40, pady=20)
    btn1.pack()



def click2():
    global lbl1
    lbl1.pack_forget()
    lbl1 = tk.Label(window, text='label2 to the program ' +"\nHow old are you?")
    lbl1.pack(pady=20)
    global age
    age = slider.get()
    if age < 18:
        print("Sorry, you're not old enough to use this program. Please try again after you've turned 18.")
        exit()
    else:
        slider.pack_forget()
        btn1.pack_forget()
        lbl1.pack_forget()
        global lbl2
        lbl2 = tk.Label(window, text="Good to see that you are old enough.  Let's get started")
        lbl2.pack(pady=20)
        btn1.pack()

def click3():
    x = 'cool'


btn1 = tk.Button(window, text="Submit", command= lbl1Erase, fg= 'black', bg='#33FFC4', padx=40, pady=20)
btn1.pack()

window.mainloop()
