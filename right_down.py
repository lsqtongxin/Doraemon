import pygame,sys
pygame.init()
#the resolution is 1200x600
screen = pygame.display.set_mode([1200,600])
doraemon = pygame.image.load("resources/images/doraemon.jpg")
doraemon2= pygame.image.load("resources/images/doraemon2.jpg")

screen.fill([255,255,255])
x,y = 0,0
x_speed = 5
y_spedd = 90
while 1:
	pygame.draw.rect(screen,[255,255,255],[x,y,120,90],0)
	x = x + x_speed
	if x > screen.get_width()-120 :
		x = -120
		y = y + y_spedd
	if y > screen.get_height()-90 :
		y = 0
	screen.blit(doraemon,[x,y])
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.time.delay(20)
