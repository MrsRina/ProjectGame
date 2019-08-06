import pygame

class load_object(object):
	def __init__(self, tag):
		try:
			self.tag             = tag
			self.node            = pygame.rect.Rect(0, 0, 0, 0)
			self.images          = {}
			self.rendering_image = self.images
			self.render          = True
			self.render_image    = True
		except:
			raise
		return None

	def add_image(self, image, tag):
		try:
			import io
			import base64

			self.images[tag] = pygame.transform.scale(pygame.image.load(io.BytesIO(base64.b64decode(image))), (self.node.x, self.node.y))
		except:
			raise
		return None

	def set_image(image):
		try:
			if image is "None" or image is None:
				self.render_image = False

			else:
				try:
					self.rendering_image = image
				except:
					pass
		except:
			raise
		return None

	def move(self, type, event):
		try:
			if type is 0:
				if event.type is pygame.MOUSEBUTTONDOWN:
					self.node.center = event.pos
		except:
			raise
		return None

	def set_pos(self, x = None, y = None):
		try:
			self.node.x = x
			self.node.y = y
		except:
			raise
		return None

	def set_size(self, width = None, height = None):
		try:
			self.node.w = width
			self.node.h = height
		except:
			raise
		return None

	def reparent_to(self, master):
		try:
			if self.render:
				if self.render_image:
					master.blit(self.images[self.rendering_image], self.node)
		except:
			raise
		return None
