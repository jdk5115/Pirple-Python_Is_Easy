#tkinter
import tkinter as tk

window = tk.Tk()

window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("500x500") #width x height

lbl1 = tk.Label(window, text='Hello! Welcome to the program.  What should I call you?').grid(row=0,column=1)

e = tk.Entry(window, width=50, fg='black')
e.grid(row=5,column=1)

def func1():
    lbl1 = tk.Label(window, text='Welcome to the program ' + e.get() ).grid(row=0,column=1)

btn1 = tk.Button(window, text="submit", command= func1, fg= 'black', bg='#33FFC4', padx=40, pady=20).grid(row=20,column=1)



window.mainloop()
