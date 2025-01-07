from Node import *

class Brain:
	def __init__(self, Input: int, Process: tuple[int,int], Output: int, Memory: int, mutate:float = 0):
		self.I: list[Node] = [Node() for _ in range(Input)]
		self.M: list[Node] = [Node() for _ in range(Memory)]
		self.P: list[list[Node]] = [[] for _ in range(Process[0])]
		self.P[0] = [Node(self.M, mutate) for _ in range(Process[1])] #add I
		for i in range(1, Process[0]):
			self.P[i] = [Node(self.P[i-1], mutate) for _ in range(Process[1])]
		self.O: list[Node] = [Node(self.P[-1], mutate) for _ in range(Output)]
		for node in self.M:
			node.update(self.P[-1], mutate)


	def mutate(self,mutate:float) -> None:
		for node in self.I+self.O+self.M:
			node.mutate(mutate)
		for layer in self.P:
			for node in layer:
				node.mutate(mutate)


	def process(self, input: list[float]) -> list[float]:
		for node,value in zip(self.I,input):
			node.value = value
		for layer in self.P:
			for node in layer:
				node.process()
		for node in self.M:
			node.process()
		out = []
		for node in self.O:
			node.process(True)
			out.append(node.value)
		return out
	

	def __repr__(self) -> str:
		return f'Input: {[node.value for node in self.I]}\n'\
			f'Process: {[node.value for node in self.P[-1]]}\n'\
			f'Output: {[node.value for node in self.O]}\n'\
			f'Memory: {[node.value for node in self.M]}'
