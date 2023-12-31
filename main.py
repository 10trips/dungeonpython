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

#add player turtle image
player = turtle.Turtle()
player.up()
player.speed(0)
wn.register_shape('knight.gif')
player.shape('knight.gif')

#Add Logo Icon
icon = turtle.Turtle()
icon.up()
icon.speed(0)
icon.goto(0,0)
wn.register_shape('logo.gif')
icon.shape('logo.gif')

#Create the turtle that Draws
drawer = turtle.Turtle()
drawer.up()
drawer.speed(0)

#Create all keys
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

#Create all hearts
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

class trigger: # object class for trigges/walls
#triggers creates boundaries where if the turtle enters it calls a specified function
    
    def __init__(self, x1,y1, x2,y2, fun, *others):  
        #x1 and y1 - is bottom left corner of trigger
        #x2 and y2  - is top right corner of trigger
        #fun - is function called when the plr enters the trigger

        #others VV the *others parameters are optional parameters that can be given but not required

        #draw - should we draw the  trigger
        #color - draw must be true, what color? (red? green? purple?)
        #bufer - defaults to 15 if not given

        global mapscale, drawer        

        if others: #defaults values if they're not given
            if not others[0]: #buffer
                self.bufer = 15
            else:
                self.bufer = others[0]     
            if others[1] == True: # draw
                
                self.draw = True
            else:
                self.draw = False
            if not others[2]: # color
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
        

        if self.draw == True: #render the box
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
            
    def collision(self): # collision function for the box
        
        if ((player.xcor() > self.x1-self.bufer) and (player.xcor() < self.x2+self.bufer) and (player.ycor() > self.y1-self.bufer) and (player.ycor() < self.y2+self.bufer)):
            self.fun() #call the function if the player is in the box

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
	
	#Checks trigger colisions based off the current level
    if level == 1:
        for t in triggers1:
            t.collision()
    if level == 2:
        for t in triggers2:
            t.collision()
    if level == 3:
        for t in triggers3:
            t.collision()
            
    #Check Key colisions and add to hotbar
    for key in keys:
        if player.distance(key) < 40 and key not in inventory:
            inventory.append(key)
            key.goto(10*mapscale - mapscale*len(inventory), 9*mapscale)

def drawboarders():#Draws the outside boarders
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
 #----Movement: Move player then check colisions---
def up():
    global player
    player.goto(player.xcor(), player.ycor()+10)
    checktriggers()

def down():
    global player
    player.goto(player.xcor(), player.ycor()-10)
    checktriggers()

def right():
    global player
    player.goto(player.xcor()+10, player.ycor())
    checktriggers()

def left():
    global player
    player.goto(player.xcor()-10, player.ycor())
    checktriggers()
#-------

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

def wallcollision():#Funcion that all walls run
    global player
    player.undo()

def lava():#Function for lava triggers
    damage()

def damage(): # resets the level and removes a heart
    global health, level
    if level == 1:
        resetlevel1()
    elif level ==2:
        resetLevel2()
    else:
        resetLevel3()

    if health == 3:
        heart3.ht()
    elif health == 2:
        heart2.ht()
    elif health == 1:
        heart1.ht()
    else:
        deathScreen()
    health -= 1

def updateGhost():#Moves the ghost toward player AND checks if it colides with the player
    global ghost
    ghost.setheading(ghost.towards(player))
    ghost.forward(6)
    if ghost.distance(player) < 20:
        damage()

def resetHearts():#Shows all the hearts.
    heart1.goto(-9 *mapscale, 9*mapscale)
    heart2.goto(-8 *mapscale, 9*mapscale)
    heart3.goto(-7 *mapscale, 9*mapscale)
    heart1.st()
    heart2.st()
    heart3.st()

def resetScreen(message, command):#Clears the screan and adds text
    global drawer, mapscale, level
    off()
    drawer.clear()
    wn.bgpic("nopic")
    ghost.ht()
    player.ht()
    key1.ht()
    key2.ht()
    key3.ht()
    heart1.ht()
    heart2.ht()
    heart3.ht()
    icon.st()
    drawer.color("darkblue")
    drawer.goto(-7 * mapscale, 5 * mapscale)
    drawer.write(message, font=("Verdana", 50, "normal"))
    drawer.goto(-4.5 * mapscale, -6 * mapscale)
    drawer.color("darkred")
    drawer.write(command, font=("Verdana", 36, "normal"))
    drawer.ht()

def deathScreen():#reset screen but specific
    resetScreen("         You Died", "Press 'R' to Restart")

def startScreen():#reset screen but specific
    off()
    resetScreen("Medieval Maze Game", "Press 'R' to Begin")
    drawer.goto(-11 * mapscale, -7 * mapscale)
    drawer.write("Avoid the Ghost, Avoid the red lava, Collect all keys, Reach the green exit", font=("Verdana", 26, "normal"))

def winScreen():#reset screen but specific
    resetScreen("         You Win", "Press 'R' to Restart")

def levelScreen():#Ckears screan and prepares for a level
    global health, inventory
    drawer.clear()
    drawboarders()
    wn.bgpic("background.png")
    icon.ht()
    player.st()
    ghost.st()
    key1.st()
    key2.st()
    key3.st()
    health = 3
    inventory = []
    resetHearts()

#--- Functions for end of level trigger
def finishLevel1():
    if len(inventory) >= 1:
        off()
        initlevel2()

def finishLevel2():
    if len(inventory) >= 2:
        off()
        initlevel3()

def finishLevel3():
    if len(inventory) >= 3:
        off()
        winScreen()
#-------

def initlevel1():#Ran once when level begins
    global mapscale, level
    level = 1
    levelScreen()
    triggers1.append(trigger(-10,4,3,5,wallcollision,15,True,"black"))
    triggers1.append(trigger(-10,-2,-9,-1,wallcollision,15,True,"black"))
    triggers1.append(trigger(-9,2,-8,3,wallcollision,15,True,"black"))
    triggers1.append(trigger(-9,-5,-8,1,wallcollision,15,True,"black"))
    triggers1.append(trigger(-7,-8,-6,-4,wallcollision,15,True,"black"))
    triggers1.append(trigger(-7,3,-2,4,wallcollision,15,True,"black"))
    triggers1.append(trigger(-6,-1,-5,2,wallcollision,15,True,"black"))
    triggers1.append(trigger(-5,-6,-4,-5,wallcollision,15,True,"black"))
    triggers1.append(trigger(-5,-3,-4,-1,wallcollision,15,True,"black"))
    triggers1.append(trigger(-5,1,-4,2,wallcollision,15,True,"black"))
    triggers1.append(trigger(-4,-4,-3,-3,wallcollision,15,True,"black"))
    triggers1.append(trigger(-3,-3,-2,1,wallcollision,15,True,"black"))
    triggers1.append(trigger(-3,5,-2,7,wallcollision,15,True,"black"))
    triggers1.append(trigger(-2,-7,-1,-6,wallcollision,15,True,"black"))
    triggers1.append(trigger(-2,-5,0,-4,wallcollision,15,True,"black"))
    triggers1.append(trigger(-2,-2,6,-1,wallcollision,15,True,"black"))
    triggers1.append(trigger(-1,-4,0,-3,wallcollision,15,True,"black"))
    triggers1.append(trigger(-1,1,0,3,wallcollision,15,True,"black"))
    triggers1.append(trigger(-1,6,0,8,wallcollision,15,True,"black"))
    triggers1.append(trigger(0,-6,7,-5,wallcollision,15,True,"black"))
    triggers1.append(trigger(0,0,3,1,wallcollision,15,True,"black"))
    triggers1.append(trigger(2,-4,3,-2,wallcollision,15,True,"black"))
    triggers1.append(trigger(2,1,3,4,wallcollision,15,True,"black"))
    triggers1.append(trigger(4,-5,5,-3,wallcollision,15,True,"black"))
    triggers1.append(trigger(4,2,5,8,wallcollision,15,True,"black"))
    triggers1.append(trigger(6,0,7,6,wallcollision,15,True,"black"))
    triggers1.append(trigger(8,2,9,8,wallcollision,15,True,"black"))
    triggers1.append(trigger(9,-1,10,8,wallcollision,15,True,"black"))

    triggers1.append(trigger(5,-8,7,-6,lava,15,True,"orange"))# lava
    triggers1.append(trigger(6,-3,10,-1,lava,15,True,"orange"))# lava
    triggers1.append(trigger(8,-8,10,-4,finishLevel1,0,True,"green"))# end
    resetlevel1()
    on()
def resetlevel1():#Ran every time the player dies
    global mapscale, inventory, player
    inventory = []
    player.goto(-9*mapscale, 7*mapscale)
    key1.goto(8*mapscale, 1*mapscale)
    key2.goto(11*mapscale, 11*mapscale)
    key3.goto(11*mapscale, 11*mapscale)
    key2.ht()
    key3.ht()
    ghost.goto(-9*mapscale,-7*mapscale)

def initlevel2():#ran once when level starts
    global level
    level = 2
    levelScreen()
    triggers2.append(trigger(-10,-2,-6,-1,wallcollision,15,True,"black"))
    triggers2.append(trigger(-9,-8,-8,-6,wallcollision,15,True,"black"))
    triggers2.append(trigger(-9,-5,-8,-3,wallcollision,15,True,"black"))
    triggers2.append(trigger(-9,0,-8,5,wallcollision,15,True,"black"))
    triggers2.append(trigger(-9,6,-5,7,wallcollision,15,True,"black"))
    triggers2.append(trigger(-8,-4,-5,-3,wallcollision,15,True,"black"))
    triggers2.append(trigger(-8,0,-3,1,wallcollision,15,True,"black"))
    triggers2.append(trigger(-6,2,-5,7,wallcollision,15,True,"black"))
    triggers2.append(trigger(-5,-8,-4,-5,wallcollision,15,True,"black"))
    triggers2.append(trigger(-5,-3,-4,0,wallcollision,15,True,"black"))
    triggers2.append(trigger(-5,4,-4,5,wallcollision,15,True,"black"))
    triggers2.append(trigger(-4,2,-3,4,wallcollision,15,True,"black"))
    triggers2.append(trigger(-4,6,-2,7,wallcollision,15,True,"black"))
    triggers2.append(trigger(-3,-6,-2,-4,wallcollision,15,True,"black"))
    triggers2.append(trigger(-3,-3,-2,-1,wallcollision,15,True,"black"))
    triggers2.append(trigger(-3,3,-2,4,wallcollision,15,True,"black"))
    triggers2.append(trigger(-2,-8,-1,-5,wallcollision,15,True,"black"))
    triggers2.append(trigger(-2,-2,-1,3,wallcollision,15,True,"black"))
    triggers2.append(trigger(-2,5,-1,8,wallcollision,15,True,"black"))
    triggers2.append(trigger(-1,-6,0,-5,wallcollision,15,True,"black"))
    triggers2.append(trigger(-1,-2,3,-1,wallcollision,15,True,"black"))
    triggers2.append(trigger(-1,2,3,3,wallcollision,15,True,"black"))
    triggers2.append(trigger(0,-4,1,-2,wallcollision,15,True,"black"))
    triggers2.append(trigger(1,-8,2,-5,wallcollision,15,True,"black"))
    triggers2.append(trigger(1,3,2,8,wallcollision,15,True,"black"))
    triggers2.append(trigger(2,-2,3,3,wallcollision,15,True,"black"))

    triggers2.append(trigger(3,-8,4,-4,lava,15,True,"orange"))# lava
    triggers2.append(trigger(3,3,4,6,lava,15,True,"orange"))# lava
    triggers2.append(trigger(4,-3,5,-2,lava,15,True,"orange"))# lava
    triggers2.append(trigger(4,-1,9,0,lava,15,True,"orange"))# lava
    triggers2.append(trigger(4,2,5,3,lava,15,True,"orange"))# lava
    triggers2.append(trigger(5,1,6,3,lava,15,True,"orange"))# lava
    triggers2.append(trigger(5,4,6,7,lava,15,True,"orange"))# lava
    triggers2.append(trigger(6,-5,9,-4,lava,15,True,"orange"))# lava
    triggers2.append(trigger(7,-3,8,-2,lava,15,True,"orange"))# lava
    triggers2.append(trigger(7,1,9,2,lava,15,True,"orange"))# lava
    triggers2.append(trigger(7,7,8,8,lava,15,True,"orange"))# lava
    triggers2.append(trigger(8,2,9,6,lava,15,True,"orange"))# lava
    triggers2.append(trigger(9,-4,10,-3,lava,15,True,"orange"))# lava
    
    triggers2.append(trigger(-1,-8,1,-6,finishLevel2,0,True,"green"))

    resetLevel2()
    on()
def resetLevel2():#ran every time the player dies
    global inventory, mapscale
    inventory = []
    ghost.goto(0,0)
    player.goto(0, 7*mapscale)
    key1.goto(-6*mapscale, -6*mapscale)
    key2.goto(3*mapscale, 7*mapscale)
    key3.ht()

def initlevel3():#ran once when level starts
    global level
    level = 3
    levelScreen()
    triggers3.append(trigger(-10,3,-8,4,wallcollision,15,True,"black"))
    triggers3.append(trigger(-9,5,-8,6,wallcollision,15,True,"black"))
    triggers3.append(trigger(-8,0,9,1,wallcollision,15,True,"black"))
    triggers3.append(trigger(-7,1,-6,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(-6,7,-5,8,wallcollision,15,True,"black"))
    triggers3.append(trigger(-5,2,-4,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(-3,2,-2,6,wallcollision,15,True,"black"))
    triggers3.append(trigger(-1,1,0,8,wallcollision,15,True,"black")) 
    triggers3.append(trigger(0,-8,1,-4,wallcollision,15,True,"black"))
    triggers3.append(trigger(0,-3,1,0,wallcollision,15,True,"black"))
    triggers3.append(trigger(0,2,1,3,wallcollision,15,True,"black"))
    triggers3.append(trigger(0,4,3,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(0,7,1,8,wallcollision,15,True,"black"))
    triggers3.append(trigger(1,-5,2,-4,wallcollision,15,True,"black"))
    triggers3.append(trigger(1,-3,2,-2,wallcollision,15,True,"black"))
    triggers3.append(trigger(1,-1,2,0,wallcollision,15,True,"black"))
    triggers3.append(trigger(2,2,5,3,wallcollision,15,True,"black"))
    triggers3.append(trigger(2,6,7,7,wallcollision,15,True,"black"))
    triggers3.append(trigger(3,-4,4,-1,wallcollision,15,True,"black"))
    triggers3.append(trigger(4,-2,10,-1,wallcollision,15,True,"black"))
    triggers3.append(trigger(4,3,5,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(5,-7,7,-6,wallcollision,15,True,"black"))
    triggers3.append(trigger(5,4,7,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(6,-6,7,-3,wallcollision,15,True,"black"))
    triggers3.append(trigger(6,2,10,3,wallcollision,15,True,"black"))
    triggers3.append(trigger(7,4,8,6,wallcollision,15,True,"black"))
    triggers3.append(trigger(8,-7,9,-3,wallcollision,15,True,"black"))
    triggers3.append(trigger(8,4,10,5,wallcollision,15,True,"black"))
    triggers3.append(trigger(9,-7,10,-6,wallcollision,15,True,"black"))
    
    triggers3.append(trigger(-10,-3,-9,-2,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-9,-6,-8,-5,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-8,-7,-7,0,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-6,-6,-4,-5,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-6,-2,-4,-1,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-4,-7,-3,-1,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-3,-4,-2,-3,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-2,-8,-1,-6,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-2,-5,-1,-2,lava,15,True,"orange"))# lava
    triggers3.append(trigger(-2,-1,-1,0,lava,15,True,"orange"))# lava
    triggers3.append(trigger(1,-8,2,-5,lava,15,True,"orange"))# lava
    triggers3.append(trigger(3,-6,5,-5,lava,15,True,"orange"))# lava
    triggers3.append(trigger(4,-7,5,-6,lava,15,True,"orange"))# lava

    triggers3.append(trigger(8,6,10,8,finishLevel3,0,True,"green"))
    resetLevel3()
    on()
def resetLevel3():#Ran every time player dies
    global inventory, mapscale
    inventory = []
    ghost.goto(0,0)
    player.goto(-9*mapscale, 7*mapscale)
    key1.goto(-2*mapscale, 7*mapscale)
    key2.goto(-5*mapscale, -4*mapscale)
    key3.goto(3*mapscale, -7*mapscale)
    key3.st()
#----- End of functions----

startScreen()#goes to tittle screen

wn.listen()
wn.mainloop()
