import pygame as pygame
from pygame import *

import json
import sys
import os

class player(object):
	def __init__(self, render, size = None, skin = None, tag = None, ins = None):
		try:
			import images

			self.render    = render
			self.tag       = tag
			self.x         = 0 if self.tag is "player" else ins.size[0] - 300
			self.y         = 0 if self.tag is "player" else 0
			self.life      = 100
			self.size      = size, size
			self.frames    = 0
			self.hit       = 0
			self.rendering = True

			if skin is "beta":
				self.sprites = [
				self.load_image(images.SPRITE_PLAYER_GUARD),
				self.load_image(images.SPRITE_PLAYER_PUNCH)]

			if skin is "galinha":
				self.sprites = [ self.load_image(images.SPRITE_GAL)]
		except:
			raise
		return None

	def load_image(self, image):
		try:
			import io
			import base64

			return pygame.transform.scale(pygame.image.load(io.BytesIO(base64.b64decode(image))), (self.size))
		except:
			raise
		return None

	def add_event(self, process = None, type = None):
		try:
			if type is "attack":
				self.key = pygame.key.get_pressed()

				if self.key[pygame.K_f]:
					self.frames = 1 if self.tag is "player" else 0
					self.hit    = 1 if self.tag is "player" else 0

				else:
					self.frames = 0
					self.hit    = 0			
		except:
			raise
		return None

	def get_damage(self, hit):
		try:
			self.life -= hit
		except:
			raise
		return None

	def spawn(self):
		try:
			if self.rendering:
				if self.life > 0:
					self.render.blit(self.sprites[int(self.frames)], (self.x, self.y))

				elif self.life < 0:
					print("Dead")
					self.rendering = False
		except:
			raise
		return None