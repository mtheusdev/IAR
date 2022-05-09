import pygame
from random import random
from constants import *

array_colors = []
for r in RGB_VALUES:
    for g in RGB_VALUES:
        for b in RGB_VALUES:
            array_colors.append((r, g, b))

def setRandomPostitionItems(database_content, items, N):
    for item in database_content:
        x = y = 0
        while(items[x][y] != []):
            x = int(random() * N)
            y = int(random() * N)
        items[x][y] = item
    return items

def initAndConfiguratePyGame():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("ANT CLUSTERING - DATA")
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    return screen, clock

def run(iterations, map_type, agents, WIDTH, HEIGHT, items, N):
    screen, clock = initAndConfiguratePyGame()
    start = 0
    half = iterations // 2
    end = iterations - 1

    for i in range(iterations):
        for agent in agents:
            agent.walkAndInteract()
            if not i % 10:
                agent.updatealpha()
        if not i%5:
            for x in range(N):
                for y in range(N):
                    color = (0, 0, 0)
                    if items[x][y] != []:
                        label = items[x][y][2]
                        color = array_colors[int(label+9)]
                    pygame.draw.rect(screen,
                                    color,
                                    [(MARGIN + WIDTH) * y + MARGIN,
                                    (MARGIN + HEIGHT) * x + MARGIN,
                                    WIDTH,
                                    HEIGHT])
            clock.tick(100)
        pygame.display.flip()
        print(i, start, half, end)
        if i == start:
            pygame.image.save(screen, f'./map{map_type}_start.jpg')
        elif i == half:
            pygame.image.save(screen, f'./map{map_type}_half.jpg')
        elif i == end:
            pygame.image.save(screen, f'./map{map_type}_end.jpg')
    
    pygame.quit()