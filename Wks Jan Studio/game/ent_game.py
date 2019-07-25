import pygame as pygame
from pygame import *

import json
import sys
import os

class spawn_ent(object):
	def __init__(self, render, tag):
		try:
			print("spawned {type}".format(type = tag))
		except:
			raise
		return None