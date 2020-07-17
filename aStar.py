import pygame
import sys
import math
from cell import Cell

pygame.init()

width, height = 500, 500
rows, cols = 50, 50
w, h = width / rows, height / cols

cells = [[Cell(x, y, w, h) for x in range(rows)] for y in range(cols)]

openList = []
closedList = []
path = []

start = cells[0][0]
end = cells[rows - 1][cols - 1]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("a*")


def dist(x1, y1, x2, y2):
    return math.dist([x1, y1], [x2, y2])


def heuristic(c, end):
    return math.dist([c.i, c.j], [end.i, end.j])


def aStar():
    openList.append(start)
    while len(openList) > 0:
        current = openList[0]
        for i in range(len(openList)):
            if(openList[i].f < current.f):
                current = openList[i]

        if (current == end):
            print("done")
          
            mainLoop()

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

        screen.fill(pygame.Color(0, 0, 0))

        for i in range(rows):
            for j in range(cols):
                cells[i][j].show(screen, pygame.Color(255, 255, 255))

        for c in openList:
            c.show(screen, pygame.Color(0, 255, 0))

        for c in closedList:
            c.show(screen, pygame.Color(255, 0, 0))

        path = []
        temp = current
        path.append(temp)
        while temp.previous != None:
            path.append(temp)
            temp = temp.previous

        for c in path:
            c.show(screen, pygame.Color(0, 0, 255))

        pygame.display.update()
    print("no solution")


def mainLoop():
	path = []
	if end.previous != None:
		temp = end
		path.append(temp)
		while temp.previous != None:
			print(temp.previous.i)
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

		screen.fill(pygame.Color(0, 0, 0))
		for i in range(rows):
			for j in range(cols):
				cells[i][j].show(screen, pygame.Color(255, 255, 255))
		for c in openList:
		    c.show(screen, pygame.Color(0, 255, 0))

		for c in closedList:
			c.show(screen, pygame.Color(255, 0, 0))
		for c in path:
			c.show(screen, pygame.Color(0, 0, 255))

		pygame.display.update()

for i in range(rows):
    for j in range(cols):
        cells[i][j].addNeighbors(cells, rows, cols)

mainLoop()
