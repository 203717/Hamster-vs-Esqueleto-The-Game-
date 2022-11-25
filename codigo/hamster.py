import pygame

class Hamster(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		super().__init__()
		file_path = 'D:/Downloads/jueguito/grafi/' + color + '.png'
		self.image = pygame.image.load(file_path).convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))
		if color == 'rojo': self.value = 100
		elif color == 'verde': self.value = 200

	def update(self,direction):
		self.rect.x += direction

class Mini(pygame.sprite.Sprite):
	def __init__(self,side,screen_width):
		super().__init__()
		self.image = pygame.image.load('D:/Downloads/jueguito/grafi/mini.png').convert_alpha()
		
		if side == 'right':
			x = screen_width + 50
			self.speed = - 3
		else:
			x = -50
			self.speed = 3

		self.rect = self.image.get_rect(topleft = (x,80))

	def update(self):
		self.rect.x += self.speed