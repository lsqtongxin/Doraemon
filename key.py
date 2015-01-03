import pygame
from pygame.locals import *
SCREEN=[800,600]
screen = pygame.display.set_mode(SCREEN,0,32)
COLOR = [255,255,255]
screen.fill(COLOR)
doraemon = pygame.image.load("resources/images/doraemon.jpg")
x,y = 120,90
x_offset,y_offset = 0,0
while True :
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_a:
				x_offset = -5
			elif event.key == K_d:
				x_offset = +5
			elif event.key == K_w:
				y_offset = -5
			elif event.key == K_s:
				y_offset = +5
		
		elif event.type == KEYUP:
			x_offset = 0
			y_offset = 0
		x+= x_offset
		y+= y_offset
		screen.blit(doraemon,[x,y])
		pygame.display.flip()




