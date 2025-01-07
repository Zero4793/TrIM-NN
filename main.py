import pygame
import sys
import os
from copy import deepcopy
from Boid import *

# fix working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame and main screen
pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('TrIM NN - Evolution Sim')
clock = pygame.time.Clock()

def main():
	keyheld = set()
	game = Main(screen)

	while True:
		# Handle events
		keypressed = None
		events = pygame.event.get()
		for event in events:
			# Quit the game
			if event.type == pygame.QUIT:
				return
			# track held and pressed keys
			if event.type == pygame.KEYDOWN:
				keyheld.add(pygame.key.name(event.key))
				keypressed = pygame.key.name(event.key)
				if keypressed == 'escape':
					return
			if event.type == pygame.KEYUP and pygame.key.name(event.key) in keyheld:
				keyheld.remove(pygame.key.name(event.key))

		# update and render
		game.process(keyheld, keypressed)   
		screen.fill(0)
		game.display()
		pygame.display.flip() 
		clock.tick(60)


class Main:
	def __init__(self, screen):
		self.screen = screen
		self.boids = [Boid() for _ in range(64)]

	def process(self, keyheld, keypressed):
		for boid in self.boids:
			boid.process()
		self.boids = [boid for boid in self.boids if boid.exist]
		if len(self.boids) < 64:
			self.boids.append(deepcopy(self.boids[0]))
			self.boids[-1].exist = True
			self.boids[-1].mutate(0.5)

	def display(self):
		for boid in self.boids:
			boid.display(self.screen)
		# print(self.boids[1].brain)

main()
pygame.quit()
sys.exit()