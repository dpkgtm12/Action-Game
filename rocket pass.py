hj='3.jpg'
mc='2.png'
kd="1.jpg"
import pygame as p
from pygame.locals import *
from sys import exit
import random as r
p.init()
screen=p.display.set_mode((0,0),0,32)
l=p.image.load(hj).convert()
b=p.image.load(mc).convert_alpha()
n=p.image.load(kd).convert()
l=p.transform.scale(l,(750,1450))
b=p.transform.scale(b,(100,60))
n=p.transform.scale(n,(750,1450))
lst=[l,n]
y=700
x=200
z=0
m=n
while True:
	for event in p.event.get():
		if event.type==QUIT:
			exit()
	px=750
	py=r.randint(400,1000)
	pd=1450-py
	ty=py-r.randint(100,300)
	while True:
		screen.blit(m,(0,0))
		a=p.mouse.get_pressed()
		if a[0]==1:
			screen.blit(b,(x,y))
			y-=20
		elif y>1400:
			exit()
		else:
			screen.blit(b,(x,y))
			y+=10
		if y<0:
			exit()
		if px<=-40:
			px=700
			py=r.randint(400,1400)
			pd=1450-py
			ty=py-r.randint(150,300)
		px=px-5
		if z==300:
			m=lst[0]
		elif z==600:
			z==0
			m=lst[1]
		p.draw.rect(screen, (100,50,0),p.Rect(px,py,50,pd))
		p.draw.rect(screen,(100,50,0),p.Rect(px,0,50,ty))
		if px<=300 and px>200  and y<ty or px<=300 and px>150 and y>py-25:
			exit()
		z+=1
		p.display.update()
	