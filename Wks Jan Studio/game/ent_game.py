import pygame as pygame
from pygame import *

import json
import sys
import os

class player(object):
	def __init__(self, render, size = None, skin = None, tag = None):
		try:
			import images

			self.render    = render
			self.tag       = tag
			self.x         = 0
			self.y         = 0
			self.life      = 100
			self.size      = size, size
			self.frames    = 0
			self.rendering = True

			if skin is "beta":
				self.sprites = [
				self.load_image(images.SPRITE_BETA_0),
				self.load_image(images.SPRITE_BETA_1),
				self.load_image(images.SPRITE_BETA_2),
				self.load_image(images.SPRITE_BETA_3),
				self.load_image(images.SPRITE_BETA_4),
				self.load_image(images.SPRITE_BETA_5),
				self.load_image(images.SPRITE_BETA_6),
				self.load_image(images.SPRITE_BETA_7),
				self.load_image(images.SPRITE_BETA_8),
				self.load_image(images.SPRITE_BETA_9),
				self.load_image(images.SPRITE_BETA_10),
				self.load_image(images.SPRITE_BETA_11)]
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
			if type is "move":
				self.key = pygame.key.get_pressed()

				if self.key[pygame.K_w]:
					self.y -= 5

				if self.key[pygame.K_a]:
					self.x -= 5

				if self.key[pygame.K_s]:
					self.y += 5

					self.frames += 1

					if self.frames >= 3:
						self.frames = 1

				if self.key[pygame.K_d]:
					self.x += 5
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