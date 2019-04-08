import pygame, sys, time, random
from pygame.locals import *
from config import *

version = "Alpha 1.0"

print("Welcome to Warfront {}".format(version))

#Opens the screen
pygame.init()
icon = pygame.image.load("graphics/icons/app.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warfront {}".format(version))

#The main menu
def main_menu():
	#Setting up images and sounds
	big_font = pygame.font.SysFont("freesansbold", 100)
	menu_bg = pygame.image.load("graphics/gui/menu_bg.png")
	
	screen.blit(menu_bg, [0, 0])
	
	#Main loop
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == K_1:
					create_game()
				elif event.key == K_2:
					load_game()
				elif event.key == K_3:
					show_credits()
				elif event.key == K_4:
					pygame.quit()
					sys.exit()
		
		#Drawing ends here
		pygame.display.update()

		clock.tick(60)

#The function to create a new game with chosen starting values and settings
def create_game():
	print("game created")

#Writing an existing game to a file
def save_game():
	print("game saved")

#Loading an existing game from a file to continue playing
def load_game():
	print("game loaded")
	
def show_credits():
	print("showing credits")

#The main game function
def play_game():
	game_paused = False
	
	"""class Button(pygame.sprite.Sprite):
		def __init__(self, button_type):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("graphics/gui/button1.png")
			self.rect = self.image.get_rect()
			
			
			self.font = pygame.font.SysFont("freesansbold", 30)
			#if button_type == "new_game":
				#self.textSurf = self.font.render("New Game", True, WHITE)
			#elif button_type == "load_game":
				#self.textSurft = self.font.render("Load Game", True, WHITE)
			#WIDTH = self.textSurf.get_width()
			#HEIGHT = self.textSurf.get_height()
			
		def clicked(self, click_pos):
			create_game()
			
	new_game_button = Button("new_game")
	new_game_button.rect.x, new_game_button.rect.y = 900, 200
	load_game_button = Button("load_game")
	load_game_button.rect.x, load_game_button.rect.y = 900, 300
	
	clickable_objects_list = pygame.sprite.Group()
	clickable_objects_list.add(new_game_button)
	clickable_objects_list.add(load_game_button)"""
	
	#Main loop
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					for object in clickable_objects_list:
						object.clicked(event.pos)
			elif event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					game_paused = True
					
		if not game_paused:
			pass
			#clickable_objects_list.draw(screen)
		
		#Drawing ends here
		pygame.display.update()
		
		clock.tick(60)


main_menu()
