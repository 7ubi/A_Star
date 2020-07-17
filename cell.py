import pygame
import random

pygame.init()

class Cell:
	def __init__(self, i, j, w, h):
		self.i = i
		self.j = j
		self.wi = w
		self.he = h
		self.g = 0
		self.h = 0
		self.f = 0

		self.isWall = False

		if(random.random() < 0.1):
			self.isWall = True

		self.previous = None

		self.neighbors = []

	def addNeighbors(self, cells, rows, cols):
		for k in range(-1, 2): 
			for m in range(-1, 2): 
				if (k == 0 and m == 0):
					continue
				if (k == -1 and self.i+k < 0):
					continue
				if (m == -1 and self.j+m < 0):
					continue
				if (k == 1 and self.i+k > rows - 1):
					continue
				if (m == 1 and self.j+m > cols - 1):
					continue

				self.neighbors.append(cells[self.i + k][self.j + m]);
      
    

	def show(self, screen, c):
		if self.isWall:
			pygame.draw.rect(screen, pygame.Color(0, 0, 0), (self.i * self.wi, self.j * self.he, self.wi, self.he))
		else:
			pygame.draw.rect(screen, c, (self.i * self.wi, self.j * self.he, self.wi, self.he))