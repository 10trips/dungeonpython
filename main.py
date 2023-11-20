import turtle

wn = turtle.Screen()


level = 1
triggers1 = []
triggers2 = []
triggers3 = []

#add player turtle image
player = turtle.Turtle()
player.up()
player.speed(0)
wn.register_shape('knight.gif')
player.shape('knight.gif')

#Add ghost
ghost = turtle.Turtle()
ghost.up()
ghost.speed(0)
wn.register_shape('ghost.gif')
ghost.shape('ghost.gif')

drawer = turtle.Turtle()
drawer.up()
drawer.speed(0)
wn.bgpic("background.png")

class trigger:
    #def __init__(self, x1,y1, x2,y2, fun, draw, color, bufer):
    def __init__(self, x1,y1, x2,y2, fun, *others):  
        #x1 and y1 - is bottom left corner of trigger
        #x2 and y2  - is top right corner of trigger
        #fun - is function called when the plr enters the trigger
        #draw - should we draw the  trigger
        #color - draw must be true, what color? (red? green? purple?)
        #bufer - defaults to 15 if not given
        if others:
            if not others[0]: #buffer
                self.bufer = 15
            else:
                self.bufer = others[0]     
            if not others[1]:
                self.draw = True
            else:
                self.draw = others[1]  
            if not others[2]:
                self.color = "black"
            else:
                self.color = others[2]    
        else:
            self.bufer = 15
            self.draw = True
            self.color = "black"

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fun = fun
        
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
    def collision(self):
        if ((player.xcor() > self.x1-self.bufer) and (player.xcor() < self.x2+self.bufer) and (player.ycor() > self.y1-self.bufer) and (player.ycor() < self.y2+self.bufer)):
            self.fun()

def checktriggers():
    global level,triggers1,triggers2,triggers3

    updateGhost()
    #Checks the map boarders to prevent glitching outside the map
    if player.xcor() > 490:
        player.goto(490, player.ycor())
    if player.xcor() < -490:
        player.goto(-490, player.ycor())
    if player.ycor() > 390:
        player.goto(player.xcor(), 390)
    if player.ycor() < -390:
        player.goto(player.xcor(), -390)

    if level == 1:
        for t in triggers1:
            t.collision()

def drawboarders():
    global drawer
    drawer.color("black")
    drawer.goto(-500, -400)
    drawer.down()
    drawer.pensize(5)
    drawer.goto(-500, 400)
    drawer.goto(500, 400)
    drawer.goto(500, -400)
    drawer.goto(-500, -400)
    drawer.up()

def up():
    global player
    checktriggers()
    player.goto(player.xcor(), player.ycor()+10)

def down():
    global player
    checktriggers()
    player.goto(player.xcor(), player.ycor()-10)

def right():
    global player
    checktriggers()
    player.goto(player.xcor()+10, player.ycor())

def left():
    global player
    checktriggers()
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

def wallcollision():
    global player
    player.undo()

def updateGhost():
    global ghost
    ghost.setheading(ghost.towards(player))
    ghost.forward(10)

triggers1.append(trigger(50,50,100,100,wallcollision,15,True,"red"))

ghost.goto(1000,1000)

drawboarders()
on()
wn.listen()
wn.mainloop()
