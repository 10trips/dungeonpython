#created by Ethan Freckleton and Alex Larsen 11/21/2023
import turtle

wn = turtle.Screen()

level = 1
triggers1 = []
triggers2 = []
triggers3 = []
inventory = []
mapscale = 50 # 50 default

#Add ghost
ghost = turtle.Turtle()
ghost.up()
ghost.speed(0)
wn.register_shape('ghost.gif')
ghost.shape('ghost.gif')

drawer = turtle.Turtle()
drawer.up()
drawer.speed(0)

#add player turtle image
player = turtle.Turtle()
player.up()
player.speed(0)
wn.register_shape('knight.gif')
player.shape('knight.gif')

key1 = turtle.Turtle()
key1.up()
key1.speed(0)
key2 = turtle.Turtle()
key2.up()
key2.speed(0)
key3 = turtle.Turtle()
key3.up()
key3.speed(0)
keys = [key1, key2, key3]

wn.register_shape('key.gif')
key1.shape('key.gif')
key2.shape('key.gif')
key3.shape('key.gif')

heart1 = turtle.Turtle()
heart1.up()
heart1.speed(0)
heart2 = turtle.Turtle()
heart2.up()
heart2.speed(0)
heart3 = turtle.Turtle()
heart3.up()
heart3.speed(0)
hearts = [heart1, heart2, heart2]

wn.register_shape('heart.gif')
heart1.shape('heart.gif')
heart2.shape('heart.gif')
heart3.shape('heart.gif')

wn.bgcolor("lightblue")

class trigger:
    #def __init__(self, x1,y1, x2,y2, fun, draw, color, bufer):
    def __init__(self, x1,y1, x2,y2, fun, *others):  
        #x1 and y1 - is bottom left corner of trigger
        #x2 and y2  - is top right corner of trigger
        #fun - is function called when the plr enters the trigger
        #draw - should we draw the  trigger
        #color - draw must be true, what color? (red? green? purple?)
        #bufer - defaults to 15 if not given

        global mapscale        

        if others:
            if not others[0]: #buffer
                self.bufer = 15
            else:
                self.bufer = others[0]     
            if others[1] == True:
                
                self.draw = True
            else:
                self.draw = False
            if not others[2]:
                self.color = "black"
            else:
                self.color = others[2]    
        else:
            self.bufer = 15
            self.draw = True
            self.color = "black"

        self.x1 = x1 * mapscale
        self.y1 = y1 * mapscale
        self.x2 = x2 * mapscale
        self.y2 = y2 * mapscale

        self.fun = fun
        

        if self.draw == True:
            drawer.st()
            drawer.goto(self.x1,self.y2)
        
            # begin render
            drawer.color(self.color)
            drawer.begin_fill()

            drawer.goto(self.x1,self.y2) #top left
            drawer.goto(self.x2,self.y2) #top right
            drawer.goto(self.x2,self.y1) #bottom right
            drawer.goto(self.x1,self.y1) #bottom left

            drawer.end_fill()
        drawer.ht()

            #drawer.ht()
            
    def collision(self):
        
        if ((player.xcor() > self.x1-self.bufer) and (player.xcor() < self.x2+self.bufer) and (player.ycor() > self.y1-self.bufer) and (player.ycor() < self.y2+self.bufer)):
            self.fun()

def checktriggers():
    global level,triggers1,triggers2,triggers3, player, keys, inventory

    updateGhost()
    #Checks the map boarders to prevent glitching outside the map
    if player.xcor() > 9.6*mapscale:
        player.goto(9.6*mapscale, player.ycor())
    if player.xcor() < -9.6*mapscale:
        player.goto(-9.6*mapscale, player.ycor())
    if player.ycor() > 7.6*mapscale:
        player.goto(player.xcor(), 7.6*mapscale)
    if player.ycor() < -7.6*mapscale:
        player.goto(player.xcor(), -7.6*mapscale)

    if level == 1:
        for t in triggers1:
            t.collision()
    for key in keys:
        if player.distance(key) < 20 and key not in inventory:
            inventory.append(key)
            key.goto(10*mapscale - mapscale*len(inventory), 9*mapscale)

def drawboarders():
    global drawer
    drawer.color("black")
    drawer.goto(-10*mapscale, -8*mapscale)
    drawer.down()
    drawer.pensize(5)
    drawer.goto(-10*mapscale, 8*mapscale)
    drawer.goto(10*mapscale, 8*mapscale)
    drawer.goto(10*mapscale, -8*mapscale)
    drawer.goto(-10*mapscale, -8*mapscale)
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
    wn.onkey(None, "r")
def off():
    wn.onkey(None, "w")
    wn.onkey(None, "s")
    wn.onkey(None, "d")
    wn.onkey(None, "a")
    wn.onkey(initlevel1, "r")

def wallcollision():
    global player
    player.undo()

def lava():
    damage()

def damage():
    global health
    if health == 3:
        heart3.ht()
    elif health == 2:
        heart2.ht()
    elif health == 1:
        heart1.ht()
    else:
        deathScreen()
    health -= 1
    resetlevel1()

def gate():
    global inventory, player, drawer
    if len(inventory) > 0:
        inventory.pop(-1)
        print(inventory)
    else:
        player.undo()

def updateGhost():
    global ghost
    ghost.setheading(ghost.towards(player))
    ghost.forward(6)
    if ghost.distance(player) < 20:
        damage()

def resetHearts():
    heart1.goto(-9 *mapscale, 9*mapscale)
    heart2.goto(-8 *mapscale, 9*mapscale)
    heart3.goto(-7 *mapscale, 9*mapscale)
    heart1.st()
    heart2.st()
    heart3.st()

def resetScreen(message, command):
    global drawer, mapscale, level
    off()
    drawer.clear()
    wn.bgpic("nopic")
    player.ht()
    ghost.ht()
    key1.ht()
    key2.ht()
    key3.ht()
    heart1.ht()
    heart2.ht()
    heart3.ht()
    for object in triggers1:
        del object
    for object in triggers2:
        del object
    for object in triggers3:
        del object
    drawer.color("red")
    drawer.goto(-4 * mapscale, 3 * mapscale)
    drawer.write(message, font=("Verdana", 50, "normal"))
    drawer.goto(-4 * mapscale, -3 * mapscale)
    drawer.write(command, font=("Verdana", 36, "normal"))
    drawer.ht()

def deathScreen():
    resetScreen("You Died", "Press 'r' to Restart")

def startScreen():
    resetScreen("Medievel Maze Game", "Press 'r' to Begin")

def winScreen():
    resetScreen("You Win", "Press 'r' to Restart")

def levelScreen():
    global health
    drawer.clear()
    drawboarders()
    wn.bgpic("background.png")
    player.st()
    ghost.st()
    key1.st()
    key2.st()
    key3.st()
    health = 3
    resetHearts()
    on()

def initlevel1():
    global mapscale, level
    level = 1
    levelScreen()
    triggers1.append(trigger(-10,5,2,6,wallcollision,15,True,"black"))
    triggers1.append(trigger(1,1,2,5,wallcollision,15,True,"black"))
    triggers1.append(trigger(3,3,4,8,wallcollision,15,True,"black"))
    triggers1.append(trigger(-3,-1,6,0,wallcollision,15,True,"black"))
    triggers1.append(trigger(5,0,6,5,wallcollision,15,True,"black"))
    triggers1.append(trigger(8,3,10,8,wallcollision,15,True,"black"))
    triggers1.append(trigger(-9,-5,-8,4,wallcollision,15,True,"black"))
    triggers1.append(trigger(-10,-1,-9,0,wallcollision,15,True,"black"))
    triggers1.append(trigger(-7,-8,-6,-4,wallcollision,15,True,"black"))
    triggers1.append(trigger(0,-5,8,-4,wallcollision,15,True,"black"))
    triggers1.append(trigger(-1,1,2,2,wallcollision,15,True,"black"))
    triggers1.append(trigger(-1,1,2,2,wallcollision,15,True,"black"))
    triggers1.append(trigger(5,-2,10,0,lava,15,True,"orange"))# lava
    triggers1.append(trigger(8,-8,10,-2,initlevel2,0,True,"green"))# end
    triggers1.append(trigger(4,-3,5,-2,gate,0,True,"yellow"))# gate

    resetlevel1()

def resetlevel1():
    global mapscale, inventory
    inventory.clear()
    key1.goto(8*mapscale, 1*mapscale)
    key2.goto(11*mapscale, 11*mapscale)
    key3.goto(11*mapscale, 11*mapscale)
    key2.ht()
    key3.ht()
    player.goto(-9*mapscale, 7*mapscale)
    ghost.goto(-9*mapscale,-7*mapscale)

def initlevel2():
    levelScreen()
    for object in triggers1:
        del object
#start main code
startScreen()

wn.listen()
wn.mainloop()