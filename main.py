'''
py3d -> 3D graphics engine using pygame
'''

# ### IMPORTS
import pygame, sys, math
from camera import Cam, rotate2d

# ### PYGAME INIT
pygame.init()
w,h = 400,400
cx,cy = w//2,h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

# ### DEFINING VERTECIES & EDGES
verts = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
edges = (0, 1),(1, 2),(2, 3),(3, 0),(4, 5),(5, 6),(6, 7),(7, 4),(0, 4),(1, 5),(2, 6),(3, 7)

# faces = (0,1,2,3),(4,5,6,7),

cam = Cam((0,0,-5))

pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(0)
pygame.event.set_grab(1)

# ### WINDOW WHILE LOOP
while True:

	# clock tick time delta
	dt = clock.tick()/1000

	# event handler
	for event in pygame.event.get():

		# quit when user exits
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

		cam.events(event)


	# screen fill white
	screen.fill((255,255,255))

	
	# drawing edges
	for edge in edges:

		# temp list of points for drawing lines
		points = []

		# find positions of lines based on respective verts
		for x,y,z in (verts[edge[0]],verts[edge[1]]):

			x -= cam.pos[0]
			y -= cam.pos[1]
			z -= cam.pos[2]

			x,z = rotate2d((x,z), cam.rot[1])
			y,z = rotate2d((y,z), cam.rot[0])

			f = 200/z
			x,y = x*f,y*f
			points += [(cx+int(x), cy+int(y))]

		# draw lines from temp list
		pygame.draw.line(screen, (0, 0, 255), points[0], points[1], 1)
	

	# update screen
	pygame.display.flip()

	keys = pygame.key.get_pressed()
	cam.update(dt, keys)