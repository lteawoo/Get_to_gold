# Import library
import random
import pygame
from pygame.locals import *

# Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False]
crystals = [[random.randint(0, width), 0]]
genTimer = 100

# Load image
player = pygame.image.load("resources/pig.png")
crystalImg = pygame.image.load("resources/crystal.png")
crystalImg = pygame.transform.scale(crystalImg, (50,50))

playerpos = [width/2 - player.get_size()[0]/2, height - player.get_size()[1]]

# Loop
while 1:
    # 화면 그려지기 전에 클리어
    screen.fill((255, 255, 255))

    # player 그리기
    screen.blit(player, playerpos)

    # crystal 그리기
    if genTimer == 0 :
        crystals.append([random.randint(0, width), 0])
        genTimer = 100 - random.randint(0, 70)

    index = 0
    for crystal in crystals :
        if crystal[1] + crystalImg.get_size()[1] >= height :
            crystals.pop(index)
        crystal[1] += 1
        index += 1

    for crystal in crystals :
        screen.blit(crystalImg, crystal)

    # 화면 업데이트
    pygame.display.flip()

    # Timer
    genTimer -= 1;

    # Loop through the events
    for event in pygame.event.get() :
        # X버튼 이벤트 체크
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # 방향키 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            if event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_d:
                keys[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_d:
                keys[2] = False

    # Move player
    if keys[1] and playerpos[0] - 1 != 0 :
        playerpos[0] -= 1
    elif keys[2] and playerpos[0] + player.get_size()[0] + 1 != width :
        playerpos[0] += 1