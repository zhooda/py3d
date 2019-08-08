'''
py3d -> 3D graphics engine using pygame
'''

# ### IMPORTS
import pygame, sys, math

# ### PYGAME INIT
pygame.init()
w,h = 400,400
cx,cy = w//2,h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

# ### DEFINING VERTECIES & EDGES
verts = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
edges = (0, 1),(1, 2),(2, 3),(3, 0),(4, 5),(5, 6),(6, 7),(7, 4),(0, 4),(1, 5),(2, 6),(3, 7)

# ### WINDOW WHILE LOOP
while True:

	# clock tick time delta
	dt = clock.tick()/1000

	# event handler
	for event in pygame.event.get():

		# quit when user exits
		if event.type == pygame.QUIT:
			sys.exit()


	# screen fill white
	screen.fill((255,255,255))

	# drawing points
	for x,y,z in verts:

		# bringing everything closer to the "camera"
		z += 5

		# multiplier to make the depth illusion
		f = 200/z
		x,y = x*f,y*f

		pygame.draw.circle(screen, (0,0,0), (cx+int(x), cy+int(y)), 6)

	# drawing edges
	for edge in edges:

		points = []
		for x,y,z in (verts[edge[0]],verts[edge[1]]):
			z += 5
			f = 200/z
			x,y = x*f,y*f
			points += [(cx+int(x), cy+int(y))]
		pygame.draw.line(screen, (0, 0, 255), points[0], points[1], 1)
	# update screen
	pygame.display.flip()