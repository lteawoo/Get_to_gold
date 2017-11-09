# Import library
import random
import object
import pygame
from pygame.locals import *

# Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False]
crystals = []
genTimer = 100
score = 0

# Load image
player = pygame.image.load("resources/pig.png")
crystalImg = pygame.image.load("resources/crystal.png")
crystalImg = pygame.transform.scale(crystalImg, (50,50))

# player setup
playerPos = [width/2 - player.get_size()[0]/2, height - player.get_size()[1]]

# Loop
while 1:
    # 화면 그려지기 전에 클리어
    screen.fill((255, 255, 255))

    # player 그리기
    screen.blit(player, playerPos)

    # crystal 그리기
    if genTimer == 0 :
        crystalObj = object.Crystal(random.randint(0, width - crystalImg.get_size()[0]), 0 - crystalImg.get_size()[1], 0.1)
        crystals.append(crystalObj)
        genTimer = 100 - random.randint(0, 20)

    index = 0
    for crystal in crystals :
        if crystal.y + crystalImg.get_size()[1] >= height :
            crystals.pop(index)

        #크리스탈 떨어짐
        crystal.y = crystal.y + crystal.speed
        crystal.speed = crystal.speed + 0.005

        #player 충돌 처리
        playerRect = pygame.Rect(player.get_rect())
        playerRect.left = playerPos[0]
        playerRect.top = playerPos[1]

        crystalRect = pygame.Rect(crystalImg.get_rect())
        crystalRect.left = crystal.x
        crystalRect.top = crystal.y
        if crystalRect.colliderect(playerRect):
            score += 1
            crystals.pop(index)

        index += 1

    for crystal in crystals :
        screen.blit(crystalImg, [crystal.x, crystal.y])

    # Hud 그리기
    font = pygame.font.Font(None, 24)
    scoreText = font.render(str(score), True, (0, 0, 0))
    scoreRect = scoreText.get_rect()
    scoreRect.topright = [width/2, 0]
    screen.blit(scoreText, scoreRect)

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
    if keys[1] and playerPos[0] - 1 != 0 :
        playerPos[0] -= 1
    elif keys[2] and playerPos[0] + player.get_size()[0] + 1 != width :
        playerPos[0] += 1