import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
screen.fill([255,255,255])
pygame.display.set_caption("Doraemon Game")
doraemon = pygame.image.load("resources/images/doraemon.jpg")
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	x,y = pygame.mouse.get_pos()
	x -= doraemon.get_width()/2
	y -= doraemon.get_height()/2	
	screen.blit(doraemon,(x,y))
	pygame.display.flip();
