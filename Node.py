from random import random
import math

class Node:
	def __init__(self, read: list['Node'] = [], mutate:float = 0, parent:'Node' = None):
		self.read: list[Node] = read
		self.weights: list[float] = parent.weights[:] if parent else [0]*len(read)
		self.bias: float = parent.bias if parent else 0
		self.value: float = 0
		if mutate!=0: self.mutate(mutate)


	def update(self, read: list['Node'], mutate:float = 0) -> None:
		self.read = read
		self.weights = [0]*len(read)
		if mutate!=0: self.mutate(mutate)	


	def mutate(self, mutate:float) -> None:
		self.weights = [w + mutate*(random()-random()) for w in self.weights]
		self.bias += mutate*(random()-random())


	def process(self, sigmoid:bool = False) -> None:
		self.value = self.bias + sum([n.value*w for n,w in zip(self.read, self.weights)])
		if sigmoid:
			self.value = 1 / (1 + math.exp(-self.value))
		else:
			self.value = max(0, self.value)