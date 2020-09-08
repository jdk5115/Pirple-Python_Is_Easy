#tkinter

import tkinter as tk

window = tk.Tk()
window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')

lbl1 = tk.Label(window, text='yo man').pack()
lbl2 = tk.Label(window, text= "Hey dude, how are you?").pack()
    # lbl1.pack() <-- can also be done on the actual line
    # lbl2.pack() <-- can also be done on the actual line

window.mainloop()