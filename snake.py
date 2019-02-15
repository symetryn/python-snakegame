import pygame
import time
import random
pygame.init()

red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
grey=(192,192,192)
display_width=800
display_height=600
block_movement=10
block_size=10
FPS=20
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')


clock=pygame.time.Clock()

font=pygame.font.SysFont(None,25)
def snake(block_size,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],block_size,block_size])
        
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    
def gameLoop():
    gameExit=False
    gameOver=False
    lead_x= display_width/2
    lead_y= display_height/2
    
    lead_x_change=0
    lead_y_change=10
    
    snakeList=[]
    snakeLength=6
    
    randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
    while not gameExit:
        while gameOver==True:
            gameDisplay.fill(grey)
            message_to_screen("Game over, press C to play again and Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=False
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    elif event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change =-block_movement
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    lead_x_change =block_movement
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change =-block_movement
                    lead_x_change =0
                elif event.key==pygame.K_DOWN:
                    lead_y_change =block_movement 
                    lead_x_change =0
            #this makes snake move only while you press it
            #if event.type==pygame.KEYUP:
                #if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    #lead_x_change=0
                #if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    #lead_y_change=0
            
        if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
            gameOver=True
        
        lead_x+=lead_x_change
        #if lead_x<0:
            #lead_x=display_width
        #if lead_x>display_width:
            #lead_x=0
        lead_y+=lead_y_change
        #if lead_y<0:
            #lead_y=display_height
        #if lead_y>display_height:
            #lead_y=0    
        gameDisplay.fill(grey)
        Apple_size=10#bigger when using bigger apple
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,Apple_size,Apple_size])

        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        snake(block_size,snakeList)
        pygame.display.update()
        
        if lead_x==randAppleX and lead_y==randAppleY:
            randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength+=1
        #to be used for striking bigger apple
        #if lead_x>=randAppleX and lead_x<=randAppleX+Apple_size:
            #if lead_y>=randAppleY and lead_y<=randAppleY+Apple_size:
                #randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
                #randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
                #snakeLength+=1                
            
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()