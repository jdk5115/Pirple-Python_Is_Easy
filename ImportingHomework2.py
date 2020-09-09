#tkinter
import tkinter as tk
import time as t

global lbl1, e, slider, btn1, x, Qcount, Questions, window, btn1 #, Bclicks, ButtonClicks, b
x=0

window = tk.Tk()
window.title("my box gui")
window.iconbitmap('target_goal_icon_152113.ico')
window.geometry("400x400") #width x height

Questions = ['Hello, what should I call you1?','How old are you2?', 'What is your favorite sport?3', 
            'How many brothers and sisters do you have4?',
            'Do you like classical music5?', 'Have you studied at University6?',  
            'Do you like ice cream7?', 'How are you feeling today8?']
x = 0
Qcount = Questions[x]

lbl1 = tk.Label(window, bg='red',text=Qcount)
lbl1.pack(fill=tk.X)

e = tk.Entry(window, width=50, fg='blue')
e.pack(pady=10)

# btn1 = tk.Button(window, text="Submit", command= btnClick() , fg= 'black', bg='#33FFC4', padx=10, pady=0)
# btn1.pack()


lbl1.pack_forget()
lbl1 = tk.Label(window, text=Questions[x])
lbl1.pack(pady=10)

# btn1.pack_forget()
# btn1 = tk.Button(window, text="Submit", command= btnClick() , fg= 'black', bg='#33FFC4', padx=40, pady=20)
# btn1.pack()

slider = tk.Scale(window,from_=0, to=100)
slider.pack()

window.mainloop()

#status = tk.Label(window, text= "Question 1" of 8")





    # click1()
    # b+=1
    # btn1 = tk.Button(window, text="Submit", command= Bclicks, fg= 'black', bg='#33FFC4', padx=40, pady=20)
    # btn1.pack()

# def lbl1Erase():
#     lbl1.pack_forget()
#     click1()

# def click1():
#     global name
#     global lbl1
#     global btn1
#     global x
#     global Qcount
#     lbl1 = tk.Label(window, text='Welcome to the program ' + e.get() +"\n" + Qcount)
#     lbl1.pack(pady=20)
#     x += 1
#     btnClick()



# def click2():
#     global lbl1
#     global age
#     lbl1.pack_forget()
#     lbl1 = tk.Label(window, text=Qcount)
#     lbl1.pack(pady=20)

#     if age < 18:
#         print("Sorry, you're not old enough to use this program. Please try again after you've turned 18.")
#         exit()
#     else:
#         slider.pack_forget()
#         btn1.pack_forget()
#         lbl1.pack_forget()
#         lbl1 = tk.Label(window, text="Good to see that you are old enough.  Let's get started")
#         lbl1.pack(pady=20)
#         btnClick()



#window.mainloop()
