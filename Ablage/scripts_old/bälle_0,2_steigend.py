
import pygame, sys, math, random
from pygame.locals import *

pygame.init()

#bg = (255, 255, 255)
bg = (40, 40, 60)

ww = 1000
wh = 800

fenster = pygame.display.set_mode((ww, wh))
fenster.fill(bg)
pygame.display.set_caption("Bälle")

pygame.display.update()

spieler = pygame.image.load("spieler.png")
# Startposition player
player_x = ww / 2
player_y = wh / 2
player = pygame.Rect(player_x, player_y, spieler.get_rect().width, spieler.get_rect().height)


ball_rot = pygame.image.load("ball_rot.png")
rot_rect = pygame.Rect(random.randint(0, ww-ball_rot.get_rect().width), random.randint(0, wh-ball_rot.get_rect().height), ball_rot.get_rect().width, ball_rot.get_rect().height)

ball_grün = pygame.image.load("ball_grün.png")
grün_rect = pygame.Rect(random.randint(0, ww-ball_grün.get_rect().width), random.randint(0, wh-ball_grün.get_rect().height), ball_grün.get_rect().width, ball_grün.get_rect().height)

ball_blau = pygame.image.load("ball_blau.png")
blau_rect = pygame.Rect(random.randint(0, ww-ball_blau.get_rect().width), random.randint(0, wh-ball_blau.get_rect().height), ball_blau.get_rect().width, ball_blau.get_rect().height)

winkel_rot = random.randint(0, 360)
winkel_grün = random.randint(0, 360)
winkel_blau = random.randint(0, 360)


bilder_bälle = [ball_rot, ball_grün, ball_blau]
bälle = [rot_rect, grün_rect, blau_rect]
winkel_bälle = [winkel_rot, winkel_grün, winkel_blau]

#print(winkel_rot)
#print(winkel_grün)
#print(winkel_blau)

winkel_player = 0
pr_player = "false"
pr_player_left = "false"
pr_player_right = "false"

mvsp = 3.5 # Movespeed
mvsp_bälle = 4

zeit_zaehler = 0

clock = pygame.time.Clock()

while True:
    #print(winkel_player)
    
    if pr_player_left == "true":
        winkel_player += 5
    if pr_player_right == "true":
        winkel_player -= 5

    if pr_player == "true":
        b = math.cos(math.radians(winkel_player)) * mvsp # Berechnet die Länge der am Winkel anliegenden Kathete.
        
        a = math.sin(math.radians(winkel_player)) * mvsp # Brechnet die Länge der des Winkels gegenüberliegenden Seite.

        #if player.top >= 0 and player.bottom <= wh:
        player.top += round(b)
        #if player.left >= 0 and player.right <= ww:
        player.left += round(a)
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            x = 0
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                pr_player = "true"

            if event.key == K_LEFT:
                pr_player_left = "true"

            if event.key == K_RIGHT:
                pr_player_right = "true"

        if event.type == KEYUP:
            if event.key == K_UP:
                pr_player = "false"
            if event.key == K_LEFT:
                pr_player_left = "false"
            if event.key == K_RIGHT:
                pr_player_right = "false"

# BÄLLE BEWEGEN SICH HIER:######################################################

    for i in range(len(bälle)):
        zaehler = 0
        if bälle[i].top  <= 0 or bälle[i].bottom >= wh:
            zaehler += 1
            #print("hallo")
            #print(winkel_bälle)
            #print(winkel_bälle[i])

            
            winkel_bälle[i] = 360 - winkel_bälle[i]

            b = math.cos(math.radians(winkel_bälle[i])) * mvsp_bälle # Berechnet die Länge der am Winkel anliegenden Kathete.
            a = math.sin(math.radians(winkel_bälle[i])) * mvsp_bälle
            
            bälle[i].left += b
            bälle[i].top += a
            #print(b)
            #print(a)
            #print(winkel_bälle[i])
            #print()
            

        if bälle[i].left <= 0 or bälle[i].right >= ww:
            zaehler += 1
            #print("hallo")
            #print(winkel_bälle[i])
            winkel_bälle[i] = 180 - winkel_bälle[i]

            b = math.cos(math.radians(winkel_bälle[i])) * mvsp_bälle # Berechnet die Länge der am Winkel anliegenden Kathete.
            a = math.sin(math.radians(winkel_bälle[i])) * mvsp_bälle 
            
            bälle[i].left += b
            bälle[i].top += a
            #print(winkel_bälle[i])
            #print()

        if zaehler == 0:
            b = math.cos(math.radians(winkel_bälle[i])) * mvsp_bälle # Berechnet die Länge der am Winkel anliegenden Kathete.
            a = math.sin(math.radians(winkel_bälle[i])) * mvsp_bälle

            bälle[i].left += b
            bälle[i].top += a

#        if bälle[i].top  <= 0 or bälle[i].bottom >= wh:
#            print("hallo")
#            winkel_bälle[i] = 360 - winkel_bälle[i]
#            print(winkel_bälle[i])
#            print()
#
#        if bälle[i].left <= 0 or bälle[i].right >= ww:
#            print("hallo")
#            winkel_bälle[i] = 180 - winkel_bälle[i]
#            print(winkel_bälle[i])
#            print()

        #if bälle[i].right >= ww:
        #    winkel_bälle[i] = 180 - winkel_bälle[i]

        #if bälle[i].bottom >= wh:
        #    winkel_bälle[i] = 360 - winkel_bälle[i]
        

################################################################################

    #bilder_bälle = [ball_rot, ball_grün, ball_blau]
    #bälle = [rot_rect, grün_rect, blau_rect]
    #winkel_bälle = [winkel_rot, winkel_grün, winkel_blau]        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    fenster.fill(bg)
                
    player_rect = spieler.get_rect().center
    player_neu = pygame.transform.rotate(spieler, winkel_player-180)
    player_neu.get_rect().center = player_rect

    player_rect = spieler.get_rect() 
    player_center_neu = player_neu.get_rect().center
    player_center_diff = (player.center[0]-player_center_neu[0], player.center[1]-player_center_neu[1])    

    for i in range(len(bälle)):
        fenster.blit(bilder_bälle[i], bälle[i])

    for element in bälle:
        if player.colliderect(element):
            print("Game over!!! ={")

    #fenster.blit(ball_rot, rot_rect)
    #fenster.blit(ball_grün, grün_rect)
    #fenster.blit(ball_blau, blau_rect)

    fenster.blit(player_neu, player_center_diff)

    zeit_zaehler += 1
    if zeit_zaehler == 150:

        bälle.append(pygame.Rect(random.randint(0, ww-ball_rot.get_rect().width), random.randint(0, wh-ball_rot.get_rect().height), ball_rot.get_rect().width, ball_rot.get_rect().height))
        bilder_bälle.append(bilder_bälle[random.randint(0,2)])
        winkel_bälle.append(random.randint(0, 360))
        
        #print("Hallo")
        #mvsp_bälle += 0.25
        #print(mvsp_bälle)
        zeit_zaehler = 0
    
    pygame.display.update()
    clock.tick(40)
    
    

#
