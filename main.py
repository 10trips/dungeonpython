import turtle

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
            if ((leo.xcor() > self.x1-self.buffer) and (leo.xcor() < self.x2+self.buffer) and (leo.ycor() > self.y1-self.buffer) and (leo.ycor() < self.y2+self.buffer)):
                

def test():
    print("world")

print("test1")


mytrigger = trigger(100,100, test, 0,0)
mytrigger.printsome()

#Balls
