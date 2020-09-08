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

def lbl1Erase():
    lbl1.pack_forget()
    func1()

def func1():
    lbl1 = tk.Label(window, text='Welcome to the program ' + e.get())
    lbl1.pack(pady=20)
    e.delete(0, 'end')
    e.destroy()
    btn1.pack_forget()

btn1 = tk.Button(window, text="submit", command= lbl1Erase, fg= 'black', bg='#33FFC4', padx=40, pady=20)
btn1.pack()


window.mainloop()
