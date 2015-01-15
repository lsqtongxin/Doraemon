import pygame,sys
pygame.init()
screen=pygame.display.set_mode([800,600])
screen.fill([125,125,125])
Doraemon=pygame.image.load("resources/images/Doraemon.jpg")
screen.blit(Doraemon,[50,50])
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
