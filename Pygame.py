import pygame, sys
from pygame import *

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Title")
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(60)
	