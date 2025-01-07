from random import random
import pygame
from Brain import Brain


class Boid:
	def __init__(self):
		self.exist = True
		self.brain = Brain(2, (2, 4), 6, 6, random()/10)


	def process(self):
		pass


	def display(self, screen):
		width, height = screen.get_size()
		mx,my = pygame.mouse.get_pos()
		out = self.brain.process([mx,my])
		pygame.draw.circle(screen, (out[0]*255, out[1]*255, out[2]*255), (out[3]*width, out[4]*height), 10+out[5]*100)

		# death by mouse
		dist = ((mx-out[3]*width)**2 + (my-out[4]*height)**2)**0.5
		if dist < 10+out[5]*100:
			self.exist = False
	

	def mutate(self, mutate:float = 0) -> None:
		self.brain.mutate(mutate)
