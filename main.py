import turtle

wn = turtle.Screen()


player = turtle.Turtle
player.up()
player.speed(0)
#add player turtle image

drawer = turtle.Turtle
drawer.up()
drawer.speed(0)

class trigger:
    def __init__(self, x1,y1, x2,y2, fun, draw, color, bufer):
        #x1 and y1 - is bottom left corner of trigger
        #x2 and y2  - is top right corner of trigger
        #fun - is function called when the plr enters the trigger
        #draw - should we draw the  trigger
        #color - draw must be true, what color? (red? green? purple?)
        #bufer - defaults to 15 if not given
    
        if not bufer:
            self.bufer = 15
        else:
            self.bufer = bufer        

        self.x1 = x2
        self.y1 = y2
        self.x2 = x2
        self.y2 = y2
        self.fun = fun
        self.draw = draw
        self.color = color
        
        if self.draw == True:
            drawer.goto(x1,y2)
        
            # begin render
            drawer.color(self.color)
            drawer.begin_fill()
            

            drawer.goto(x1,y2) #top left
            drawer.goto(x2,y2) #top right
            drawer.goto(x2,y1) #bottom right
            drawer.goto(x1,y1) #bottom left

            drawer.end_fill()

            drawer.ht()
        def collision():
            if ((player.xcor() > self.x1-self.buffer) and (player.xcor() < self.x2+self.buffer) and (player.ycor() > self.y1-self.buffer) and (player.ycor() < self.y2+self.buffer)):
                self.fun()
                

def test():
    print("world")

def up():
    #checkobjects()
    player.setheading(90)
    player.goto(player.xcor(), player.ycor()+10)

def down():
    #checkobjects()
    player.setheading(270)
    player.goto(player.xcor(), player.ycor()-10)

def right():
    #checkobjects()
    player.setheading(0)
    player.goto(player.xcor()+10, player.ycor())

def left():
    #checkobjects()
    player.setheading(180)
    player.goto(player.xcor()-10, player.ycor())

def on():
    wn.onkey(up, "w")
    wn.onkey(down, "s")
    wn.onkey(right, "d")
    wn.onkey(left, "a")
def off():
    wn.onkey(None, "w")
    wn.onkey(None, "s")
    wn.onkey(None, "d")
    wn.onkey(None, "a")

wn.listen()

wn.mainloop()

#Balls
