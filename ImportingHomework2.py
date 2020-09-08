#tkinter
import tkinter as tk

window = tk.Tk()

window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("500x500") #width x height

lbl1 = tk.Label(window, text='Hello! Welcome to the program.  What should I call you?')
lbl1.pack(pady=10)

e = tk.Entry(window, width=50, fg='black')
e.pack(pady=10)

slider = tk.Scale(window,from_=0, to=100, orient=HORIZONTAL)


def lbl1Erase():
    lbl1.pack_forget()
    click1()

def click1():
    global name
    name = e.get()
    lbl1 = tk.Label(window, text='Welcome to the program ' + e.get() +"\nHow old are you?")
    lbl1.pack(pady=20)
    e.delete(0, 'end')
    e.destroy()
    btn1.pack_forget()
    slider.pack()
    btn2.pack()

def click2():
    global age
    age = slider.get()

    
btn1 = tk.Button(window, text="Submit Name", command= lbl1Erase, fg= 'black', bg='#33FFC4', padx=40, pady=20)
btn1.pack()

btn2 = tk.Button(window, text="Submit Age", command= click2, fg= 'black', bg='#33FFC4', padx=40, pady=20)

window.mainloop()
