import pygame
import sys
import math
from cell import Cell

pygame.init()

width, height = 500, 500
rows, cols = 50, 50
w, h = width / rows, height / cols


openList = []
closedList = []

def newCellSet():
	global cells
	cells = [[Cell(x, y, w, h) for x in range(rows)] for y in range(cols)]

	for i in range(rows):
	    for j in range(cols):
	        cells[i][j].addNeighbors(cells, rows, cols)

	global start
	start = cells[0][0]
	start.isWall = False
	global end
	end = cells[rows - 1][cols - 1]
	end.isWall = False

	global openList 
	openList = []
	global closedList
	closedList = []
	global path
	path = []
newCellSet()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("a*")


def dist(x1, y1, x2, y2):
    return math.dist([x1, y1], [x2, y2])


def heuristic(c, end):
    return math.dist([c.i, c.j], [end.i, end.j])

def drawCells():
	screen.fill(pygame.Color(0, 0, 0))
	for i in range(rows):
		for j in range(cols):
			cells[i][j].show(screen, pygame.Color(255, 255, 255))
	for c in openList:
			c.show(screen, pygame.Color(204, 254, 255))

	for c in closedList:
		c.show(screen, pygame.Color(135, 239, 255))

	for c in path:
		c.show(screen, pygame.Color(99, 255, 151))
	start.show(screen, pygame.Color(255, 148, 148))
	end.show(screen, pygame.Color(255, 0, 0))




def aStar():
	global openList 
	openList = []
	global closedList
	closedList = []
	openList.append(start)

	while len(openList) > 0:
		current = openList[0]
		for i in range(len(openList)):
			if(openList[i].f < current.f):
				current = openList[i]
		if (current == end):
			mainLoop(s=start, e=end)
		
		openList.remove(current)
		closedList.append(current)

		for n in current.neighbors:
			if not n in closedList and not n.isWall:
				tempG = current.g + dist(current.i, current.j, n.i, n.j)

				newPath = False

				if n in openList:
					if(tempG < n.g):
						n.g = tempG
						newPath = True
				else:
					n.g = tempG
					openList.append(n)
					newPath = True

				if newPath:
					n.previous = current
					n.h = heuristic(n, end)
					n.f = n.g + n.h

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		global path
		path = []
		temp = current
		path.append(temp)
		while temp.previous != None:
			path.append(temp)
			temp = temp.previous

		drawCells()
		pygame.display.update()
	print("no solution")


def mainLoop(s=None, e=None):
	if s == None and e == None: 
		global start
		start = cells[0][0]
		start.isWall = False
		global end
		end = cells[rows - 1][cols - 1]
		end.isWall = False
	global path
	path = []
	if end.previous != None:
		temp = end
		path.append(temp)
		while temp.previous != None:
			path.append(temp.previous)
			temp = temp.previous

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				aStar()
			if key[pygame.K_s]:
				x, y = pygame.mouse.get_pos()
				j = int(x / width * rows)
				i = int(y / height * cols)
				start = cells[i][j]
			if key[pygame.K_e]:
				x, y = pygame.mouse.get_pos()
				j = int(x / width * rows)
				i = int(y / height * cols)
				end = cells[i][j]
			if key[pygame.K_r]:
				newCellSet()

			mouse = pygame.mouse.get_pressed()
			if mouse[0]:
				x, y = pygame.mouse.get_pos()
				j = int(x / width * rows)
				i = int(y / height * cols)
				cells[int(i)][int(j)].isWall = True
			if mouse[2]:
				x, y = pygame.mouse.get_pos()
				j = int(x / width * rows)
				i = int(y / height * cols)
				cells[int(i)][int(j)].isWall = False


		drawCells()
		pygame.display.update()


mainLoop()
