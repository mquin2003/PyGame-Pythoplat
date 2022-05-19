                                                                                           


#Mesatronix
#Pythoplat
#Manuel Quinones, Matthew Wong, Sunny Jin
#You're a king who rules over the tranquility kingdom. The evil fish emperor of the aquatic kingdrom has kidnapped you and trapped you in his kingdom. You must retrieve the key to the door and escape the kingdom.
#----------------------------------------------------
#Fix the control screen
#----------------------------------------------------
from gamelib import *

#Game object
game = Game(900,768,"Pythoplat")

#variables for jumping ac
jumping = False
landed = False

factor = 1

#Keys
keya = Image("images/keya.png",game)
keya.resizeBy(-60)
keya.moveTo(100,100)

keyd = Image("images/keyd.png",game)
keyd.resizeBy(-83)
keyd.moveTo(100,250)

space=Image("images/space.png",game)
space.resizeBy(-40)
space.moveTo(200,400)
#For the intro
f = Font(red,50,black,"Furore Regular")
a = Font(green,50,black,"Furore Regular")
#Title Graphics

play = Image("images/play.png",game)
play.moveTo(450,500)
play.resizeBy(-30)

'''story = Image("images/story.png",game)
story.moveTo(450,600)
story.resizeBy(-30)

controls = Image("images/controls.png",game)
controls.moveTo(450,700)
controls.resizeBy(-30)'''

title = Image("images/logo.png",game)
title.moveTo(450,250)

title.resizeBy(-30)

Go = Image("images/Go.png",game)
Go.resizeBy(-60)
Go.moveTo(450,720)

#Stuff

gameover = Image("images/gameover.png",game)
gameover.resizeTo(game.width,game.height)
win = Image("images/win.png",game)
win.resizeBy(40)
#Bubbles for the top left
bubble = Image("images/Bubble2.png",game)
bubble2 = Image("images/Bubble2.png",game)
bubble4 = Image("images/Bubble2.png",game)
bubble3 = Image("images/Bubble2.png",game)


bubble.resizeBy(-90)
bubble2.resizeBy(-90)
bubble4.resizeBy(-90)
bubble3.resizeBy(-90)


bubble.moveTo(870,30)
bubble2.moveTo(820,30)
bubble4.moveTo(770,30)
bubble3.moveTo(720,30)


#Bubble for block hit
bubble6 = Image("images/coin.png",game)
bubble7 = Image("images/coin.png",game)
bubble8 = Image("images/coin.png",game)
bubble9 = Image("images/coin.png",game)
bubble10 = Image("images/coin.png",game)
bubble11 = Image("images/coin.png",game)
bubble12 = Image("images/coin.png",game)

bubble6.resizeBy(-80)
bubble7.resizeBy(-80)
bubble8.resizeBy(-80)
bubble9.resizeBy(-80)
bubble10.resizeBy(-80)
bubble11.resizeBy(-80)
bubble12.resizeBy(-80)

bubble6.moveTo(270,400)
bubble7.moveTo(1000,550)
bubble8.moveTo(445,30)
bubble9.moveTo(480,30)
bubble10.moveTo(1105,150)
bubble11.moveTo(1140,150)
bubble12.moveTo(1175,150)

bubble6.visible = False
bubble7.visible = False
bubble8.visible = False
bubble9.visible = False
bubble10.visible = False
bubble11.visible = False
bubble12.visible = False
#Goground Image
bk = Image("images/background.jpg",game)
bk.resizeTo(game.width,game.height)

#King Image
king = Image("images/king.png",game)
king2 = Image("images/king2.png",game)

king.resizeBy(-52)
king2.resizeBy(-52)

king.moveTo(60,695)
king2.moveTo(-100,1000)

#Ground Images
ground = Image("images/groundn.png",game)
ground2 = Image("images/groundn.png",game)
ground3 = Image("images/groundn.png",game)

ground.moveTo(450,530)
ground3.moveTo(1000,530)
ground2.moveTo(1000,530)

#Fish
fish = Image("images/fish3.png",game)
fish2 = Image("images/fish2.png",game)
fish3 = Image("images/fish3.png",game)

fish.resizeBy(-65)
fish2.resizeBy(-65)
fish3.resizeBy (-65)

fish.moveTo(564,580)
fish2.moveTo(515,580)
fish3.moveTo(1280,340)

fish2.visible = False

#Door
door = Animation("images/a.png",11,game,1500/3,2000/4)
door.resizeBy(-60)
door.moveTo(1200,670)
door.stop()


#Extra
extra = Animation("images/extra.png",7,game,1536/3,1536/3,0.1)
extra.resizeBy(-90)
extra.moveTo(500,70)

extra2 = Animation("images/extra2.png",16,game,1500/3,2184/6)
extra2.resizeBy(-85)
extra2.moveTo(400,50)

extra3 = Animation("images/extra3.png",8,game,351/3,444/3)
extra3.resizeBy(-70)
extra3.moveTo(20,70)
 
#Yellow Q block Images
itemq = Image("images/Question.jpg",game)
itemq1 = Image("images/Question.jpg",game)
itemq2 = Image("images/Question.jpg",game)
itemq3 = Image("images/Question.jpg",game)
itemq4 = Image("images/Question.jpg",game)
itemq5 = Image("images/Question.jpg",game)
itemq6 = Image("images/Question.jpg",game)


itemq.resizeBy(-83)
itemq1.resizeBy(-83)
itemq2.resizeBy(-83)
itemq3.resizeBy(-83)
itemq4.resizeBy(-83)
itemq5.resizeBy(-83)
itemq6.resizeBy(-83)
#Brown Q block Images
itemb = Image("images/item2.png",game)
itemb1 = Image("images/item2.png",game)
itemb2 = Image("images/item2.png",game)
itemb3 = Image("images/item2.png",game)
itemb4 = Image("images/item2.png",game)
itemb5 = Image("images/item2.png",game)
itemb6 = Image("images/item2.png",game)

itemb.resizeBy(-96.5)
itemb1.resizeBy(-96.5)
itemb2.resizeBy(-96.5)
itemb3.resizeBy(-96.5)
itemb4.resizeBy(-96.5)
itemb5.resizeBy(-96.5)
itemb6.resizeBy(-96.5)


itemb.visible = False
itemb1.visible = False
itemb2.visible = False
itemb3.visible = False
itemb4.visible = False
itemb5.visible = False
itemb6.visible = False
#Key
key = Image("images/key.png",game)
key.resizeBy(-69)
key.moveTo(80,200)
key.visible = False

key2 = Image("images/key.png",game)
key2.resizeBy(-69)
key2.moveTo(bubble.x,bubble.y+40)
key2.visible = False
#Jumping
onbrick = False


#Brick Images
brick = Image("images/Brick.png",game)
brick1 = Image("images/Brick.png",game)
brick2 = Image("images/Brick.png",game)
brick3 = Image("images/Brick.png",game)
brick4 = Image("images/Brick.png",game)
brick5 = Image("images/Brick.png",game)
brick6 = Image("images/Brick.png",game)
brick7 = Image("images/Brick.png",game)
brick8 = Image("images/Brick.png",game)
brick9 = Image("images/Brick.png",game)
brick10 = Image("images/Brick.png",game)
brick11 = Image("images/Brick.png",game)
brick12 = Image("images/Brick.png",game)
brick13 = Image("images/Brick.png",game)
brick14 = Image("images/Brick.png",game)
brick15 = Image("images/Brick.png",game)
brick16 = Image("images/Brick.png",game)
brick17 = Image("images/Brick.png",game)
brick18 = Image("images/Brick.png",game)
brick19 = Image("images/Brick.png",game)
brick20 = Image("images/Brick.png",game)
brick21 = Image("images/Brick.png",game)
brick22 = Image("images/Brick.png",game)
brick23 = Image("images/Brick.png",game)
brick24 = Image("images/Brick.png",game)
brick25 = Image("images/Brick.png",game)
brick26 = Image("images/Brick.png",game)
brick27 = Image("images/Brick.png",game)
brick28 = Image("images/Brick.png",game)
brick29 = Image("images/Brick.png",game)
brick30 = Image("images/Brick.png",game)
brick31 = Image("images/Brick.png",game)
brick32 = Image("images/Brick.png",game)
brick33 = Image("images/Brick.png",game)
brick34 = Image("images/Brick.png",game)
brick35 = Image("images/Brick.png",game)
brick36 = Image("images/Brick.png",game)
brick37 = Image("images/Brick.png",game)
brick38 = Image("images/Brick.png",game)
brick39 = Image("images/Brick.png",game)
brick40 = Image("images/Brick.png",game)
brick41 = Image("images/Brick.png",game)
brick42 = Image("images/Brick.png",game)
brick43 = Image("images/Brick.png",game)
brick44 = Image("images/Brick.png",game)
brick45 = Image("images/Brick.png",game)
brick46 = Image("images/Brick.png",game)
brick47 = Image("images/Brick.png",game)
brick48 = Image("images/Brick.png",game)
brick49 = Image("images/Brick.png",game)
brick50 = Image("images/Brick.png",game)

brick.resizeBy(-60)
brick1.resizeBy(-60)
brick2.resizeBy(-60)
brick3.resizeBy(-60)
brick4.resizeBy(-60)
brick5.resizeBy(-60)
brick6.resizeBy(-60)
brick7.resizeBy(-60)
brick8.resizeBy(-60)
brick9.resizeBy(-60)
brick10.resizeBy(-60)
brick11.resizeBy(-60)
brick12.resizeBy(-60)
brick13.resizeBy(-60)
brick15.resizeBy(-60)
brick14.resizeBy(-60)
brick16.resizeBy(-60)
brick17.resizeBy(-60)
brick18.resizeBy(-60)
brick19.resizeBy(-60)
brick20.resizeBy(-60)
brick21.resizeBy(-60)
brick22.resizeBy(-60)
brick23.resizeBy(-60)
brick24.resizeBy(-60)
brick25.resizeBy(-60)
brick26.resizeBy(-60)
brick27.resizeBy(-60)
brick28.resizeBy(-60)
brick29.resizeBy(-60)
brick30.resizeBy(-60)
brick31.resizeBy(-60)
brick32.resizeBy(-60)
brick33.resizeBy(-60)
brick34.resizeBy(-60)
brick35.resizeBy(-60)
brick36.resizeBy(-60)
brick37.resizeBy(-60)
brick38.resizeBy(-60)
brick39.resizeBy(-60)
brick40.resizeBy(-60)
brick41.resizeBy(-60)
brick42.resizeBy(-60)
brick43.resizeBy(-60)
brick44.resizeBy(-60)
brick45.resizeBy(-60)
brick46.resizeBy(-60)
brick47.resizeBy(-60)
brick48.resizeBy(-60)
brick49.resizeBy(-60)
brick50.resizeBy(-60)

brick49.visible = False
#Platform
brick.moveTo(200,630)
brick1.moveTo(235,630)
brick2.moveTo(270,630)
brick3.moveTo(305,630)
brick4.moveTo(340,630)

#Platform
brick5.moveTo(460,630)
brick6.moveTo(495,630)
brick7.moveTo(530,630)
brick8.moveTo(565,630)

#Platform with Q block
brick9.moveTo(235,475)
itemq.moveTo(270,475)
itemb.moveTo(270,475)
brick15.moveTo(305,475)

#Platform with Spikes
brick10.moveTo(305,630)
brick11.moveTo(690,630)
brick12.moveTo(725,630)
brick13.moveTo(760,630)
brick14.moveTo(795,630)


#Platform with Q block
brick16.moveTo(930,630)
brick17.moveTo(965,630)
itemq1.moveTo(1000,630)
itemb1.moveTo(1000,630)
brick18.moveTo(1070,630)
brick19.moveTo(1035,630)

#Platform
brick20.moveTo(830,500)
brick21.moveTo(760,500)
brick22.moveTo(795,500)

#Platform
brick23.moveTo(690,370)
brick24.moveTo(655,370)
brick25.moveTo(620,370)

#Platform
brick26.moveTo(515,240)
brick27.moveTo(480,240)
itemq2.moveTo(445,110)
itemb2.moveTo(445,110)
itemq3.moveTo(480,110)
itemb3.moveTo(480,110)
brick28.moveTo(445,240)
brick48.moveTo(410,240)

#Platform
brick29.moveTo(830,240)
brick30.moveTo(865,240)
brick31.moveTo(795,240)


#Platform
brick32.moveTo(305,240)
brick33.moveTo(270,240)
brick34.moveTo(235,240)


#Platform
brick35.moveTo(60,240)
brick36.moveTo(95,240)
brick37.moveTo(25,240)
brick38.moveTo(130,240)

#Platform
brick39.moveTo(1000,370)
brick40.moveTo(1035,370)
brick41.moveTo(1070,370)
brick42.moveTo(1105,370)
brick43.moveTo(1140,370)
brick44.moveTo(1175,370)
itemq4.moveTo(1105,200)
itemq5.moveTo(1140,200)
itemq6.moveTo(1175,200)
itemb4.moveTo(1105,200)
itemb5.moveTo(1140,200)
itemb6.moveTo(1175,200)
brick46.moveTo(1245,370)
brick47.moveTo(1280,370)


#Invisible
brick49.moveTo(250,630)
brick50.moveTo(200,630)

#Spikes
spike = Image("images/Spikes.png",game)
spike2 = Image("images/Spikes.png",game)

spike.moveTo(390,722)
spike2.moveTo(741,600)

spike.resizeBy(-68)
spike2.resizeBy(-72)

king.health = 100

#Title Screen
while not game.over:
    game.processInput()

    bk.draw()
    #story.draw()
    #controls.draw()
    play.draw()
    king.draw()
    title.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    
    game.update(60)

game.over = False
#Level One Game Loop
while not game.over:
    game.processInput()
    bk.draw()
    Go.draw()
    keya.draw()
    keyd.draw()
    space.draw()
    game.drawText("The A Key Is Left", 175,80,f)
    game.drawText("The D Key Is Right", 175,230,f)
    game.drawText("The SPACE Key Is To Jump", 400,380,f)
    game.drawText("By jumping on the fish the key will spawn",125,500,f)
    game.drawText("Hitting the bottom of the yellow block",150,600,f)
    game.drawText("will give you a point", 275,650,f)
    if Go.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(60)

game.over = False

while not game.over:
    game.processInput()
    bk.draw()
    
    door.draw()
    
    king.draw()
    king2.draw()

    
    ground.draw()
    ground2.draw()
    ground3.draw()
    
    fish.draw()    
    fish2.draw()
    fish3.draw()
    
    
    extra.draw()
    extra2.draw()
    extra3.draw()
    
    bubble.draw()
    bubble2.draw()
    bubble4.draw()
    bubble3.draw()


    bubble6.draw()
    bubble7.draw()
    bubble8.draw()
    bubble9.draw()
    bubble10.draw()
    bubble11.draw()
    bubble12.draw()
    
    brick.draw()
    brick1.draw()
    brick2.draw()
    brick3.draw()
    brick4.draw()
    brick5.draw()
    brick6.draw()
    brick7.draw()
    brick8.draw()
    brick9.draw()
    brick10.draw()
    brick11.draw()
    brick12.draw()
    brick13.draw()
    brick15.draw()
    brick14.draw()
    brick16.draw()
    brick17.draw()
    brick18.draw()
    brick19.draw()
    brick20.draw()
    brick21.draw()
    brick22.draw()
    brick23.draw()
    brick24.draw()
    brick25.draw()
    brick26.draw()
    brick27.draw()
    brick28.draw()
    brick29.draw()
    brick30.draw()
    brick31.draw()
    brick32.draw()
    brick33.draw()
    brick34.draw()
    brick35.draw()
    brick36.draw()
    brick37.draw()
    brick38.draw()
    brick39.draw()
    brick40.draw()
    brick41.draw()
    brick42.draw()
    brick43.draw()
    brick44.draw()
    brick45.draw()
    brick46.draw()
    brick47.draw()
    brick48.draw()
    brick49.draw()
    #brick50.draw()

    itemq.draw()
    itemq1.draw()
    itemq2.draw()
    itemq3.draw()
    '''itemq4.draw()
    itemq5.draw()
    itemq6.draw()'''
    
    itemb.draw()
    itemb1.draw()
    itemb2.draw()
    itemb3.draw()
    '''itemb4.draw()
    itemb5.draw()
    itemb6.draw()'''    
    
    spike.draw()
    spike2.draw()

    key.draw()
    key2.draw()





    

    if king.y< 690:
        landed = False#not landed
    else:
        landed = True

    if king2.y< 690:
       landed = False#not landed
    else:
        landed = True




    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True




    if king2.collidedWith(brick,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2


    if king2.collidedWith(brick2,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick3,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2



    if king2.collidedWith(brick7,"rectangle") or king.collidedWith(brick7,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2



    if king2.collidedWith(itemq,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2


    if king2.collidedWith(itemq1,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick21,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick30,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

   
    if king2.collidedWith(brick24,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick27,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick30,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick33,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick36,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick41,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick44,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king2.collidedWith(brick46,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2
#---------------------------------------------------------------------------------------------------------------------------------            
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True
#------------------------------------------------------------------------------------------------------------------------------------
    if king.collidedWith(brick46,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

        
    if king.collidedWith(brick44,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick41,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2


    if king.collidedWith(brick,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2


    if king.collidedWith(brick2,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick3,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2



    if king.collidedWith(brick7,"rectangle") or king.collidedWith(brick7,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2



    if king.collidedWith(itemq,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2


    if king.collidedWith(itemq1,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick21,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick30,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

   
    if king.collidedWith(brick24,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick27,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick30,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick33,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(brick36,"rectangle") and king.y < 680:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)
        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2

    if king.collidedWith(itemq3,"rectangle") and king.y < 110:
        landed = True
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True
        if keys.Pressed[K_d]:
            king.x+=2
            king.visible = True
            king2.visible = False
            king2.moveTo(king.x,king.y)


        if keys.Pressed[K_a]:
        #king.nextFrame()
            king2.x-=2   


    #-------------------------------------------------------------------
    fish.x-=1
    if fish.x<=460:
        fish.moveTo(580,580)

    fish3.x-=1
    if fish.x>=990:
        fish3.moveTo(1280,280)
    if fish3.isOffScreen:
        fish3.moveTo(1280,280)
        if keys.Pressed[K_d]:
            fish3.x-=3

#    if fish.x<=460:
 #       fish.moveTo(580,580)

        

            
    #-------------------------------------------------------------------

    if king.collidedWith(fish2) and king.bottom > fish2.top:#Needs Fixing
        key.visible = True
        fish2.visible = False
        fish.visible = False
        fish.moveTo(-1000,-1000)
        fish2.moveTo(-1000,-1000)

    if king2.collidedWith(fish2)and king.bottom > fish2.top:#Needs Fixing
        key.visible = True
        fish2.visible = False
        fish.visible = False
        fish.moveTo(-1000,-1000)
        fish2.moveTo(-1000,-1000)
        
    if king.collidedWith(fish) and king.bottom > fish.top:#Needs Fixing
        key.visible = True
        fish2.visible = False
        fish.visible = False
        fish.moveTo(-1000,-1000)
        fish2.moveTo(-1000,-1000)        
    if king2.collidedWith(fish) and king.bottom > fish.top:#Needs Fixing
        key.visible = True
        fish2.visible = False
        fish.visible = False
        fish.moveTo(-1000,-1000)
        fish2.moveTo(-1000,-1000)


    if king.collidedWith(itemq) or king2.collidedWith(itemq):
        itemb.visible = True
        bubble6.visible = True

    if king.collidedWith(itemq1) or king2.collidedWith(itemq1):
        itemb1.visible = True
        bubble7.visible = True

        
    if king.collidedWith(itemq2) or king2.collidedWith(itemq2):
        itemb2.visible = True
        bubble8.visible = True

    if king.collidedWith(itemq3 )or king2.collidedWith(itemq3):
        itemb3.visible = True
        bubble9.visible = True

    '''if king.collidedWith(itemq4 )or king2.collidedWith(itemq4):
        itemb4.visible = True
        bubble10.visible = True

    if king.collidedWith(itemq5 )or king2.collidedWith(itemq5):
        itemb5.visible = True
        bubble11.visible = True

    if king.collidedWith(itemq6 )or king2.collidedWith(itemq6):
        itemb6.visible = True
        bubble12.visible = True'''


    if king.collidedWith(key):
            key2.resizeBy(-50)
            key2.visible = True
            key.visible = False

    if king.collidedWith(bubble6) or king2.collidedWith(bubble6):
        king.health+=25
        bubble6.visible = False
        if king.health>100:
            king.health-=25

    if king.collidedWith(bubble7) or king2.collidedWith(bubble7):
        king.health+=25
        bubble7.visible = False
        if king.health>100:
            king.health-=25

    if king.collidedWith(bubble8) or king2.collidedWith(bubble8):
        king.health+=25
        bubble8.visible = False
        if king.health>100:
            king.health-=25

    if king.collidedWith(bubble9) or king2.collidedWith(bubble9):
        king.health+=25
        bubble9.visible = False
        if king.health>100:
            king.health-=25

    if king.collidedWith(bubble10) or king2.collidedWith(bubble10):
        king.health+=25
        bubble10.visible = False
        if king.health>100:
            king.health-=25
    
    if king.collidedWith(bubble11) or king2.collidedWith(bubble11):
        king.health+=25
        bubble11.visible = False
        if king.health>100:
            king.health-=25
    if king.collidedWith(bubble11) or king2.collidedWith(bubble11):
        king.health+=25
        bubble12.visible = False
        if king.health>100:
            king.health-=25
    

 
            


    if jumping:
        #king.nextFrame()
        king.y -=27*factor#adjust for the drop
        king2.y -=27*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping
        king.y +=3#adjust for the height of the jump - lower number higher jump
        king2.y +=3
        #king.nextFrame()


    if king.makeVisible:
        extra.x+=2
        extra2.x-=2
        extra3.x-=2
        
    if extra2.isOffScreen("left"):
        y = randint(20,200)
        extra2.moveTo(950,y)

    if extra.isOffScreen("right"):
        y = randint(20,200)
        extra.moveTo(-50,y)

    if extra3.isOffScreen("left"):
        y = randint(20,200)
        extra3.moveTo(950,y)

    if not landed: #is jumping
        king.y +=6
        king2.y +=6#adjust for the height of the jump - lower number higher jump
        #king.nextFrame()


    if king.x>=400 and keys.Pressed[K_d]:
        brick.x-=3
        brick1.x-=3
        brick2.x-=3
        brick3.x-=3
        brick4.x-=3
        brick5.x-=3
        brick6.x-=3
        brick7.x-=3
        brick8.x-=3
        brick9.x-=3
        itemq.x-=3
        itemb.x-=3
        brick15.x-=3
        brick10.x-=3
        brick11.x-=3
        brick12.x-=3
        brick13.x-=3
        brick14.x-=3
        brick16.x-=3
        brick17.x-=3
        itemq1.x-=3
        itemb1.x-=3
        brick18.x-=3
        brick19.x-=3
        brick20.x-=3
        brick21.x-=3
        brick22.x-=3
        brick23.x-=3
        brick24.x-=3
        brick25.x-=3
        brick26.x-=3
        brick27.x-=3
        itemq2.x-=3
        itemb2.x-=3
        itemq3.x-=3
        itemb3.x-=3
        brick28.x-=3
        brick48.x-=3
        brick29.x-=3
        brick30.x-=3
        brick31.x-=3
        brick32.x-=3
        brick33.x-=3
        brick34.x-=3
        brick35.x-=3
        brick36.x-=3
        brick37.x-=3
        brick38.x-=3
        brick39.x-=3
        brick40.x-=3
        brick41.x-=3
        brick42.x-=3
        brick43.x-=3
        brick44.x-=3
        brick45.x-=3
        brick46.x-=3
        brick47.x-=3
        spike.x-=3
        spike2.x-=3
        key.x-=3
        bubble6.x-=3
        bubble7.x-=3
        bubble8.x-=3
        bubble9.x-=3
        bubble10.x+=3
        bubble11.x+=3
        bubble12.x+=3
        fish.x-=3
        fish2.x-=3
        fish3.x-=3
        door.x -=3
        '''itemq4.x-=3
        itemq5.x-=3
        itemq6.x-=3
        itemb4.x-=3
        itemb5.x-=3
        itemb6.x-=3'''

    if king2.x<=800 and keys.Pressed[K_a]:
        brick.x+=3
        brick1.x+=3
        brick2.x+=3
        brick3.x+=3
        brick4.x+=3
        brick5.x+=3
        brick6.x+=3
        brick7.x+=3
        brick8.x+=3
        brick9.x+=3
        itemq.x+=3
        itemb.x+=3
        brick15.x+=3
        brick10.x+=3
        brick11.x+=3
        brick12.x+=3
        brick13.x+=3
        brick14.x+=3
        brick16.x+=3
        brick17.x+=3
        itemq1.x+=3
        itemb1.x+=3
        brick18.x+=3
        brick19.x+=3
        brick20.x+=3
        brick21.x+=3
        brick22.x+=3
        brick23.x+=3
        brick24.x+=3
        brick25.x+=3
        brick26.x+=3
        brick27.x+=3
        itemq2.x+=3
        itemb2.x+=3
        itemq3.x+=3
        itemb3.x+=3
        brick28.x+=3
        brick48.x+=3
        brick29.x+=3
        brick30.x+=3
        brick31.x+=3
        brick32.x+=3
        brick33.x+=3
        brick34.x+=3
        brick35.x+=3
        brick36.x+=3
        brick37.x+=3
        brick38.x+=3
        brick39.x+=3
        brick40.x+=3
        brick41.x+=3
        brick42.x+=3
        brick43.x+=3
        brick44.x+=3
        brick45.x+=3
        brick46.x+=3
        brick47.x+=3
        spike.x+=3
        spike2.x+=3
        key.x+=3
        bubble6.x+=3
        bubble7.x+=3
        bubble8.x+=3
        bubble9.x+=3
        bubble10.x+=3
        bubble11.x+=3
        bubble12.x+=3
        fish.x+=3
        fish2.x+=3
        fish3.x+=3
        door.x+=3
        '''itemq4.x+=3
        itemq5.x+=3
        itemq6.x+=3
        itemb4.x+=3
        itemb5.x+=3
        itemb6.x+=3'''

    if king2.left <=game.left:
        king2.x = king2.width
        brick.moveTo(200,630)
        brick1.moveTo(235,630)
        brick2.moveTo(270,630)
        brick3.moveTo(305,630)
        brick4.moveTo(340,630)
        brick5.moveTo(460,630)
        brick6.moveTo(495,630)
        brick7.moveTo(530,630)
        brick8.moveTo(565,630)
        brick9.moveTo(235,475)
        itemq.moveTo(270,475)
        itemb.moveTo(270,475)
        brick15.moveTo(305,475)
        brick10.moveTo(305,630)
        brick11.moveTo(690,630)
        brick12.moveTo(725,630)
        brick13.moveTo(760,630)
        brick14.moveTo(795,630)
        brick16.moveTo(930,630)
        brick17.moveTo(965,630)
        itemq1.moveTo(1000,630)
        itemb1.moveTo(1000,630)
        brick18.moveTo(1070,630)
        brick19.moveTo(1035,630)
        brick20.moveTo(830,500)
        brick21.moveTo(760,500)
        brick22.moveTo(795,500)
        brick23.moveTo(690,370)
        brick24.moveTo(655,370)
        brick25.moveTo(620,370)
        brick26.moveTo(515,240)
        brick27.moveTo(480,240)
        itemq2.moveTo(445,110)
        itemb2.moveTo(445,110)
        itemq3.moveTo(480,110)
        itemb3.moveTo(480,110)
        brick28.moveTo(445,240)
        brick48.moveTo(410,240)
        brick29.moveTo(830,240)
        brick30.moveTo(865,240)
        brick31.moveTo(795,240)
        brick32.moveTo(305,240)
        brick33.moveTo(270,240)
        brick34.moveTo(235,240)
        brick35.moveTo(60,240)
        brick36.moveTo(95,240)
        brick37.moveTo(25,240)
        brick38.moveTo(130,240)
        brick39.moveTo(1000,370)
        brick40.moveTo(1035,370)
        brick41.moveTo(1070,370)
        brick42.moveTo(1105,370)
        brick43.moveTo(1140,370)
        brick44.moveTo(1175,370)
        brick45.moveTo(1210,370)
        brick46.moveTo(1245,370)
        brick47.moveTo(1280,370)
        spike.moveTo(390,722)
        spike2.moveTo(741,600)
        door.moveTo(1200,670)
        bubble6.moveTo(270,400)
        bubble7.moveTo(1000,550)
        bubble8.moveTo(445,30)
        bubble9.moveTo(480,30)
        fish3.moveTo(1000,340)
        '''itemq4.moveTo(1105,200)
        itemq5.moveTo(1140,200)
        itemq6.moveTo(1175,200)
        itemb4.moveTo(1105,200)
        itemb5.moveTo(1140,200)
        itemb6.moveTo(1175,200)
        bubble10.moveTo(itemq4.x,itemq4.y+5)
        bubble11.moveTo(itemq5.x,itemq5.y+5)
        bubble12.moveTo(itemq6.x,itemq6.y+5)'''
        
    if king.right >= game.right:
        king.x = king.width+730
 

    if king2.x>=800 and keys.Pressed[K_a]:
        brick.x+=0
        brick1.x+=0
        brick2.x+=0
        brick3.x+=0
        brick4.x+=0
        brick5.x+=0
        brick6.x+=0
        brick7.x+=0
        brick8.x+=0
        brick9.x+=0
        itemq.x+=0
        itemb.x+=0
        brick15.x+=0
        brick10.x+=0
        brick11.x+=0
        brick12.x+=0
        brick13.x+=0
        brick14.x+=0
        brick16.x+=0
        brick17.x+=0
        itemq1.x+=0
        itemb1.x+=0
        brick18.x+=0
        brick19.x+=0
        brick20.x+=0
        brick21.x+=0
        brick22.x+=0
        brick23.x+=0
        brick24.x+=0
        brick25.x+=0
        brick26.x+=0
        brick27.x+=0
        itemq2.x+=0
        itemb2.x+=0
        itemq3.x+=0
        itemb3.x+=0
        brick28.x+=0
        brick48.x+=0
        brick29.x+=0
        brick30.x+=0
        brick31.x+=0
        brick32.x+=0
        brick33.x+=0
        brick34.x+=0
        brick35.x+=0
        brick36.x+=0
        brick37.x+=0
        brick38.x+=0
        brick39.x+=0
        brick40.x+=0
        brick41.x+=0
        brick42.x+=0
        brick43.x+=0
        brick44.x+=0
        brick45.x+=0
        brick46.x+=0
        brick47.x+=0
        spike.x+=0
        spike2.x+=0
        key.x+=0
        bubble6.x+=0
        bubble7.x+=0
        bubble8.x+=0
        bubble9.x+=0

    if key.y<=30:
            key.moveTo(715,30)
    if keys.Pressed[K_SPACE] and onbrick and not jumping:
        jumping = True

    if keys.Pressed[K_d]:
        #king.nextFrame()
       king.x+=3
       king2.moveTo(king.x,king.y)
       king.visible = True
       king2.visible = False
       
    if keys.Pressed[K_a]:
        king2.x-=3
        king.visible = False
        king2.visible = True
        king.moveTo(king2.x,king2.y)

        

    if king.collidedWith(spike) or king2.collidedWith(spike2)or king2.collidedWith(spike) or king.collidedWith(spike2):
        king.health-=25
        king.moveTo(brick38.x,695)
        king2.moveTo(brick38.x,695)
    if king.health<100:
        bubble.moveTo(-1000,1000)

    if king.collidedWith(spike) or king2.collidedWith(spike2)or king2.collidedWith(spike) or king.collidedWith(spike2):
        king.health-=25
        king.moveTo(brick38.x,695)
        king2.moveTo(brick38.x,695)
    if king.health<75:
        bubble4.moveTo(-1000,1000)

    if king.collidedWith(spike) or king2.collidedWith(spike2)or king2.collidedWith(spike) or king.collidedWith(spike2):
        king.health-=25
        king.moveTo(brick38.x,695)
        king2.moveTo(brick38.x,695)
    if king.health<50:
        bubble3.moveTo(-1000,1000)

    if king.collidedWith(spike) or king2.collidedWith(spike2)or king2.collidedWith(spike) or king.collidedWith(spike2):
        king.health-=25
        king.moveTo(brick38.x,695)
        king2.moveTo(brick38.x,695)
    if king.health<25:
        bubble2.moveTo(-1000,1000)

    if king.health>=25:
        bubble2.moveTo(720,30)
    if king.health>=99:
        bubble.moveTo(870,30)
    if king.health>=50:
        bubble3.moveTo(770,30)
    if king.health>=75:
        bubble4.moveTo(820,30)

    if bubble.isOffScreen("all") and bubble4.isOffScreen("all") and bubble3.isOffScreen("all") and bubble2.isOffScreen("all"):
        game.over = True
        gameover.draw()

    if king.collidedWith(door)and key2.y<=70 and keys.Pressed[K_s]:
        game.over = True
        win.draw()
    if king2.collidedWith(door) and key2.y<=70 and keys.Pressed[K_s]:
        game.over =True
        bk.draw()
        win.draw()
        
        

    game.update(60)
    
    







    
