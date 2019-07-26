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

			import ent_game

			self.window = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
			self.run    = True

			pygame.display.set_caption("My Dear Batata")

			self.start_scene = True

			self.player = ent_game.player(self.window, 800, "beta", "player")
			self.enemie = ent_game.player(self.window, 500, "galinha", "enemies", ins = self.player)

			while self.run:
				if self.start_scene:
					self.window.fill((190, 190, 190, 50))

					for process in pygame.event.get():
						self.load_event(process, pygame.QUIT, self.end_loop)

					self.scene()

					pygame.display.flip()
		except:
			raise
		return None

	def scene(self):
		try:
			self.player.add_event(type = "attack")
			self.player.spawn()

			self.enemie.add_event(type = "attack")
			self.enemie.spawn()

			self.player.get_damage(self.enemie.hit)
			self.enemie.get_damage(self.player.hit)
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
