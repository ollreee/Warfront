import pygame, sys, time, random
pygame.init()

from config import *

version = "Alpha 1.0"

print("Welcome to Warfront {}".format(version))

#Opens the screen
icon = pygame.image.load("graphics/app.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warfront {}".format(version))


def main_menu():
	#Setting up images and sounds
	big_font = pygame.font.SysFont('freesansbold', 100, True, False)
	small_font = pygame.font.SysFont('freesansbold', 30, True, False)
	menu_bg = pygame.image.load("graphics/gui/menu_bg.png")
	button1 = pygame.image.load("graphics/gui/button1.png")

	#Main loop
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#if event.type == pygame.KEYDOWN:
				#pass
	
		screen.blit(menu_bg, [0, 0])
		screen.blit(button1, [900, 200])
		screen.blit(button1, [900, 300])
	
		title = big_font.render("Warfront", True, WHITE)
		new_game = small_font.render("New Game", True, WHITE)
		load_game = small_font.render("Load Game", True, WHITE)
		screen.blit(title, [900, 40])
		screen.blit(new_game, [915, 215])
		screen.blit(load_game, [915, 315])
	
		pygame.display.flip()
		#Drawing ends here

		clock.tick(60)
		
def create_game():
	pass
	
def save_game():
	pass

def load_game():
	pass
	
def play_game():
	pass
	
main_menu()
