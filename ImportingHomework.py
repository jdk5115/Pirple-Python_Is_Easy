import turtle as t

t.speed('fastest')
t.color('gold')
t.begin_fill()
sq = 5
t. pensize(2)

#Draw a pyramid
for i in range (20):
    t.forward(sq)
    t.right(90)
    t.forward(sq)
    t.right(90)
    t.forward(sq)
    t.right(90)
    t.forward(sq)
    t.right(90)
    sq += 5

t.color('white')
t.goto(-200,200)
t.pensize(2)
t.color("gold")
t.begin_fill()
t.circle(50)
t.end_fill()



t.mainloop()