# Zeit wird gezählt
import pygame, math, random, time
from pygame.locals import *

pygame.init()

#bg = (255, 255, 255)
bg = (20, 20, 50)
black = (0, 0, 0)

diff_bg = (255, 255, 0)

ww = 800
wh = 600

fenster = pygame.display.set_mode((ww, wh), FULLSCREEN)
pygame.mouse.set_visible(0)
fenster.fill(bg)
pygame.display.set_caption("Don't hit the balls!!!")

pygame.display.update()

spieler = pygame.image.load("player_1.png")
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

angle_rot = random.randint(0, 360)
angle_grün = random.randint(0, 360)
angle_blau = random.randint(0, 360)


bilder_bälle = [ball_rot, ball_grün, ball_blau]
bälle = [rot_rect, grün_rect, blau_rect]
angle_bälle = [angle_rot, angle_grün, angle_blau]

#print(angle_rot)
#print(angle_grün)
#print(angle_blau)

angle_player = 0
pr_player = "false"
pr_player_left = "false"
pr_player_right = "false"

mvsp = 3.5 # Movespeed
mvsp_bälle = 4
spawn_count = 150

zeit_zaehler = 0

clock = pygame.time.Clock()
fps = 50
time_count = 0
difficult = "Normal"


x = 1
x2 = 1
end = 0

# Intro-loop
while x2 == 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                x = 0
                x2 = 0

            if event.key == K_SPACE:
                x2 = 0

            if event.key == K_DOWN and difficult != "Easy":
                if difficult == "Hard":
                    difficult = "Normal"
                else:
                    difficult = "Easy"

            if event.key == K_UP and difficult != "Hard":
                if difficult == "Easy":
                    difficult = "Normal"
                else:
                    difficult = "Hard"

    if difficult == "Easy":
        spawn_count = 250
        diff_bg = (0, 255, 0)

    if difficult == "Normal":
        spawn_count = 150
        diff_bg = (255, 255, 0)

    if difficult == "Hard":
        diff_bg = (255, 0, 0)
        spawn_count = 50

    fenster.fill((255, 175, 0))
    text_title = pygame.font.SysFont(None, 125)
    text_subt  = pygame.font.SysFont(None, 60)
    text_subt2 = pygame.font.SysFont(None, 25)

    title = text_title.render("Hello", True, black)
    fenster.blit(title, (50, 50))

    subt1 = text_subt.render("Press 'Space' to start.", True, black, (255, 250, 0))
    subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
    subt3 = text_subt.render(difficult, True, black, diff_bg)
    subt4 = text_subt2.render("Use arrow keys to change.", True, black)
    subt5 = text_subt.render("Hardness:", True, black)
    
    fenster.blit(subt1, (100, 325))
    fenster.blit(subt2, (100, 400))
    fenster.blit(subt3, (500, 100))
    fenster.blit(subt4, (500, 210))
    fenster.blit(subt5, (500, 20))#(325, 100))

    pygame.draw.polygon(fenster, black, ((500, 90), (525, 65), (550, 90)))
    pygame.draw.polygon(fenster, black, ((500, 167), (525, 192), (550, 167)))

    pygame.display.update()

#print(spawn_count)

# Main-loop

while x == 1:
    time_count += 1
    #print(angle_player)
    
    if pr_player_left == "true":
        angle_player += 5
    if pr_player_right == "true":
        angle_player -= 5

    if pr_player == "true":
        b = math.cos(math.radians(angle_player)) * mvsp # Berechnet die Länge der am angle anliegenden Kathete.
        
        a = math.sin(math.radians(angle_player)) * mvsp # Brechnet die Länge der des angles gegenüberliegenden Seite.

        #if player.top >= 0 and player.bottom <= wh:
        player.top += round(b)
        #if player.left >= 0 and player.right <= ww:
        player.left += round(a)
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            x = 0
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                x = 0
            if event.key == K_UP or event.key == K_w:
                pr_player = "true"

            if event.key == K_LEFT or event.key == K_a:
                pr_player_left = "true"

            if event.key == K_RIGHT or event.key == K_d:
                pr_player_right = "true"

        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_w:
                pr_player = "false"
            if event.key == K_LEFT or event.key == K_a:
                pr_player_left = "false"
            if event.key == K_RIGHT or event.key == K_d:
                pr_player_right = "false"

# BÄLLE BEWEGEN SICH HIER:######################################################

    for i in range(len(bälle)):
        zaehler = 0
        if bälle[i].top  <= 0 or bälle[i].bottom >= wh:
            zaehler += 1
            #print("hallo")
            #print(angle_bälle)
            #print(angle_bälle[i])

            
            angle_bälle[i] = 360 - angle_bälle[i]

            b = math.cos(math.radians(angle_bälle[i])) * mvsp_bälle # Berechnet die Länge der am angle anliegenden Kathete.
            a = math.sin(math.radians(angle_bälle[i])) * mvsp_bälle
            
            bälle[i].left += b
            bälle[i].top += a
            #print(b)
            #print(a)
            #print(angle_bälle[i])
            #print()
            

        if bälle[i].left <= 0 or bälle[i].right >= ww:
            zaehler += 1
            #print("hallo")
            #print(angle_bälle[i])
            angle_bälle[i] = 180 - angle_bälle[i]

            b = math.cos(math.radians(angle_bälle[i])) * mvsp_bälle # Berechnet die Länge der am angle anliegenden Kathete.
            a = math.sin(math.radians(angle_bälle[i])) * mvsp_bälle 
            
            bälle[i].left += b
            bälle[i].top += a
            #print(angle_bälle[i])
            #print()

        if zaehler == 0:
            b = math.cos(math.radians(angle_bälle[i])) * mvsp_bälle # Berechnet die Länge der am angle anliegenden Kathete.
            a = math.sin(math.radians(angle_bälle[i])) * mvsp_bälle

            bälle[i].left += b
            bälle[i].top += a

#        if bälle[i].top  <= 0 or bälle[i].bottom >= wh:
#            print("hallo")
#            angle_bälle[i] = 360 - angle_bälle[i]
#            print(angle_bälle[i])
#            print()
#
#        if bälle[i].left <= 0 or bälle[i].right >= ww:
#            print("hallo")
#            angle_bälle[i] = 180 - angle_bälle[i]
#            print(angle_bälle[i])
#            print()

        #if bälle[i].right >= ww:
        #    angle_bälle[i] = 180 - angle_bälle[i]

        #if bälle[i].bottom >= wh:
        #    angle_bälle[i] = 360 - angle_bälle[i]
        

################################################################################

    #bilder_bälle = [ball_rot, ball_grün, ball_blau]
    #bälle = [rot_rect, grün_rect, blau_rect]
    #angle_bälle = [angle_rot, angle_grün, angle_blau]        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    fenster.fill(bg)
                
    player_rect = spieler.get_rect().center
    player_neu = pygame.transform.rotate(spieler, angle_player-180)
    player_neu.get_rect().center = player_rect

    player_rect = spieler.get_rect() 
    player_center_neu = player_neu.get_rect().center
    player_center_diff = (player.center[0]-player_center_neu[0], player.center[1]-player_center_neu[1])    

    for i in range(len(bälle)):
        fenster.blit(bilder_bälle[i], bälle[i])

    #fenster.blit(ball_rot, rot_rect)
    #fenster.blit(ball_grün, grün_rect)
    #fenster.blit(ball_blau, blau_rect)

    fenster.blit(player_neu, player_center_diff)

    zeit_zaehler += 1
    if zeit_zaehler >= spawn_count:
        bälle.append(pygame.Rect(random.randint(0, ww-ball_rot.get_rect().width), random.randint(0, wh-ball_rot.get_rect().height), ball_rot.get_rect().width, ball_rot.get_rect().height))
        bilder_bälle.append(bilder_bälle[random.randint(0,2)])
        angle_bälle.append(random.randint(0, 360))
        
        #print("Hallo")
        #mvsp_bälle += 0.25
        #print(mvsp_bälle)
        zeit_zaehler = 0

    for element in bälle:
        if player.colliderect(element):
            x = 0
            end = 1

    pygame.display.update()
    clock.tick(fps)

    if not player.colliderect(0, 0, ww, wh):
        x = 0
        end = 1
    
# Ende:
if end == 1:
    x = 1
    while x == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x = 0
        fenster.fill((255, 255, 50))

        basicFont = pygame.font.SysFont(None, 100)#150)
        text = basicFont.render("You loose. =(", True, black)
        text_time = text_subt.render("time: " + str(round(time_count/fps, 2)) + " seconds.", True, black)
        text_Esc = text_subt.render("Press 'Esc' to exit.", True, black)

        fenster.blit(text, (50, 100))
        fenster.blit(text_time, (75, 300))
        fenster.blit(text_Esc, (75, 500))
        pygame.display.update()

pygame.quit()


#
