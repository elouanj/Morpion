# -*- coding: utf-8 -*-
from pygame import *
from pygame.locals import *

init()
   
def placerRond(pos_souris):
	minLarg = 20
	maxLarg = 152
	minHaut = 20
	maxHaut = 152
	posX = 20
	posY = 20
	for i in range (0,9):
		if pos_souris[0] > minLarg and  pos_souris[0] < maxLarg and pos_souris[1] > minHaut and  pos_souris[1] < maxHaut:
			fenetre.blit(rond, (posX, posY))
		minLarg += 152
		maxLarg += 152
		posX += 152
		if minLarg > 324 and maxLarg > 456:
			minLarg = 20
			maxLarg = 152
			minHaut += 152
			maxHaut += 152
			posX = 20
			posY += 152

def placerCroix(pos_souris):
	minLarg = 20
	maxLarg = 152
	minHaut = 20
	maxHaut = 152
	posX = 20
	posY = 20
	for i in range (0,9):
		if pos_souris[0] > minLarg and  pos_souris[0] < maxLarg and pos_souris[1] > minHaut and  pos_souris[1] < maxHaut:
			fenetre.blit(croix, (posX, posY))
		minLarg += 152
		maxLarg += 152
		posX += 152
		if minLarg > 324 and maxLarg > 456:
			minLarg = 20
			maxLarg = 152
			minHaut += 152
			maxHaut += 152
			posX = 20
			posY += 152
			
def victoire():
	print("bite")

joueur=1
fenetre = display.set_mode((640, 480))
rectangle1 = Rect(0,0,456,20)
rectangle2 = Rect(0,152,456,20)
rectangle3 = Rect(0,304,456,20)
rectangle4 = Rect(0,456,456,20)
rectangle5 = Rect(0,0,20,456)
rectangle6 = Rect(152,0,20,456)
rectangle7 = Rect(304,0,20,456)
rectangle8 = Rect(456,0,20,476)
white=(255,255,255)

rond = image.load("rond.png")
rond = rond.convert()

croix = image.load("croix.png")
croix = croix.convert()

continu = True
while (continu):
	draw.rect(fenetre,white,rectangle1)
	draw.rect(fenetre,white,rectangle2)
	draw.rect(fenetre,white,rectangle3)
	draw.rect(fenetre,white,rectangle4)
	draw.rect(fenetre,white,rectangle5)
	draw.rect(fenetre,white,rectangle6)
	draw.rect(fenetre,white,rectangle7)
	draw.rect(fenetre,white,rectangle8)
	display.flip()
	for p_event in event.get():
		if p_event.type == QUIT:
			continu = False
		if p_event.type == MOUSEBUTTONDOWN :
			print(joueur)
			pos_souris = mouse.get_pos()
			if joueur == 1:
				placerRond(pos_souris)
			if joueur == 2:
				placerCroix(pos_souris)
			victoire()
			joueur += 1
			if joueur > 2:
				joueur = 1
