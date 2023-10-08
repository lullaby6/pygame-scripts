import pygame, sys, random;from pygame import *;pygame.init();window = pygame.display.set_mode((700, 400));x = 0;y = 0;h = 35; w = 25;xa = 100;ya = 100;wa = 20;ha = 50
while True:
	window.fill((200, 200, 200))
	for event in pygame.event.get():
		if event.type == QUIT:pygame.quit();sys.exit()
		elif event.type == pygame.KEYDOWN: 
			if event.key == K_ESCAPE:pygame.quit();sys.exit()
	pygame.draw.rect(window,(25, 25, 25),(x, y, w, h))
	pygame.draw.rect(window,(25, 25, 25),(xa, ya, wa, ha))
	x, y = pygame.mouse.get_pos()
	if (x + w > xa and y + h > ya and x + w < xa + wa and y + h < ya + ha) or (x > xa and y + h > ya and (not(x > xa + wa or y > ya + ha))) or (x + wa > xa and y > ya and ya + ha > y and (not(x + w > xa + wa))) or (xa == x and y == y) or (x < xa and x + w > xa + wa and ((y < ya and y + h > ya) or (y > ya and y + h > ya and (not(ya + ha < y))))) or (x < xa and x + w > xa and y < ya and y + h > ya + ha):print("Colisionando")
	print("hola")	
	pygame.display.update()
	