import pygame

pygame.init()
window= pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Try #1")
running=True
x=0
y=0
width=30
height=70
velocity=5
wBNW=pygame.mixer.Sound('wbnw.wav')
wBNW.play()
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    key= pygame.key.get_pressed()
    if key[pygame.K_w]:
        y-=velocity
    if key[pygame.K_a]:
        x-=velocity
    if key[pygame.K_s]:
        y+=velocity
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        x+=velocity
    window.fill((0,0,0))
    pygame.draw.rect(window,(200,0,200),(x,y,width,height))
    pygame.display.update()
pygame.quit()
