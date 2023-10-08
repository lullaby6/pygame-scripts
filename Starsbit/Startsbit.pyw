import pygame, sys, random
from pygame import *
import math, time
pygame.init()

window = pygame.display.set_mode((1000, 560))
pygame.display.set_caption("Startsbit")
icon = pygame.image.load('data/icon.png')
pygame.display.set_icon(icon)

height = 560
width = 1000

bat = 0
pl = 2

pause = 1
game = 1
change = 1

deltatime = 0

fx = 0
fy = 0

dist = 0
c1 = 0
c2 = 0
div = False


vibrate = 0; vibrate2 = False; v_d = 0; v_t = 0; tx = 0; ty = 0
def vibrateF(x, y, a, b):
	global vibrate2; global tx; global ty; global v_t; global v_d; global vibrate
	if vibrate2 == False: tx += x; ty += y; vibrate2 = True
	if v_d < b: v_d += 1
	else: tx = 0; ty = 0; vibrate2 = False; v_d = 0; v_t += 1
	if v_t == a: ty = 0; tx = 0; vibrate2 = False; vibrate = 0; v_d = 0; v_t = 0
	if v_t == 2: x *= -1;y *= -1

class Player:
	def __init__(self, id):
		self.x = 100;self.y = height/2-30/2
		self.f = 1
		self.s = 10
		self.c = (215, 215, 215)
		self.up = False;self.up2 = False
		self.down = False;self.down2 = False
		self.right = False;self.right2 = False
		self.left = False;self.left2 = False
		self.sp = 0.35
		self.sxr = 2;self.sxl = 2;self.syu = 2;self.syd = 2
		self.b = 0
		self.id = id
		self.state = True
		self.image = pygame.image.load("data/shf1.png")
		self.angle = 0
		self.imagerotate = pygame.transform.rotate(self.image, self.angle)
		self.dge = False
		self.dup = 0;self.dup2 = 0
		self.ddown = 0;self.ddown2 = 0
		self.dleft = 0;self.dleft2 = 0
		self.dright = 0;self.dright2 = 0
		self.cleft = 97;self.cright = 100;self.cup = 119;self.cdown = 115
		self.cfa = 99;self.cshot = 118;self.crot = 98
		if self.id == 2:
			self.x = width - 100
			self.f = self.f * -1
			self.image = pygame.image.load("data/shf2.png")
			self.cleft = 276;self.cright = 275;self.cup = 273;self.cdown = 274
			self.cfa = 47;self.cshot = 46;self.crot = 44
	def display(self):
		self.imagerotate = pygame.transform.rotate(self.image, self.angle)
		window.blit(self.imagerotate, (-fx + width / 2 + (tx + (self.x))-15, -fy + height / 2 + (ty + (self.y))-10))
	def move(self):
		if self.b > 0:
			self.b += 1 
			if self.b >= 16:
				self.b = 0
		if self.right == True:
			self.right2 = True
			if self.sxr < 8:
				self.sxr += self.sp 
			self.x += self.sxr 
		elif self.right2 == True:
			if self.sxr > 2:
				self.sxr -= self.sp 
			else:
				self.right2 = False
				self.sxr = 2
			self.x += self.sxr 
		if self.left == True:
			self.left2 = True
			if self.sxl < 8:
				self.sxl += self.sp 
			self.x -= self.sxl 
		elif self.left2 == True:
			if self.sxl > 2:
				self.sxl -= self.sp 
			else:
				self.left2 = False
				self.sxl = 2
			self.x -= self.sxl 		
		if self.up == True:
			self.up2 = True
			if self.syu < 8:
				self.syu += self.sp 
			self.y -= self.syu 
		elif self.up2 == True:
			if self.syu > 2:
				self.syu -= self.sp 
			else:
				self.up2 = False
				self.syu = 2
			self.y -= self.syu 			
		if self.down == True:
			self.down2 = True
			if self.syd < 8:
				self.syd += self.sp 
			self.y += self.syd 
		elif self.down2 == True:
			if self.syd > 2:
				self.syd -= self.sp 
			else:
				self.down2 = False
				self.syd = 2
			self.y += self.syd 
		if self.f == 1:
			if self.x + 25 > width*2:
				self.x = width*2 - 25
			if self.x - 5 < -width:
				self.x = -width + 5
		else:
			if self.x + 15 > width*2:
				self.x = width*2 - 15
			if self.x - 15 < -width:
				self.x = -width + 15
		if self.y + 20 > height*2:
			self.y = height*2 - 20
		if self.y - 10 < -height:
			self.y = -height + 10		
		if self.dge == True:
			if self.angle < 360:
				self.angle += 25
			elif self.angle >= 360:
				self.angle = 0
				self.dge = False	
		if self.dup == 1:
			if self.dup2 < 15:
				self.dup2 +=1
			else:
				self.dup = 0
				self.dup2 = 0
		if self.dup == 2:
			self.dup2 = 0
			self.dup = 3
		if self.dup >= 3:
			self.syu = 30
			if self.dup2 < 2:
				self.dup2 += 1
			else:
				self.up2 = True
				self.syu = 8
				self.dup = 0
				self.dup2 = 0			
		if self.dright == 1:
			if self.dright2 < 15:
				self.dright2 +=1
			else:
				self.dright = 0
				self.dright2 = 0
		if self.dright == 2:
			self.dright2 = 0
			self.dright = 3
		if self.dright >= 3:
			self.sxr = 30
			if self.dright2 < 2:
				self.dright2 += 1
			else:
				self.sxr = 8
				self.dright = 0
				self.dright2 = 0
				
		if self.dleft == 1:
			if self.dleft2 < 15:
				self.dleft2 +=1
			else:
				self.dleft = 0
				self.dleft2 = 0
		if self.dleft == 2:
			self.dleft2 = 0
			self.dleft = 3
		if self.dleft >= 3:
			self.sxl = 30
			if self.dleft2 < 2:
				self.dleft2 += 1
			else:
				self.sxl = 8
				self.dleft = 0
				self.dleft2 = 0			
		if self.ddown == 1:
			if self.ddown2 < 15:
				self.ddown2 +=1
			else:
				self.ddown = 0
				self.ddown2 = 0
		if self.ddown == 2:
			self.ddown2 = 0
			self.ddown = 3
		if self.ddown >= 3:
			self.syd = 30
			if self.ddown2 < 2:
				self.ddown2 += 1
			else:
				self.down2 = True
				self.syd = 8
				self.ddown = 0
				self.ddown2 = 0
	def control(self):
		global change
		if event.type == pygame.KEYDOWN:
			if self.cleft == 0:
				self.cleft = event.key
				change = 1
			if self.cright == 0:
				self.cright = event.key
				change = 1
			if self.cup == 0:
				self.cup = event.key
				change = 1
			if self.cdown == 0:
				self.cdown = event.key
				change = 1
			if self.cfa == 0:
				self.cfa = event.key
				change = 1
			if self.cshot == 0:
				self.cshot = event.key
				change = 1
			if self.crot == 0:
				self.crot = event.key
				change = 1
			if event.key == self.cleft:
				if change == -1:
					self.cleft = 0
					change = 2
				else:
					self.left = True
					self.dleft += 1
			if event.key == self.cright:
				if change == -1:
					self.cright = 0
					change = 2
				else:
					self.right = True
					self.dright += 1
			if event.key == self.cup:
				if change == -1:
					self.cup = 0
					change = 2
				else:
					self.up = True
					self.dup += 1
			if event.key == self.cdown:
				if change == -1:
					self.cdown = 0
					change = 2
				else:
					self.down = True
					self.ddown += 1
			if event.key == self.cfa:
				if change == -1:
					self.cfa = 0
					change = 2
				else:
					self.f = self.f * -1
					if self.f == 1:self.image = pygame.image.load("data/shf1.png")
					else:self.image = pygame.image.load("data/shf2.png")
			if event.key == self.cshot and self.b == 0:
				if change == -1:
					self.cshot = 0
					change = 2
				else:
					bullets.append(Bullet(self.x+self.s/2*self.f, self.y, 20 * self.f, 0, self.id))
					self.b = 1
			if event.key == self.crot and self.dge == False:
				if change == -1:
					self.crot = 0
					change = 2
				else:
					self.dge = True
	def control0(self):
		if event.type == pygame.KEYUP:
			if event.key == self.cleft:
				self.left = False
			elif event.key == self.cright:
				self.right = False
			elif event.key == self.cup:
				self.up = False
			elif event.key == self.cdown:
				self.down = False
	def control3(self):
		if self.id == 0:
			self.x = width - 100
			self.f = self.f * -1
		self.id = 2
		if ((self.y - pla.y < 30 and self.y - pla.y > 0) or (pla.y - self.y < 30 and pla.y - self.y > 0)) and self.b == 0:
			bullets.append(Bullet(self.x+self.s/2*self.f, self.y, 20 * self.f, 0, self.id))
			self.b = 1
		if pla.y < self.y:
			if self.ddown == 0:
				self.up = True
				self.down = False
		else:
			if self.dup == 0:
				self.up = False
				self.down = True
		#if pla.x < self.x:
			#self.left = True
			#self.right = False
		#else:
			#self.left = False
			#self.right = True
		if pla.x > self.x:
			self.f = 1
			self.image = pygame.image.load("data/shf1.png")
		else:
			self.f = -1
			self.image = pygame.image.load("data/shf2.png")
		if (self.y - pla.y < 10 and self.y - pla.y > 0) or (pla.y - self.y < 10 and pla.y - self.y > 0):	
			if pla.x < self.x:
				self.left = True
				self.right = False
			else:
				self.left = False
				self.right = True			
		if math.hypot(self.x-pla.x, self.y-pla.y) < 40 and self.dge == False:
			self.dge = True
		for obj in bullets:
			if math.hypot(self.x-obj.x, self.y-obj.y) < 45 and self.dge == False and (not(obj.id == self.id)):
				self.dge = True
			#if math.hypot(self.x-obj.x, self.y-obj.y) > 300 and ((self.y - obj.y < 10 and self.y - obj.y > 0) or (pla.y - obj.y < 10 and pla.y - obj.y > 0)) and (not(obj.id == self.id)) and ((self.x < obj.x and obj.dx == -20) or (self.x > obj.x and obj.dx == 20)):
				#if self.y < pla.y:
					#self.ddown = 3
					#self.up = False
				#else:
					#self.dup = 3
					#self.down = False
	def exploit(self, d):
		if not d == 100:
			if d < 0:d = random.uniform(-7, -5)
			else: d = random.uniform(5, 7)
			bullets.append(Bullet(self.x + self.s/2, self.y - self.s, d, random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x - self.s/2, self.y - self.s, d, random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x + self.s/2, self.y + self.s, d, random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x - self.s/2, self.y + self.s, d, random.uniform(-2.5, 2.5), self.id))
			if self.f == 1:
				bullets.append(Bullet(self.x + self.s/2, self.y, d, random.uniform(-2.5, 2.5), self.id))
				bullets.append(Bullet(self.x + self.s/2+self.s, self.y, d, random.uniform(-2.5, 2.5), self.id))
			else:
				bullets.append(Bullet(self.x - self.s/2, self.y, d, random.uniform(-2.5, 2.5), self.id))
				bullets.append(Bullet(self.x - self.s/2-self.s, self.y, d, random.uniform(-2.5, 2.5), self.id))
		else:
			bullets.append(Bullet(self.x + self.s/2, self.y - self.s, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x - self.s/2, self.y - self.s, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x + self.s/2, self.y + self.s, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
			bullets.append(Bullet(self.x - self.s/2, self.y + self.s, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
			if self.f == 1:
				bullets.append(Bullet(self.x + self.s/2, self.y, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
				bullets.append(Bullet(self.x + self.s/2+self.s, self.y, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
			else:
				bullets.append(Bullet(self.x - self.s/2, self.y, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
				bullets.append(Bullet(self.x - self.s/2-self.s, self.y, random.uniform(-7, 7), random.uniform(-2.5, 2.5), self.id))
		self.state = False
		global vibrate
		vibrate = 1
		global game
		game = 0
	def reset(self):
		if self.id == 1:
			self.x = 100
			self.y = height/2-30/2
			self.f = 1
			self.image = pygame.image.load("data/shf1.png")
		else:
			self.x = width - 100
			self.y = height/2-30/2
			self.f = -1
			self.image = pygame.image.load("data/shf2.png")
		self.state = True
		self.sxr = 2;self.sxl = 2;self.syu = 2;self.syd = 2
		self.b = 0
		self.up = False;self.up2 = False
		self.down = False;self.down2 = False
		self.right = False;self.right2 = False
		self.left = False;self.left2 = False
		self.angle = 0
		self.dge = False
		self.dup = 0;self.dup2 = 0
		self.ddown = 0;self.ddown2 = 0
		self.dleft = 0;self.dleft2 = 0
		self.dright = 0;self.dright2 = 0
				
class Bullet:
	def __init__(self, x, y, dx, dy, id):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.s = 10
		self.c = (215, 215, 215)
		self.id = id
		self.c1 = 0
		self.c2 = 0
		self.dist = 0
		self.state = True
	def display(self):
		pygame.draw.rect(window, self.c, (-fx + width / 2 + (tx + (self.x)), -fy + height / 2 + (ty + (self.y)), self.s, self.s))
	def move(self):
		self.x += self.dx 
		self.y += self.dy 
		if math.hypot(self.x-pla.x, self.y-pla.y) < 20 and pla.state == True and (not(self.id == pla.id)) and pla.dge == False:
			pla.exploit(self.dx)
			bullets.remove(self)
		if math.hypot(self.x-pla2.x, self.y-pla2.y) < 20 and pla2.state == True and (not(self.id == pla2.id)) and pla2.dge == False:
			pla2.exploit(self.dx)
			bullets.remove(self)
		for obj in bullets:
			if not obj.id == self.id:
				if math.hypot(self.x-obj.x, self.y-obj.y) < 10 and pla.state == True and pla2.state == True:
					bullets.remove(self)
					bullets.remove(obj)
					global vibrate
					vibrate = 2
		if self.x > width*2 or self.x < -width:
			bullets.remove(self)
				
bullets = []
	
class Star:
	def __init__(self):
		global height
		global width
		self.v = random.uniform(0.05, 2)
		self.s = random.uniform(2.5, 7.5)
		self.d = 0
		self.rmd = random.randint(50, 100)
		self.r = random.uniform(0, 255)
		self.g = random.uniform(0, 255)
		self.b = random.uniform(0, 255)
		self.c = (self.r, self.g, self.b)
		self.ac = self.c
		self.y = random.uniform(-height, height*2)
		self.x = random.uniform(-width, width*2)
	def display(self):
		pygame.draw.rect(window, self.c, (-fx + width / 2 + (tx + (self.x)), -fy + height / 2 + (ty + (self.y)), self.s, self.s))
	def move(self):
		if self.d < self.rmd:
			self.d += 1 
		else:
			self.d = 0
			if self.c == self.ac:
				self.c = (255, 255, 255)
			else:
				self.c = self.ac
		self.x -= self.v 
		if self.x < -width:
			self.v = random.uniform(0.05, 2)
			self.s = random.uniform(2.5, 7.5)
			self.d = 0
			self.rmd = random.randint(50, 100)
			self.r = random.uniform(0, 255)
			self.g = random.uniform(0, 255)
			self.b = random.uniform(0, 255)
			self.c = (self.r, self.g, self.b)
			self.ac = self.c
			self.y = random.uniform(-height, height*2)
			self.x = width*2

stars = []
for x in range(360):
	stars.append(Star())

pla = Player(1)
pla2 = Player(2)

window.fill((0, 0, 15))
k = pygame.Surface((width, height), pygame.SRCALPHA)
k.fill((0, 0, 15, 100))

background = pygame.image.load("data/fill.png")

def reset():
	pla.reset()
	pla2.reset()
	global vibrate
	global game
	global cont
	global tx
	global ty
	tx = 0
	ty = 0
	vibrate = 0
	game = 1
	cont = 0
	for x in range(len(bullets)):
		if len(bullets) > 0:
			for obj in bullets:
				bullets.remove(obj)
			
clock = pygame.time.Clock()
cont = 0
fullscreen = 1
while True:
	#time.sleep(0.005)
	for event in pygame.event.get():
		if pause == 1:
			if pla.state == True: pla.control()
			if pla2.state == True and pl == 2: pla2.control()
		if pla.state == True: pla.control0()
		if pla2.state == True and pl == 2: pla2.control0()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			#print(event.key)
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == K_r:
				reset()
			elif event.key == K_p:
				pause *= -1
			elif event.key == 49:
				pl = 1
				reset()
			elif event.key == 50:
				pl = 2
				reset()
			elif event.key == 292:
				fullscreen *= -1
				if fullscreen == 1:pygame.display.set_mode((1000, 560))
				else:pygame.display.set_mode((1000, 560), FULLSCREEN)
			elif event.key == 51:
				if change == 1:
					change = -1
				elif change == -1:
					change = 1
	#print(change)
	#if pla.x > pla2.x:c1 = pla.x - pla2.x
	#elif pla.x < pla2.x:c1 = pla2.x - pla.x
	#if pla.y > pla2.y:c2 = pla.y - pla2.y
	#elif pla.y < pla2.y:c2 = pla2.y - pla.y
	#dist = math.sqrt((c1*c1)+(c2*c2))
	#dist = int(dist)
	#print(c1) 
	#print(c2) 
	#if c1 > 1000 or c2 > 500: pygame.draw.rect(window, (255, 255, 255), (500, 0, 2.5, 560));div = True
	#else: div = False		
	try:
		for obj in stars:
			if pause == 1: obj.move()
			obj.display()
		for obj in bullets:
			if pause == 1: obj.move()
			obj.display()
		if pla.state == True: pla.display()
		if pla2.state == True: pla2.display()
		if pause == 1:
			if pla2.state == True and pl == 1:
				pla2.control3()
			if pla.state == True: pla.move()
			if pla2.state == True: pla2.move()
		if vibrate == 1:
			vibrateF(random.randint(-20, 20), random.randint(-20, 20), 3, 4)
		if vibrate == 2:
			vibrateF(random.randint(-10, 10), random.randint(-10, 10), 2, 4)
		if math.hypot(pla.x-pla2.x, pla.y-pla2.y) < 20 and pause == 1 and pla.state == True and pla2.state == True:
			if pla.dge == False:
				pla.exploit(100)
			if pla2.dge == False:
				pla2.exploit(100)
			vibrate = 1
		if pla.state == True and pla2.state == True:
			fx = pla.x / 2 + pla2.x / 2
			fy = pla.y / 2 + pla2.y / 2
		if pla.state == True and pla2.state == False:
			fx = pla.x
			fy = pla.y
		if pla2.state == True and pla.state == False:
			fx = pla2.x
			fy = pla2.y
		#pygame.draw.rect(window, (215, 215, 215), (fx, fy, 10, 10))
		#pygame.draw.rect(window, (215, 215, 215), (-fx + width / 2 + fx, -fy + height / 2 +fy, 10, 10))
		if fx > width * 2 - width / 2:
			fx = width * 2 - width / 2
		if fx < -width + width / 2:
			fx = -width + width / 2
		if fy < -height + height / 2:
			fy = -height + height / 2
		if fy > height * 2 - height / 2:
			fy = height * 2 - height / 2
		if game == 0:
			if cont < 2500: cont += 10
			else: cont = 0;reset();game = 1
	except Exception as e:
		print(e)
	#deltatime = ((pygame.time.get_ticks() - bat) / 1000.0) + 1
	#bat = pygame.time.get_ticks()
	#print(deltatime)
	pygame.display.update()
	if pause == 1:
		pygame.mouse.set_visible(False)
		#window.blit(k, (0, 0))
		#window.blit(background, (0, 0))
	else:pygame.mouse.set_visible(True)	
	window.fill((0, 0, 15))
	clock.tick(60)