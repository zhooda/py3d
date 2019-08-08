import pygame, sys, math

class Cam:
	def __init__(self, pos = (0, 0, 0), rot = (0, 0)):
		self.pos = list(pos)
		self.rot = list(rot)

	def update(self, dt, key):
		s = dt*10

		if key[pygame.K_q]: self.pos[1] -= s
		if key[pygame.K_e]: self.pos[1] += s

		if key[pygame.K_w]: self.pos[2] += s
		if key[pygame.K_s]: self.pos[2] -= s
		if key[pygame.K_a]: self.pos[0] -= s
		if key[pygame.K_d]: self.pos[0] += s


def rotate2d(pos, rad):
	x,y = pos
	s,c = math.sin(rad), math.cos(rad)
	return x*c-y*s,y*c+x*s