import turtle

wn = turtle.Screen()
wn.bgpic("background.png")

class trigger:
    def __init__(self, x, y, fun, draw, color):
        
        self.x = x
        self.y = y
        self.myfun = fun
        self.draw = draw
        self.color = color
    def printsome(self):
        print(self.x,self.y)
        self.myfun()
        if self.draw == True:
            pass
            #draw with color

def test():
    print("world")

print("test1")

def enemy():
	print("enemy")
mytrigger = trigger(100,100, test, 0,0)
mytrigger.printsome()

#Balls
wn.mainloop()