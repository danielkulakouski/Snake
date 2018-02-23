###############################################################################
# Name:
#  _____              _      _   _  __     _       _                   _    _ 
# |  __ \            (_)    | | | |/ /    | |     | |                 | |  (_)
# | |  | | __ _ _ __  _  ___| | | ' /_   _| | __ _| | _____  _   _ ___| | ___ 
# | |  | |/ _` | '_ \| |/ _ \ | |  <| | | | |/ _` | |/ / _ \| | | / __| |/ / |
# | |__| | (_| | | | | |  __/ | | . \ |_| | | (_| |   < (_) | |_| \__ \   <| |
# |_____/ \__,_|_| |_|_|\___|_| |_|\_\__,_|_|\__,_|_|\_\___/ \__,_|___/_|\_\_|
# Due Date: December 2016
# Description: Snake Game
###############################################################################

import pygame
import time
from math import sqrt
from random import randint
pygame.init()

HEIGHT = 600
WIDTH  = 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))

grass = pygame.image.load("grass.jpg")
grass = grass.convert_alpha()
grass = pygame.transform.scale(grass, (WIDTH,HEIGHT))

back = pygame.image.load("backButton.png")
back = back.convert_alpha()
back = pygame.transform.scale(back, (50,50))
headU = pygame.image.load("snakeHeadUp.png")
headU = headU.convert_alpha()

play = pygame.image.load("playButton.png")
play = play.convert_alpha()
hover = pygame.image.load("hover.png")
hover = hover.convert_alpha()
playW = 400
playH = 100
playX = WIDTH/2
playY = (HEIGHT/2)+20
play = pygame.transform.scale(play, (playW,playH))
hover = pygame.transform.scale(hover, (playW,playH))

ins = pygame.image.load("instructions.png")
ins = ins.convert_alpha()
insH = pygame.image.load("instructionsHover.png")
insH = insH.convert_alpha()
insX = WIDTH/2
insY = (HEIGHT/2)+150
ins = pygame.transform.scale(ins, (playW,playH))
insH = pygame.transform.scale(insH, (playW,playH))

insPage = pygame.image.load("instructionsPage.png")
insPage = insPage.convert_alpha()
insPage = pygame.transform.scale(insPage, (WIDTH,HEIGHT))

snakeText = pygame.image.load("snakeText.png")
snakeText = snakeText.convert_alpha()
snakeText = pygame.transform.scale(snakeText, (450,150))

gameOverScreen = pygame.image.load("gameOver.png")
gameOverScreen = gameOverScreen.convert_alpha()
gameOverScreen = pygame.transform.scale(gameOverScreen, (450,150))

headD = pygame.image.load("snakeHeadDown.png")
headD = headD.convert_alpha()

headL = pygame.image.load("snakeHeadLeft.png")
headL = headL.convert_alpha()

headR = pygame.image.load("snakeHeadRight.png")
headR = headR.convert_alpha()

bodyU = pygame.image.load("snakeBodyDown.png")
bodyU = bodyU.convert_alpha()

bodyD = pygame.image.load("snakeBodyUp.png")
bodyD = bodyD.convert_alpha()

bodyL = pygame.image.load("snakeBodyRight.png")
bodyL = bodyL.convert_alpha()

bodyR = pygame.image.load("snakeBodyLeft.png")
bodyR = bodyR.convert_alpha()


orange = pygame.image.load("orange.png")
orange = orange.convert_alpha()

kiwi = pygame.image.load("kiwi.png")
kiwi = kiwi.convert_alpha()

banana = pygame.image.load("banana.png")
banana = banana.convert_alpha()

apple = pygame.image.load("apple.png")
apple = apple.convert_alpha()

pois = pygame.image.load("poisApple.png")
pois = pois.convert_alpha()

WHITE = (255,255,255)
BLACK = (0,0,0)
outline=0

timeLimit = 10

BODY_SIZE = []
HSPEED = 20
VSPEED = 20

##speedX = 0
##speedY = VSPEED
speedX = []
speedY = []

segx = [int(WIDTH/2.)]*3
segy = [HEIGHT, HEIGHT+VSPEED, HEIGHT+2*VSPEED]

font = pygame.font.SysFont("Arial Black",30)

segmentCLR = (255,0,0)

fruitx = 0
fruity = 0

poisx,poisy = randint(0,WIDTH/HSPEED)*HSPEED,randint(0,HEIGHT/VSPEED)*VSPEED

score = 0

fruitNum = randint(1,4)
poisRandNum = randint(10,20)

playGame = False
instruction = False

poisApple = False

one = True
two = False
three = False
four = False

gameOverBool = False

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_screen():
    global headU
    global headD
    global headL
    global headR
    global bodyU
    global bodyD
    global bodyL
    global bodyR
    global orange
    global kiwi
    global banana
    global apple
    global gameOverBool
    global end
    global pois

    if(instruction==False):
        screen.blit(grass, (0,0))

        #pygame.draw.rect(screen, (randint(0,255),randint(0,255),randint(0,255)), (fruitx, fruity, 15,15),outline)

        if(playGame==True and gameOverBool==False):
            if(fruitNum==1):
                orange = pygame.transform.scale(orange, (30,30))
                screen.blit(orange, (fruitx-15,fruity-15))
            if(fruitNum==2):
                kiwi = pygame.transform.scale(kiwi, (30,30))
                screen.blit(kiwi, (fruitx-15,fruity-15))
            if(fruitNum==3):
                banana = pygame.transform.scale(banana, (30,30))
                screen.blit(banana, (fruitx-15,fruity-15))
            if(fruitNum==4):
                apple = pygame.transform.scale(apple, (30,30))
                screen.blit(apple, (fruitx-15,fruity-15))

        if(gameOverBool==False):
            for i in range(len(segx)):
                segmentCLR = (255,0,0)
                BODY_SIZE[i] = 20
                BODY_SIZE[0] = 38
                if (i==0):
                    headU = pygame.transform.scale(headU, (BODY_SIZE[0],BODY_SIZE[0]))
                    headD = pygame.transform.scale(headD, (BODY_SIZE[0],BODY_SIZE[0]))
                    headL = pygame.transform.scale(headL, (BODY_SIZE[0],BODY_SIZE[0]))
                    headR = pygame.transform.scale(headR, (BODY_SIZE[0],BODY_SIZE[0]))
                    #screen.blit(head, (segx[0]-(BODY_SIZE[0]/2),segy[0]-(BODY_SIZE[0]/2)))
                    if(speedX[i] == -HSPEED):
                        screen.blit(headL, (segx[0]-(BODY_SIZE[0]/2),segy[0]-(BODY_SIZE[0]/2)))
                    elif(speedX[i] == HSPEED):
                        screen.blit(headR, (segx[0]-(BODY_SIZE[0]/2),segy[0]-(BODY_SIZE[0]/2)))
                    elif(speedY[i] == -VSPEED):
                        screen.blit(headU, (segx[0]-(BODY_SIZE[0]/2),segy[0]-(BODY_SIZE[0]/2)))
                    elif(speedY[i] == VSPEED):
                        screen.blit(headD, (segx[0]-(BODY_SIZE[0]/2),segy[0]-(BODY_SIZE[0]/2)))                      
                else:
                    bodyU = pygame.transform.scale(bodyU, (BODY_SIZE[i],BODY_SIZE[i]))
                    bodyD = pygame.transform.scale(bodyD, (BODY_SIZE[i],BODY_SIZE[i]))
                    bodyL = pygame.transform.scale(bodyL, (BODY_SIZE[i],BODY_SIZE[i]))
                    bodyR = pygame.transform.scale(bodyR, (BODY_SIZE[i],BODY_SIZE[i]))
                    if(speedX[i] == -HSPEED):
                        screen.blit(bodyL, (segx[i]-(BODY_SIZE[i]/2),segy[i]-(BODY_SIZE[i]/2)))
                    elif(speedX[i] == HSPEED):
                        screen.blit(bodyR, (segx[i]-(BODY_SIZE[i]/2),segy[i]-(BODY_SIZE[i]/2)))
                    elif(speedY[i] == -VSPEED):
                        screen.blit(bodyU, (segx[i]-(BODY_SIZE[i]/2),segy[i]-(BODY_SIZE[i]/2)))
                    elif(speedY[i] == VSPEED):
                        screen.blit(bodyD, (segx[i]-(BODY_SIZE[i]/2),segy[i]-(BODY_SIZE[i]/2)))

        if(playGame==True and gameOverBool==False):
            global timeRemaining
            global timeeeeeeee
            global poisApple
            
            text = font.render(str(score), 1, WHITE)
            screen.blit(text,((WIDTH/2)+330,20))
            text2 = font.render("Apples Eaten:",1,WHITE)
            screen.blit(text2,((WIDTH/2)+100,20))
            timeRemaining = int(timeLimit-(time.clock()*3))+timeeeeeeee
            tim = font.render(str(timeRemaining),1,WHITE)
            screen.blit(tim,((WIDTH/2)+330,80))
            text3 = font.render("Time Remaining:",1,WHITE)
            screen.blit(text3,((WIDTH/2)+53,80))

            if(timeRemaining<=0):
                gameOverBool = True

            if(timeRemaining>poisRandNum):
                poisApple=True

            if(poisApple):
                pois = pygame.transform.scale(pois,(30,30))
                screen.blit(pois,(poisx-15,poisy-15))
                
        if(playGame==False):
            introScreen()


        if(gameOverBool==True):
            gameOver()
            
            #pygame.draw.circle(screen, segmentCLR, (segx[i], segy[i]),BODY_SIZE[i], ountline)
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#

pygame.mixer.music.load("backgroundMusic.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops = -1)
eat = pygame.mixer.Sound("eat.wav")
click = pygame.mixer.Sound("click.wav")
click.set_volume(0.4)

def introScreen():
    global timeeeeeeee
    timeeeeeeee = int(time.clock()*3)
    screen.blit(snakeText, ((WIDTH/2)-225,(HEIGHT/2)-220))

    screen.blit(play, (playX-playW/2,playY-playH/2))
    
    (cursorX,cursorY)=pygame.mouse.get_pos()
    if((cursorX>playX-playW/2 and cursorX<playX+playW/2 and cursorY>playY-playH/2 and cursorY<playY+playH/2) and instruction==False):
        screen.blit(hover, (playX-playW/2,playY-playH/2))

    screen.blit(ins, (insX-playW/2,insY-playH/2))
        
    (cursorX,cursorY)=pygame.mouse.get_pos()
    if((cursorX>insX-playW/2 and cursorX<insX+playW/2 and cursorY>insY-playH/2 and cursorY<insY+playH/2) and instruction==False):
        screen.blit(insH, (insX-playW/2,insY-playH/2))

def gameOver():
    #screen.blit(grass, (0,0))
    screen.blit(gameOverScreen,(180,200))
    text = font.render(str(score), 1, WHITE)
    screen.blit(text,((WIDTH/2)+110,380))
    text2 = font.render("Apples Eaten:",1,WHITE)
    screen.blit(text2,((WIDTH/2)-130,380))

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

inPlay = True
exitFlag = False

segmentCLR = [0]*len(segx)
BODY_SIZE = [0]*len(segx)
speedX = [0]*len(segx)
speedY = [0]*len(segx)
fruitx = randint(15,WIDTH-15)
fruity = randint(15,HEIGHT-15)

while inPlay:
    while not exitFlag:         # check for events
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:       # If user clicked close
                exitFlag = True                # Flag that we are done so we exit this loop
                inPlay = False

            if (event.type == pygame.MOUSEBUTTONDOWN):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if(cursorX>playX-playW/2 and cursorX<playX+playW/2 and cursorY>playY-playH/2 and cursorY<playY+playH/2 and instruction==False and playGame==False):
                    playGame = True
                    click.play()

                if(cursorX>insX-playW/2 and cursorX<insX+playW/2 and cursorY>insY-playH/2 and cursorY<insY+playH/2 and instruction==False and playGame==False):
                    instruction = True
                    click.play()
                    
        if(instruction==True):
            screen.blit(insPage, (0,0))
            screen.blit(back,(10,10))

            if(distance(cursorX,cursorY,10,10)<55):
                instruction = False

        if(playGame==True and gameOverBool==False):
            if (distance(segx[0],segy[0],fruitx,fruity)<20):
                fruitx,fruity = randint(0,WIDTH/HSPEED)*HSPEED,randint(0,HEIGHT/VSPEED)*VSPEED
                timeLimit+=5
                eat.play()
                score+=1
                fruitNum = randint(1,4)
                segx.append(segx[-1])           # assign the same x and y coordinates
                segy.append(segy[-1])
                segmentCLR = [0]*len(segx)
                BODY_SIZE = [0]*len(segx)

            if (distance(segx[0],segy[0],poisx,poisy)<20):
                poisx,poisy = randint(0,WIDTH/HSPEED)*HSPEED,randint(0,HEIGHT/VSPEED)*VSPEED
                eat.play()
                timeLimit-=3
                if(len(segx)>2):
                    segx.remove(segx[-1])           # assign the same x and y coordinates
                    segy.remove(segy[-1])

        for i in range(0,len(segx)):
            if(i!=0 and playGame==True):
                if(distance(segx[0],segy[0],segx[i],segy[i])<BODY_SIZE[i]):
                    gameOverBool = True
            
        if(playGame==True and gameOverBool==False):
            keys = pygame.key.get_pressed()
            for i in range(0,len(speedX)):
                if keys[pygame.K_LEFT] and speedX[i]!=HSPEED:
                    speedX[i] = -HSPEED
                    speedY[i] = 0
                elif keys[pygame.K_RIGHT] and speedX[i]!=-HSPEED:
                    speedX[i] = HSPEED
                    speedY[i] = 0
                elif keys[pygame.K_UP] and speedY[i]!=VSPEED:
                    speedX[i] = 0
                    speedY[i] = -VSPEED
                elif keys[pygame.K_DOWN] and speedY[i]!=-VSPEED:
                    speedX[i] = 0
                    speedY[i] = VSPEED
        elif(playGame==False):
            for i in range(0,len(speedX)):
                if(segy[0]<=(HEIGHT/2)-230 and one==True):
                    speedY[i] = 0
                    speedX[i] = -HSPEED
                    one = False
                    two = True
                    three = False
                    Four = False
                if(segx[0]<=(WIDTH/2)-225 and two==True):
                    speedY[i] = VSPEED
                    speedX[i] = 0
                    one = False
                    two = False
                    three = True
                    four = False
                if(segy[0]>=(HEIGHT/2)-60 and three==True):
                    speedY[i] = 0
                    speedX[i] = HSPEED
                    one = False
                    two = False
                    three = False
                    four = True
                if(segx[0]>=(WIDTH/2)+225 and four==True):
                    speedY[i] = -VSPEED
                    speedX[i] = 0
                    one = True
                    two = False
                    three = False
                    four = False
                
                
        if(segx[0]<-1):
            segx[0] = WIDTH-1
        if(segx[0]>WIDTH-1):
            segx[0] = -1
        if(segy[0]<-1):
            segy[0] = HEIGHT-1
        if(segy[0]>HEIGHT-1):
            segy[0] = -1

    # move all segments
        for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
            segx[i]=segx[i-1]               # every segment takes the coordinates
            segy[i]=segy[i-1]               # of the previous one
    # move the head
        segx[0] = segx[0] + speedX[i]
        segy[0] = segy[0] + speedY[i]
    # update the screen
        redraw_screen()
        pygame.time.delay(50)

pygame.mixer.music.stop()
pygame.quit()                           # always quit pygame when done!
