# Zeit wird gezaehlt
import pygame, math, random, time
from pygame.locals import *

import PIL.Image as Image
import numpy as np
import random
import torch
import torch.nn as nn
from torch.autograd import Variable

import os, sys
# os.environ["SDL_VIDEODRIVER"] = "dummy"

def GameStart(model,options,optimizer,ceriterion):

    num_games_played = 0

    obs = options.observation

    pygame.init()

    bg = (255, 255, 255)
    # bg = (20, 20, 50)
    black = (0, 0, 0)

    diff_bg = (255, 255, 0)

    ww = 400
    wh = 300

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
    reward = 1


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
            # pygame.draw.rect(fenster,(0, 0, 0), (10,10, ww-20, wh-20),3)

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

            reward = 1

            for element in baelle:
                if player.colliderect(element):
                    # fenster.blit(explosion, (player.left-explosion.get_rect().width/2+12, player.top-explosion.get_rect().height/2+12))
                    pygame.display.update()
                    # pygame.mixer.music.play()
                    # time.sleep(1)
                
                    x = 0
                    end = 1
                    reward = -4
                    player.left = ww/2 - player.width/2
                    player.top = wh/2 - player.height/2

            pygame.display.update()
            clock.tick(fps)

            

            if not player.colliderect(20, 20, ww-40, wh-40):            
                x = 0
                end = 1
                reward = -4
                player.left = ww/2 - player.width/2
                player.top = wh/2 - player.height/2

            pygame.event.pump()
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            agent_input = Image.fromarray(image_data).resize((150,112)).convert(mode='L')
            # agent_input.save("a.png")
            # exit()
            agent_input = np.asarray(agent_input).astype(np.float32)
            # agent_input = Image.fromarray(np.asarray(image_data).astype(np.float32))
            # agent_input = agent_input.rotate(-90, expand=1 ).resize((400,300)).convert('L')
            agent_ouput,obs = step_model(agent_input,model,optimizer,ceriterion,obs,reward,action,options)
            action = np.argmax(agent_ouput)
            # print(action)
            # print(obs)
            pygame.display.update()

            
        # Ende:
        if end == 1:
            x = 1
            # reset reward
            reward = 1
            num_games_played += 1
            print("time: " + str(round(time_count/fps, 2)) + " seconds.")

            if options.mode == "Train" and num_games_played % options.save_checkpoint_freq == 0:
                print("saving model",num_games_played)

                torch.save(model.state_dict(),options.model_name)

            if num_games_played == options.max_episode:
                print("Max episodes reached! exiting.")
                exit()
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



def step_model(agent_input,model,optimizer,ceriterion,obs,reward,prev_action,options):

    # print("reward",reward,"obs",obs)


    if reward == -1:
        terminal = True
        if model.epsilon > options.final_e:
            delta = (options.init_e - options.final_e)/options.exploration
            model.epsilon -= delta
    else:
        terminal = False

    if obs > 0:
        obs -= 1
        action = model.get_action_randomly()
        

        # saving previous action response
        action_set = np.zeros(model.actions, dtype=np.float32)
        action_set[prev_action] = 1.0
        model.store_transition(agent_input, action_set, reward, terminal)
        

        return action,obs

    else:
        optimizer.zero_grad()
        # total_reward += options.gamma**model.time_step * r

        action_set = np.zeros(model.actions, dtype=np.float32)
        action_set[prev_action] = 1.0
        model.store_transition(agent_input, action_set, reward, terminal)


        action = model.get_action()
        model.increase_time_step()

        if options.mode == "Train":

            minibatch = random.sample(model.replay_memory,options.batch_size)
            
            # if len(model.screens) < 8:
            #     state_batch = np.array([data[0] for data in minibatch])    
            # else:
            #     model.screens.pop(0)
            #     model.screens.append(agent_input)
            #     state_batch = np.array(model.screens)
            
            state_batch = np.array([data[0] for data in minibatch])
            action_batch = np.array([data[1] for data in minibatch])
            reward_batch = np.array([data[2] for data in minibatch])
            next_state_batch = np.array([data[3] for data in minibatch])
            state_batch_var = Variable(torch.from_numpy(state_batch))
            next_state_batch_var = Variable(torch.from_numpy(next_state_batch))
            

            q_value_next = model.forward(next_state_batch_var)
            # exit()
            q_value = model.forward(state_batch_var)
            
            y = reward_batch.astype(np.float32)
            
            
            max_q, _ = torch.max(q_value_next, dim=1)
            # print(max_q.shape)
            # exit()
            for i in range(options.batch_size):
                if not minibatch[i][4]:
                    y[i] += options.gamma*max_q.data[i]

            y = Variable(torch.from_numpy(y))

            action_batch_var = Variable(torch.from_numpy(action_batch))

            if model.use_cuda:
                action_batch_var = action_batch_var.cuda()
                y = y.cuda()
            
            q_value = torch.sum(torch.mul(action_batch_var, q_value), dim=1)


            loss = ceriterion(q_value, y)
            loss.backward()
            optimizer.step()

        return action,obs
    
#
