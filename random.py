import pygame,random
pygame.init()
screen = pygame.display.set_mode([1200,600])
doraemon = pygame.image.load("resources/images/doraemon.jpg")
color=[255,255,255]
screen.fill(color)
x,y = 0,0
while 1:
	pygame.draw.rect(screen,color,[x,y,120,90],0)
	x = random.randint(0,1200)
	y = random.randint(0,600)
	screen.blit(doraemon,[x,y])
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.time.delay(1000)
