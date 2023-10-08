import pygame, sys, random
from pygame import *

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game of Life")

cels = []
id = 0
h = 0

pause = -1

mouse_x = 0
mouse_y = 0
click = 0


class Cel:
	def __init__(self, x, y, id, state):
		self.state = state
		self.tempstate = state
		self.x = x
		self.y = y
		self.id = id
		self.ul = False
		self.up = False
		self.ur = False
		self.le = False
		self.ri = False
		self.dl = False
		self.do = False
		self.dr = False
		self.c = (10, 10, 10)
		self.v = 0
	
	def display(self):
		if self.state:pygame.draw.rect(window, self.c, (self.x, self.y, 10, 10))
		
		if click == 1 and mouse_x > self.x and mouse_y > self.y and mouse_x < self.x+10 and mouse_y < self.y+10: 
			self.temps = False
			self.tempstate = False
		if click == 2 and mouse_x > self.x and mouse_y > self.y and mouse_x < self.x+10 and mouse_y < self.y+10: 
			self.temps = True
			self.tempstate = True
			
	def move(self):
		for obj in cels:
			if not self.id == obj.id:
				if obj.x-10== self.x and obj.y-10== self.y:
					if obj.state:
						if self.ul == False:
							self.v += 1
							self.ul = True
					else:
						if self.ul == True:
							self.v -= 1
							self.ul = False
				if obj.x == self.x and obj.y-10== self.y:
					if obj.state:
						if self.up == False:
							self.v += 1
							self.up = True
					else:
						if self.up == True:
							self.v -= 1
							self.up = False
				if obj.x+10== self.x and obj.y-10== self.y:
					if obj.state:
						if self.ur == False:
							self.v += 1
							self.ur = True
					else:
						if self.ur == True:
							self.v -= 1
							self.ur = False
				if obj.x-10== self.x and obj.y == self.y:
					if obj.state:
						if self.le == False:
							self.v += 1
							self.le = True
					else:
						if self.le == True:
							self.v -= 1
							self.le = False
				if obj.x+10== self.x and obj.y == self.y:
					if obj.state:
						if self.ri == False:
							self.v += 1
							self.ri = True
					else:
						if self.ri == True:
							self.v -= 1
							self.ri = False
				if obj.x-10== self.x and obj.y+10== self.y:
					if obj.state:
						if self.dl == False:
							self.v += 1
							self.dl = True
					else:
						if self.dl == True:
							self.v -= 1
							self.dl = False
				if obj.x == self.x and obj.y+10== self.y:
					if obj.state:
						if self.do == False:
							self.v += 1
							self.do = True
					else:
						if self.do == True:
							self.v -= 1
							self.do = False
				if obj.x+10== self.x and obj.y+10== self.y:
					if obj.state:
						if self.dr == False:
							self.v += 1
							self.dr = True
					else:
						if self.dr == True:
							self.v -= 1
							self.dr = False
						
		if self.v <= 1 or self.v >= 4: 
			self.tempstate = False
		if self.v == 3: 
			self.tempstate = True
		
	def update(self):
		self.state = self.tempstate
		
for y in range(25):
	for x in range(25):
		tempstate = False
		temprandom = random.randint(0, 6)
		if temprandom == 5:
			tempstate = True
		cels.append(Cel(x*10, y*10, id, tempstate))
		id += 1
		
while True:
	pygame.display.update()
	window.fill((255, 255, 255))
	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	for g in range(1, 50):
		pygame.draw.line(window, (200, 200, 200), (g*10, 0), (g*10, 500), 1)
		pygame.draw.line(window, (200, 200, 200), (0, g*10), (500, g*10), 1)
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == K_p: 
				pause *= -1
		if event.type == pygame.MOUSEBUTTONDOWN: 
			if event.button == 1: 
				click = 2
			if event.button == 3: 
				click = 1
		if event.type == pygame.MOUSEBUTTONUP: 
			click = 0
			
	h = 0
	for obj in cels:
		obj.display()
		h += 1
		if pause == -1: 
			obj.move()	
		if h == len(cels):
			for obj2 in cels:
				obj2.update()