import pygame
import random
import sys
import datetime
from pygame.locals import *

class GameState:
	def update(dt):
		return
	def draw():
		return

class GameObject:
	def update(dt):
		return
	def draw():
		return

class Game:
	def __init__(self):
		pygame.init()
		self.mainClock = pygame.time.Clock()
		self.screenW = 800
		self.screenH = 600
		self.screen = pygame.display.set_mode((self.screenW, self.screenH))
		pygame.display.set_caption('Tetrix')
	def play(self):
		while True:
			dt = self.mainClock.get_time() / 1000
			render()
			update(dt)
			self.mainClock.tick(30)
		return
	def update(dt):
		return
	def render():
		return

game = Game()
game.play()