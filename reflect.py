import pygame,sys
pygame.init()
#the resolution is 1200x600
screen = pygame.display.set_mode([1200,600])
doraemon = pygame.image.load("doraemon.jpg")
doraemon2= pygame.image.load("doraemon2.jpg")
color=[255,255,255]
screen.fill(color)
x,y = 0,0
x_speed = 5
y_speed = 90
direction =1
while 1:
	pygame.draw.rect(screen,color,[x,y,120,90],0)
	x = x + x_speed
	if direction > 0 :
		screen.blit(doraemon,[x,y])
	else :
		screen.blit(doraemon2,[x,y])
	if x > screen.get_width()-120 or x < 0:
		x_speed = - x_speed
		direction = - direction
		pygame.draw.rect(screen,color,[x,y,120,90],0)
		y = y + y_speed
	if y > screen.get_height()-90 :
		y = 0
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.time.delay(15)
	