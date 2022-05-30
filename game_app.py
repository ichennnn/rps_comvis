#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:35:36 2022

@author: ichennnn
"""

import cv2
import time
import os

os.chdir('')

import HandTrackingModule as htm

import pygame
import random

# adjust size of screen cam
cw, ch = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, cw)
cap.set(4, ch)

# fps
cTime = 0
pTime = 0

# game controls
running = True
menu = True
new_game=False
playres = False

detector = htm.handDetector(detectionCon=0.75)
pygame.init()


# screen display
color_bg=(157,192,239)
color_orange=(255,128,0)
color_white=(255,255,255)
color_green=(14,162,68)
color_dgrey=(110,109,109)

w_font = pygame.font.SysFont('futura', 24, True)
w_font2 = pygame.font.SysFont('futura', 18, True)

s_width = 600
s_height = 500
screen = pygame.display.set_mode([s_width, s_height])
pygame.display.set_caption('Rock Paper Scissors')

fpsg=60
timer = pygame.time.Clock()
turn=0
moves = ['rock', 'paper', 'scissors']


def start_menu():
    screen.fill(color_bg)
    
    msg1=w_font.render(('Rock Paper Scissors'), True, color_white)
    screen.blit(msg1, (20, 20))
    msg11=w_font.render('Computer Vision Ver.', True, color_white)
    screen.blit(msg11, (20, 50))
    startimg=pygame.image.load('startimg.ico')
    screen.blit(startimg,(20,75))
    msg2=w_font.render('built by Irene Chen',True, color_white)
    screen.blit(msg2, (20, 150))
    
    pygame.draw.rect(screen, color_orange, [ 20,190, 560, 250],0, 5)
    msgex=w_font2.render('To play, make the hand gesture (rock, paper or scissor)',True, color_white)
    msgex2=w_font2.render('as shown below, then hit the ENTER key on keyboard',True, color_white)
    screen.blit(msgex,(30,200))
    screen.blit(msgex2,(30,220))
    r=pygame.image.load('rock.png')
    r = pygame.transform.scale(r, (220, 220))
    screen.blit(r, (-10,200))
    s = pygame.image.load('scissors.png')
    s= pygame.transform.scale(s, (220, 220))
    p = pygame.image.load('paper.png')
    p = pygame.transform.scale(p, (220, 220))
   
    or_txt = w_font2.render('OR',True,color_white)
    screen.blit(or_txt,(180,310))
    screen.blit(or_txt,(360,310))
    screen.blit(s, (375, 205))
    screen.blit(p, (200,215))
    r_txt = w_font.render('ROCK',True, color_white)
    p_txt = w_font.render('PAPER',True, color_white)
    s_txt = w_font.render('SCISSORS',True, color_white)
    screen.blit(p_txt, (240,400))
    screen.blit(s_txt, (400,400))
    screen.blit(r_txt, (45,400))
    
    msg4=w_font2.render('PRESS TAB on keyboard TO QUIT', True, color_white)
    screen.blit(msg4, (20, 470))
    
    msg3=w_font2.render('PRESS ENTER on keyboard TO START',True, color_white)
    msg4=w_font2.render('PRESS TAB on keyboard TO QUIT', True, color_white)
    screen.blit(msg3, (20, 450))
    screen.blit(msg4, (20, 470))

def win_lose(cmo, pmo):
    #res is w respect to the player
    if cmo == pmo:
        res = 'Drew'
    else:
        if pmo == 'rock':
            if cmo == 'scissors':
                res = 'Lost'
            else:
                res = 'Won'
        elif pmo == 'scissors':
            if cmo == 'rock':
                res = 'Lost'
            else:
                res = 'Won'
        else:
            #paper
            if cmo == "scissors":
                res = 'Lost'
            else:
                res = 'Won'
    return res

def blitMoves(cmo, pmo, res):
    screen.fill(color_bg)
    
    if cmo == 'rock':
        com=pygame.image.load('rock.png')
    elif cmo == 'scissors':
        com=pygame.image.load('scissors.png')
    else:
        com=pygame.image.load('paper.png')
    if pmo == 'rock':
        you=pygame.image.load('rock.png')
    elif pmo == 'scissors':
        you=pygame.image.load('scissors.png')
    else:
        you=pygame.image.load('paper.png')
    
    box_l = 243
    if res == 'Won':
        colorc = color_green
        box_l = 250
    elif res == 'Drew':
        colorc = color_orange
    else:
        colorc = color_dgrey
    pygame.draw.rect(screen, colorc, [ 210,390, 180, 70],0, 5)
    you = pygame.transform.scale(you, (200, 200))
    com = pygame.transform.scale(com, (200, 200))
    
    move_msg1=w_font.render(f"Computer Picked {cmo.upper()}", True, color_white)
    screen.blit(move_msg1,(20,100))
    screen.blit(com,(340,5))
    move_msg2 = w_font.render(f"You Picked {pmo.upper()}", True, color_white)
    screen.blit(move_msg2,(20,250))
    screen.blit(you,(335,185))
    wl_msg = w_font2.render(f"YOU {res.upper()}", True, color_white)
    # won 250, drew lost 243
    screen.blit(wl_msg,(box_l,410))
    ag_msg = w_font2.render('PRESS ENTER TO PLAY AGAIN or TAB TO QUIT',True
                            , color_white)
    screen.blit(ag_msg, (45, 470))
    
def rpsGame(pmo):
    #pick computers move
    global cmo
    global res
    cmo = moves[random.randint(0, len(moves)-1)]
    res = win_lose(cmo, pmo)
    return cmo, pmo, res

def makeYourMove():
    screen.fill(color_bg)
    rmk = w_font.render('MAKE YOUR MOVE', True, color_white)
    rmk2 = w_font2.render('To make your move by forming the hand gestures as shown',
                          True, color_white)
    rmk3 = w_font2.render('below (rock, paper or scissors) and hit ENTER to submit',
                          True, color_white)
    rmk4= w_font2.render('Note: Hand gestures should be made exactly like in diagram',
                         True, color_white)
    screen.blit(rmk, (180, 40))
    screen.blit(rmk2, (20, 90))
    screen.blit(rmk3, (20, 110))
    screen.blit(rmk4, (20, 150))
    pygame.draw.rect(screen, color_orange, [ 20,190, 560, 250],0, 5)

    r=pygame.image.load('rock.png')
    r = pygame.transform.scale(r, (220, 220))
    screen.blit(r, (-10,170))
    s = pygame.image.load('scissors.png')
    s= pygame.transform.scale(s, (220, 220))
    p = pygame.image.load('paper.png')
    p = pygame.transform.scale(p, (220, 220))
   
    or_txt = w_font2.render('OR',True,color_white)
    screen.blit(or_txt,(180,310))
    screen.blit(or_txt,(360,310))
    screen.blit(s, (375, 165))
    screen.blit(p, (200,175))
    r_txt = w_font.render('ROCK',True, color_white)
    p_txt = w_font.render('PAPER',True, color_white)
    s_txt = w_font.render('SCISSORS',True, color_white)
    screen.blit(p_txt, (240,380))
    screen.blit(s_txt, (400,380))
    screen.blit(r_txt, (45,380))
    
    msg4=w_font2.render('PRESS TAB on keyboard TO QUIT', True, color_white)
    screen.blit(msg4, (20, 470))

while running:
    timer.tick(fpsg)
    success, img = cap.read()
    screen.fill(color_bg)

    img = detector.findHand(img)
    all_lm = detector.findPosition(img, draw=False)
    if menu:
        start_menu()
    else:    
        makeYourMove()
        if new_game:
            if len(all_lm)!=0:
                # there is a hand detected
                if all_lm[16][2] > all_lm[13][2]:
                    # fourth finger down 
                    if all_lm[12][2] > all_lm[9][2]:
                        # third finger down
                        if all_lm[8][2] > all_lm[6][2]:
                            #second finger down
                            # rock
                            pmo = 'rock'
                    else:
                        # scissors
                        pmo = 'scissors'
                else:
                    #  = paper
                    pmo ='paper'
        if playres:
            blitMoves(cmo, pmo, res)
    
    #event handling
    for event in pygame.event.get():
        #exit
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                # hit tab  to quit all
                running = False
                cv2.waitKey(1000)
                cv2.destroyAllWindows()
            elif event.key == pygame.K_RETURN and (not menu) and (not playres):
                new_game=False
                cmo, pmo , res = rpsGame(pmo)
                playres = True
            elif event.key == pygame.K_RETURN and (playres):
                playres = False
                new_game=True
            elif event.key == pygame.K_RETURN:
                menu = False
                new_game=True
            
                
                
    # fps
    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime
    cv2.putText(img, "fps: "+str(fps), (460, 40), cv2.FONT_HERSHEY_PLAIN, 3,
              (255,0,0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    pygame.display.flip()

pygame.quit()
cv2.destroyAllWindows()
