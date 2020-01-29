from turtle import *
import time
wn=Screen()
wn.bgcolor('Black')
wn.title('MyTimer')

pen=Turtle()
pen.ht()
pen.color('White')
pen.speed(0)
pen.up()
pen.goto(300,0)
pen.write("MyTimer",font=("Elephant",20,'bold'))

pen2=Turtle()
pen2.ht()
pen2.speed(0)
pen2.up()
pen2.color("White")
beg=time.time()
def start():
    pen2.goto(0,-300)
    pen2.write("Start!!(press up arrow..)",font=("Courier",20,'bold'))


def end():
    pen2.clear()
    en=time.time()
    fin=en-beg
    fin=int(fin)
    pen2.goto(0,0)
    pen2.write(fin,font=("Times",20,'bold'))

def clearr():
    wn.clear()
wn.listen()
wn.onkey(start,"Up")
wn.onkey(end,"Down")
wn.onkey(clearr,"d")
wn.mainloop()
