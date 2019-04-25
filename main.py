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

#A simple sanity test for user input on text menus, obsolete when GUI's get implemented
def number_test(number):
		try:
			int(number)
			return int(number)
		except ValueError:
			return False

#The main menu
def main_menu():	
	#Setting up images and sounds
	big_font = pygame.font.SysFont("freesansbold", 100)
	menu_bg = pygame.image.load("graphics/gui/menu_bg.png")
	
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
	
	"""class Faction():
		def __init__(self):
			confirmed = False
			
			while not confirmed:
				self.name = input("What is the name of your faction? ").strip()
				self.money = input("How rich is your faction? (1-10) ").strip()
				self.advancement = input("How advanced is your faction? (1-10) ").strip()
				
				print("{}, {}, {}".format(self.name, self.money, self.advancement))
				if input("Is this okay? Type \"yes\" to accept. ") == "yes":
					confirmed = True
	
	create_factions_menu = True
	factions_list = []
	
	while create_factions_menu:
		main_input = input("> ")
		
		if main_input == "create_faction":
			factions_list.append(Faction())
			
		elif main_input == "done":
			print(factions_list)
			create_factions_menu = False"""


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
	#Loading map tileset
	I_FOREST = pygame.image.load("graphics/map/forest.png")
	I_SEA = pygame.image.load("graphics/map/sea.png")
	I_DESERT = pygame.image.load("graphics/map/desert.png")
	I_ARCTIC = pygame.image.load("graphics/map/arctic.png")
	
	FOREST = 0
	SEA = 1
	DESERT = 2
	ARCTIC = 3
	
	tile_images = {
		FOREST: I_FOREST,
		SEA: I_SEA,
		DESERT: I_DESERT,
		ARCTIC: I_ARCTIC
	}
	
	TILESIZE = 40
	MAPWIDTH = 20
	MAPHEIGHT = 18
	
	tilemap = [[SEA for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
	
	for row in range(MAPHEIGHT):
		for col in range(MAPWIDTH):
			rand_number = random.randrange(0, 100)
			if row < 3 or row > 15:
				tile = SEA
			elif row < 5:
				tile = ARCTIC
			elif row < 12:
				if rand_number < 80:
					tile = FOREST
				else:
					tile = SEA
			else:
				tile = DESERT
				
			tilemap[row][col] = tile
	
	in_game_ui = pygame.image.load("graphics/gui/in_game_ui.png")
	
	game_paused = False
	
	#Main loop
	clock = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pass
			elif event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					game_paused = not game_paused
					
		if not game_paused:
			for row in range(MAPHEIGHT):
				for col in range(MAPWIDTH):
					screen.blit(tile_images[tilemap[row][col]], [col*TILESIZE, row*TILESIZE])
			
			screen.blit(in_game_ui, [800, 0])
			#clickable_objects_list.draw(screen)
		
		#Drawing ends here
		pygame.display.update()
		
		clock.tick(60)


play_game()