import pygame as pygame
from pygame import *

import json
import sys
import os

class Game(object):
	def __init__(self):
		try:
			width  = 1024
			height = 768

			self.window = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
			self.run    = True

			pygame.display.set_caption("My Dear Batata")

			self.start_scene = True

			import mok_2d
			import images

			self.config_scenes(framework = mok_2d, images = images)

			while self.run:
				if self.start_scene:
					self.window.fill((190, 190, 190, 50))

					for process in pygame.event.get():
						self.load_event(process, pygame.QUIT, self.end_loop)
						self.planet.move(0, process)

					self.planet.reparent_to(self.window)

					pygame.display.flip()
		except:
			raise
		return None

	def load_event(self, process, event_name, function):
		try:
			if process.type is event_name:
				return function()
		except:
			raise
		return None

	def config_scenes(self, framework, images):
		try:
			self.planet = framework.load_object("Planet")
			self.planet.add_image(images.IMAGE_PLANET, "Planet_Image")
		except:
			raise
		return None

	def end_loop():
		try:
			self.run = False
			sys.exit()
		except:
			raise
		return None

if not __name__ is "__main__":
	try:
		Game()
	except:
		raise
