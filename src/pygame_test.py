## run pip install pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((900,450)) #Resolution: width, height
pygame.display.set_caption('Blackjack') #Title
clock = pygame.time.Clock()

table_surface = pygame.image.load('assets/table.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(table_surface, (0,0)) #block image transfer (one image on another image)      0,0 is at top left corner of box screen      
    pygame.display.update()
    clock.tick(60) #Framerate
    
    