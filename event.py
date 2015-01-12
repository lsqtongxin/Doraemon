import pygame,time
from pygame.locals import *

pygame.init()
SCREEN_SIZE = [480,240]
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = ["Event List"]

while True:
	event = pygame.event.wait()
	event_text.append(str(event)+"_time"+str(time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))))

	if event.type == QUIT:
		exit()
	
	screen.fill(0)
	y = 0

	for text in event_text:
		if y >=SCREEN_SIZE[1]:
			screen.fill(0)
			y=0
		else :
			screen.blit(font.render(text,True,(0,255,0)),(0,y))
			y+=font_height
	pygame.display.flip()


