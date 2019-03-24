# Zeit wird gezaehlt
import pygame, math, random, time
from pygame.locals import *

import PIL.Image as Image
import numpy as np


def GameStart(model,options,optimizer,ceriterion):

    obs = options.observation

    pygame.init()

    bg = (255, 255, 255)
    # bg = (20, 20, 50)
    black = (0, 0, 0)

    diff_bg = (255, 255, 0)

    ww = 800
    wh = 600

    fenster = pygame.display.set_mode((ww, wh))
    pygame.mouse.set_visible(0)
    fenster.fill(bg)
    pygame.display.set_caption("Don't hit the balls!!!")

    pygame.display.update()

    spieler = pygame.image.load("player_1.png")
    # Startposition player
    player_x = ww / 2
    player_y = wh / 2
    player = pygame.Rect(player_x, player_y, spieler.get_rect().width, spieler.get_rect().height)

    # pygame.mixer.music.load("noise.mp3")
    ########################################################################################################################################################################

    difficult = "Normal"

    game = 1



    while game == 1:
        ball_rot = pygame.image.load("ball_rot.png")
        rot_rect = pygame.Rect(random.randint(0, ww-ball_rot.get_rect().width), random.randint(0, wh-ball_rot.get_rect().height), ball_rot.get_rect().width, ball_rot.get_rect().height)

        ball_gruen = pygame.image.load("ball_gruen.png")
        gruen_rect = pygame.Rect(random.randint(0, ww-ball_gruen.get_rect().width), random.randint(0, wh-ball_gruen.get_rect().height), ball_gruen.get_rect().width, ball_gruen.get_rect().height)

        ball_blau = pygame.image.load("ball_blau.png")
        blau_rect = pygame.Rect(random.randint(0, ww-ball_blau.get_rect().width), random.randint(0, wh-ball_blau.get_rect().height), ball_blau.get_rect().width, ball_blau.get_rect().height)

        # explosion = pygame.image.load("explosion.png")

        angle_rot = random.randint(0, 360)
        angle_gruen = random.randint(0, 360)
        angle_blau = random.randint(0, 360)


        bilder_baelle = [ball_rot, ball_gruen, ball_blau]
        baelle = [rot_rect, gruen_rect, blau_rect]
        angle_baelle = [angle_rot, angle_gruen, angle_blau]

        #print(angle_rot)
        #print(angle_gruen)
        #print(angle_blau)

        angle_player = 0
        pr_player = "false"
        pr_player_left = "false"
        pr_player_right = "false"

        mvsp = 3.5 # Movespeed
        mvsp_baelle = 4
        spawn_count = 150

        zeit_zaehler = 0

        clock = pygame.time.Clock()
        fps = 50
        time_count = 0

        x = 1
        x2 = 0
        end = 0
        action = 5
        reward = 1
        # Main-loop

        while x == 1:
            time_count += 1
            #print(angle_player)
            
            if pr_player_left == "true":
                angle_player += 5
            if pr_player_right == "true":
                angle_player -= 5

            if pr_player == "true":
                b = math.cos(math.radians(angle_player)) * mvsp # Berechnet die Laenge der am angle anliegenden Kathete.
                
                a = math.sin(math.radians(angle_player)) * mvsp # Brechnet die Laenge der des angles gegenueberliegenden Seite.

                #if player.top >= 0 and player.bottom <= wh:
                player.top += round(b)
                #if player.left >= 0 and player.right <= ww:
                player.left += round(a)
            
            '''
            We take image data here
            and get inputs based on states (images,reward,terminal)
            '''

            # agent_ouput = model.forward(out)
            # print(agent_ouput)
            # result.save('i.png')
            # exit()

            pygame.display.update()

            '''
            Number of Actions: 6
            0 : KeyUp + KeyLeft
            1 : KeyUp + KeyRight
            2 : KeyUp
            3 : KeyLeft
            4 : KeyRight
            5 : DoNothing
            '''

            if action == 0:
                pr_player_left = "true"
                pr_player = "true"
                pr_player_right = "false"

            if action == 1:
                pr_player_left = "false"
                pr_player = "true"
                pr_player_right = "true"

            if action == 2:
                pr_player_left = "false"
                pr_player = "true"
                pr_player_right = "false"

            if action == 3:
                pr_player_left = "true"
                pr_player = "false"
                pr_player_right = "false"

            if action == 4:
                pr_player_left = "false"
                pr_player = "false"
                pr_player_right = "true"

            if action == 5:
                pr_player_left = "false"
                pr_player = "false"
                pr_player_right = "false"

        # BaeLLE BEWEGEN SICH HIER:######################################################

            for i in range(len(baelle)):
                zaehler = 0
                if baelle[i].top  <= 0 or baelle[i].bottom >= wh:
                    zaehler += 1
                    #print("hallo")
                    #print(angle_baelle)
                    #print(angle_baelle[i])

                    
                    angle_baelle[i] = 360 - angle_baelle[i]

                    b = math.cos(math.radians(angle_baelle[i])) * mvsp_baelle # Berechnet die Laenge der am angle anliegenden Kathete.
                    a = math.sin(math.radians(angle_baelle[i])) * mvsp_baelle
                    
                    baelle[i].left += b
                    baelle[i].top += a
                    #print(b)
                    #print(a)
                    #print(angle_baelle[i])
                    #print()
                    

                if baelle[i].left <= 0 or baelle[i].right >= ww:
                    zaehler += 1
                    #print("hallo")
                    #print(angle_baelle[i])
                    angle_baelle[i] = 180 - angle_baelle[i]

                    b = math.cos(math.radians(angle_baelle[i])) * mvsp_baelle # Berechnet die Laenge der am angle anliegenden Kathete.
                    a = math.sin(math.radians(angle_baelle[i])) * mvsp_baelle 
                    
                    baelle[i].left += b
                    baelle[i].top += a
                    #print(angle_baelle[i])
                    #print()

                if zaehler == 0:
                    b = math.cos(math.radians(angle_baelle[i])) * mvsp_baelle # Berechnet die Laenge der am angle anliegenden Kathete.
                    a = math.sin(math.radians(angle_baelle[i])) * mvsp_baelle

                    baelle[i].left += b
                    baelle[i].top += a

            fenster.fill(bg)
                        
            player_rect = spieler.get_rect().center
            player_neu = pygame.transform.rotate(spieler, angle_player-180)
            player_neu.get_rect().center = player_rect

            player_rect = spieler.get_rect() 
            player_center_neu = player_neu.get_rect().center
            player_center_diff = (player.center[0]-player_center_neu[0], player.center[1]-player_center_neu[1])    

            for i in range(len(baelle)):
                fenster.blit(bilder_baelle[i], baelle[i])

            #fenster.blit(ball_rot, rot_rect)
            #fenster.blit(ball_gruen, gruen_rect)
            #fenster.blit(ball_blau, blau_rect)

            fenster.blit(player_neu, player_center_diff)

            zeit_zaehler += 1
            if zeit_zaehler >= spawn_count:
                baelle.append(pygame.Rect(random.randint(0, ww-ball_rot.get_rect().width), random.randint(0, wh-ball_rot.get_rect().height), ball_rot.get_rect().width, ball_rot.get_rect().height))
                bilder_baelle.append(bilder_baelle[random.randint(0,2)])
                angle_baelle.append(random.randint(0, 360))
                
                #print("Hallo")
                #mvsp_baelle += 0.25
                #print(mvsp_baelle)
                zeit_zaehler = 0

            for element in baelle:
                if player.colliderect(element):
                    # fenster.blit(explosion, (player.left-explosion.get_rect().width/2+12, player.top-explosion.get_rect().height/2+12))
                    pygame.display.update()
                    # pygame.mixer.music.play()
                    # time.sleep(1)
                
                    x = 0
                    end = 1
                    player.left = ww/2 - player.width/2
                    player.top = wh/2 - player.height/2

            pygame.display.update()
            clock.tick(fps)


            if not player.colliderect(0, 0, ww, wh):            
                x = 0
                end = 1
                player.left = ww/2 - player.width/2
                player.top = wh/2 - player.height/2

            pygame.event.pump()
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            agent_input = Image.fromarray(image_data).resize((400,300)).convert(mode='L')
            agent_input = np.asarray(agent_input).astype(np.float32)
            # agent_input = Image.fromarray(np.asarray(image_data).astype(np.float32))
            # agent_input = agent_input.rotate(-90, expand=1 ).resize((400,300)).convert('L')
            agent_ouput,obs = train_model(agent_input,model,optimizer,ceriterion,obs)
            action = np.argmax(agent_ouput)
            # print(action)
            # print(obs)
            pygame.display.update()

            
        # Ende:
        if end == 1:
            x = 1
            # while x == 1:
            #     for event in pygame.event.get():
            #         if event.type == KEYDOWN:
            #             x = 0

                # fenster.fill((255, 255, 50))

                # basicFont = pygame.font.SysFont(None, 100)#150)
                # text = basicFont.render("You hit a ball. =(", True, black)
                # text_time = text_subt.render("time: " + str(round(time_count/fps, 2)) + " seconds.", True, black)
                # text_Esc = text_subt.render("Press any key to continue.", True, black)

                # fenster.blit(text, (50, 100))
                # fenster.blit(text_time, (75, 300))
                # fenster.blit(text_Esc, (75, 500))
                # pygame.display.update()



    ########################################################################################################################################################################

    pygame.quit()



def train_model(agent_input,model,optimizer,ceriterion,obs):

    if obs > 0:
        obs -= 1
        action = model.get_action_randomly()
        return action,obs

    else:
        exit()

#
