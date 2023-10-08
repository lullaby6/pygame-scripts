import pygame, sys, random;from pygame import *;pygame.init();window = pygame.display.set_mode((425, 375));pygame.display.set_caption("Snake");snake = [0, 0];apple = [12, 7];x = [1, 2, 3];y = [7, 7, 7];frameCount = 0;game = True;pd = snake;pd2 = snake
while True:
	pygame.display.update();frameCount += 1;window.fill((255, 255, 255))
	for g in range(1, 17):pygame.draw.line(window, (200, 200, 200), (g*25, 0), (g*25, 475), 1);pygame.draw.line(window, (200, 200, 200), (0, g*25), (475, g*25), 1)
	pygame.draw.rect(window,(25, 25, 25),(apple[0]*25, apple[1]*25, 25, 25))
	for size in range(len(x)):pygame.draw.rect(window,(25, 25, 25),(x[size]*25, y[size]*25, 25, 25))
	if x[len(x)-1] < 0 or x[len(x)-1] > 16 or y[len(x)-1] < 0 or y[len(x)-1] > 14:game = False
	if (frameCount % 60) == 0:
		if x[len(x)-2] == x[len(x)-1] + snake[0] and y[len(x)-2] == y[len(x)-1] + snake[1]:snake = pd
		x.append(x[len(x)-1] + snake[0]);y.append(y[len(y)-1] + snake[1])
		for size in range(len(x)-1):
			if x[size] == x[len(x)-1] and y[size] == y[len(x)-1] and len(x) > 2:game = False
			if x[size] == apple[0] and y[size] == apple[1]:apple = [random.randint(0, 16), random.randint(0, 14)]
		x.pop(0);y.pop(0);snake = pd2
	if x[len(x)-1] == apple[0] and y[len(y)-1] == apple[1]:x.append(x[len(x)-1]);y.append(y[len(y)-1]);apple = [random.randint(0, 16), random.randint(0, 14)]
	for event in pygame.event.get():
		if event.type == QUIT:pygame.quit();sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				if (not(snake[0] == 1)):pd = snake;snake = [-1, 0];pd2 = snake
			elif event.key == K_RIGHT or event.key == K_d:
				if (not(snake[0] == -1)):pd = snake;snake = [1, 0];pd2 = snake
			elif event.key == K_UP or event.key == K_w:
				if (not(snake[1] == 1)):pd = snake;snake = [0, -1];pd2 = snake
			elif event.key == K_DOWN or event.key == K_s:
				if (not(snake[1] == -1)):pd = snake;snake = [0, 1];pd2 = snake
			elif event.key == K_ESCAPE:pygame.quit();sys.exit()
			if pd[0] == 0 and pd[1] == 0: pd = snake
	if game == False:x = [1, 2, 3];y = [7, 7, 7];snake = [0, 0];apple = [12, 7];frameCount = 0;game = True;pd = snake;pd2 = snake