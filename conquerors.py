import pygame, sys
from pygame.locals import *

def getNewBoard():
	board = []
	for x in range(int(WIDTH / CELLSIZE)):
		board.append([])
		for y in range(int(HEIGHT / CELLSIZE)):
			board[x].append({'player': None, 'area': None, 'track': None})
	return board

def terminate():
	pygame.quit()
	sys.exit()

def waitForPlayerToPressEnter():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				if event.key == K_RETURN:
					return

def drawText(text, font, cx, cy):
	textSurf = font.render(text, 1, TEXTCOLOR)
	textRect = textSurf.get_rect(center = (cx, cy))
	windowSurface.blit(textSurf, textRect)

def pause():
	pygame.mixer.music.pause()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.mixer.music.unpause()
					return
		
		drawText('Game paused', bigFont, WIDTH / 2, HEIGHT * 1/3)
		drawText('Press ESC to resume the game', smallFont, WIDTH / 2, HEIGHT * 5/6)  
		pygame.display.update()          


# Set up colors.
# Just create new tuple and append it to 'colors' list to add new color. 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)

colors = [RED, GREEN, BLUE, YELLOW, AQUA, MAGENTA]

# Set up game constants.
GAMENAME = 'Conquerors'
WIDTH = 800
HEIGHT = 600
CELLSIZE = 20
FPS = 10
ROUNDTIME = 60 * 1000
TEXTCOLOR = BLACK
BACKGROUND = WHITE

# Set up move directions.
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Set up board status labels.
PLAYER1 = 'Player 1'
PLAYER2 = 'Player 2'
AREA1 = 'area1'
AREA2 = 'area2'
TRACK1 = 'track1'
TRACK2 = 'track2'

# Set up pygame window
pygame.init()
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAMENAME)
mainClock = pygame.time.Clock()

# Set up fonts
bigFont = pygame.font.Font('west_england.ttf', 64)
mediumFont = pygame.font.Font('west_england.ttf', 32)
smallFont = pygame.font.Font('west_england.ttf', 24)

# Set up images.
# Just create new dictionary and append it to 'bugs' list to add new bug to the game.
bugsurf1 = pygame.transform.scale(pygame.image.load('1.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug1 = {
	'up': bugsurf1,
	'down': pygame.transform.rotate(bugsurf1, 180),
	'left': pygame.transform.rotate(bugsurf1, 90), 
	'right': pygame.transform.rotate(bugsurf1, -90),
}

bugsurf2 = pygame.transform.scale(pygame.image.load('2.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug2 = {
	'up': bugsurf2,
	'down': pygame.transform.rotate(bugsurf2, 180),
	'left': pygame.transform.rotate(bugsurf2, 90), 
	'right': pygame.transform.rotate(bugsurf2, -90),
}

bugsurf3 = pygame.transform.scale(pygame.image.load('3.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug3 = {
	'up': bugsurf3,
	'down': pygame.transform.rotate(bugsurf3, 180),
	'left': pygame.transform.rotate(bugsurf3, 90), 
	'right': pygame.transform.rotate(bugsurf3, -90),
}

bugsurf4 = pygame.transform.scale(pygame.image.load('4.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug4 = {
	'up': bugsurf4,
	'down': pygame.transform.rotate(bugsurf4, 180),
	'left': pygame.transform.rotate(bugsurf4, 90), 
	'right': pygame.transform.rotate(bugsurf4, -90),
}

bugsurf5 = pygame.transform.scale(pygame.image.load('5.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug5 = {
	'up': bugsurf5,
	'down': pygame.transform.rotate(bugsurf5, 180),
	'left': pygame.transform.rotate(bugsurf5, 90), 
	'right': pygame.transform.rotate(bugsurf5, -90),
}

bugsurf6 = pygame.transform.scale(pygame.image.load('6.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug6 = {
	'up': bugsurf6,
	'down': pygame.transform.rotate(bugsurf6, 180),
	'left': pygame.transform.rotate(bugsurf6, 90), 
	'right': pygame.transform.rotate(bugsurf6, -90),
}

bugsurf7 = pygame.transform.scale(pygame.image.load('7.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug7 = {
	'up': bugsurf7,
	'down': pygame.transform.rotate(bugsurf7, 180),
	'left': pygame.transform.rotate(bugsurf7, 90), 
	'right': pygame.transform.rotate(bugsurf7, -90),
}

bugsurf8 = pygame.transform.scale(pygame.image.load('8.png'), (2 * CELLSIZE, 2 * CELLSIZE))
bug8 = {
	'up': bugsurf8,
	'down': pygame.transform.rotate(bugsurf8, 180),
	'left': pygame.transform.rotate(bugsurf8, 90), 
	'right': pygame.transform.rotate(bugsurf8, -90),
}

bugs = [bug1, bug2, bug3, bug4, bug5, bug6, bug7, bug8]

# Set up sounds
pygame.mixer.music.load('music.wav')

# WELCOME SCREEN
windowSurface.fill(BACKGROUND)

drawText('Welcome to', mediumFont, WIDTH/2, HEIGHT/4)
drawText('CONQUERORS', bigFont, WIDTH/2, HEIGHT/2)
drawText('Press Enter to start', smallFont, WIDTH/2, HEIGHT* 3/4)

pygame.display.update()

waitForPlayerToPressEnter()

playGame = False
gameOver = False

# Set up players
player1 = {
'coords': [1,28],
'bug': bugs[0], 
'color': colors[0],
}

player2 = {
'coords': [38,1],
'bug': bugs[1], 
'color': colors[1],
}

# THE MAIN GAME LOOP
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				terminate()
			if event.key == K_RETURN:
				playGame = True
				
			# Bug and color selection for Player 1.
			if event.key == K_w:
				i = bugs.index(player1['bug'])
				if i < len(bugs) - 1:
					player1['bug'] = bugs[i + 1]
				else:
					player1['bug'] = bugs[0]
			if event.key == K_s:
				i = bugs.index(player1['bug'])
				if i > 0:
					player1['bug'] = bugs[i - 1]
				else:
					player1['bug'] = bugs[-1]
			if event.key == K_d:
				i = colors.index(player1['color'])
				if i < len(colors) - 1:
					player1['color'] = colors[i + 1]
				else:
					player1['color'] = colors[0]
			if event.key == K_a:
				i = colors.index(player1['color'])
				if i > 0:
					player1['color'] = colors[i - 1]
				else:
					player1['color'] = colors[-1]

			# Bug and color selection for Player 2.
			if event.key == K_UP:
				i = bugs.index(player2['bug'])
				if i < len(bugs) - 1:
					player2['bug'] = bugs[i + 1]
				else:
					player2['bug'] = bugs[0]
			if event.key == K_DOWN:
				i = bugs.index(player2['bug'])
				if i > 0:
					player2['bug'] = bugs[i - 1]
				else:
					player2['bug'] = bugs[-1]
			if event.key == K_RIGHT:
				i = colors.index(player2['color'])
				if i < len(colors) - 1:
					player2['color'] = colors[i + 1]
				else:
					player2['color'] = colors[0]
			if event.key == K_LEFT:
				i = colors.index(player2['color'])
				if i > 0:
					player2['color'] = colors[i - 1]
				else:
					player2['color'] = colors[-1]

	# CHOOSE YOUR FIGHTER SCREEN.
	windowSurface.fill(BACKGROUND)

	drawText('Choose your fighter!', bigFont, WIDTH/2, HEIGHT/6)

	drawText('Player 1', mediumFont, WIDTH/4, HEIGHT/3)
	drawText('W', smallFont, WIDTH/4, HEIGHT/2 - 50)
	drawText('S', smallFont, WIDTH/4, HEIGHT/2 + 50)
	drawText('A', smallFont, WIDTH/4 - 50, HEIGHT/2 + 110)
	drawText('D', smallFont, WIDTH/4 + 50, HEIGHT/2 + 110)

	drawText('Player 2', mediumFont, WIDTH* 3/4, HEIGHT/3)
	drawText('^', smallFont, WIDTH* 3/4, HEIGHT/2 - 50)
	drawText('v', smallFont, WIDTH* 3/4, HEIGHT/2 + 50)
	drawText('[', smallFont, WIDTH* 3/4 - 50, HEIGHT/2 + 110)
	drawText(']', smallFont, WIDTH* 3/4 + 50, HEIGHT/2 + 110)

	drawText('Press ENTER to continue', smallFont, WIDTH/2, HEIGHT* 5/6 + 25)
	drawText('Press ESC to quit', smallFont, WIDTH/2, HEIGHT* 5/6 + 50)

	windowSurface.blit(player1['bug']['up'], pygame.Rect(WIDTH/4 - CELLSIZE, HEIGHT/2 - CELLSIZE, 0, 0))
	windowSurface.blit(player2['bug']['up'], pygame.Rect(WIDTH * 3/4 - CELLSIZE, HEIGHT/2 - CELLSIZE, 0, 0))

	pygame.draw.rect(windowSurface, player1['color'], (WIDTH/4 - CELLSIZE, HEIGHT/2 + 90, 2 * CELLSIZE, 2 * CELLSIZE))
	pygame.draw.rect(windowSurface, player2['color'], (WIDTH * 3/4 - CELLSIZE, HEIGHT/2 + 90, 2 * CELLSIZE, 2 * CELLSIZE))

	pygame.display.update()
	mainClock.tick(FPS)

	# Prepare for the new round.
	if playGame:
		pygame.time.set_timer(USEREVENT, ROUNDTIME)
		timer = 0
		direction1 = UP
		direction2 = DOWN
		score1 = 0
		score2 = 0
		# Create new board.
		board = getNewBoard()
		# Place players on default positions.
		player1['coords'] = [1,28]
		player2['coords'] = [38,1]
		# Place players on the Cell objects.
		board[player1['coords'][0]][player1['coords'][1]]['player'] = PLAYER1
		board[player2['coords'][0]][player2['coords'][1]]['player'] = PLAYER2
		# Define initial players' areas.
		for x in range(5):
			for y in range(int(HEIGHT / CELLSIZE) - 5, int(HEIGHT / CELLSIZE)):
				board[x][y]['area'] = AREA1

		for x in range(int(WIDTH / CELLSIZE) - 5, int(WIDTH / CELLSIZE)):
			for y in range(5):
				board[x][y]['area'] = AREA2
		# Play music
		pygame.mixer.music.play(-1, 0.0)

	# GAME ROUND SUBLOOP    
	while playGame:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == USEREVENT:
				playGame = False
				gameOver = True
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pause()
			
				# Key events for player 1.
				if event.key == K_a and direction1 != RIGHT:
					direction1 = LEFT
				elif event.key == K_d and direction1 != LEFT:
					direction1 = RIGHT
				elif event.key == K_w and direction1 != DOWN:
					direction1 = UP
				elif event.key == K_s and direction1 != UP:
					direction1 = DOWN
			
				# Key events for player 2.
				if event.key == K_LEFT and direction2 != RIGHT:
					direction2 = LEFT
				elif event.key == K_RIGHT and direction2 != LEFT:
					direction2 = RIGHT
				elif event.key == K_UP and direction2 != DOWN:
					direction2 = UP
				elif event.key == K_DOWN and direction2 != UP:
					direction2 = DOWN

		# Move player 1 around and keep a track after him if he is not on his area.
		if direction1 == LEFT and player1['coords'][0] > 0:
			# Erase old player's position from the board object.
			board[player1['coords'][0]][player1['coords'][1]]['player'] = None
			# If player is not on his own area keep a track after him.
			if board[player1['coords'][0]][player1['coords'][1]]['area'] != AREA1:
				board[player1['coords'][0]][player1['coords'][1]]['track'] = TRACK1
			# Change player's coord in the player object.
			player1['coords'][0] -= 1
			# Write new player's position to the board object.
			board[player1['coords'][0]][player1['coords'][1]]['player'] = PLAYER1
		elif direction1 == RIGHT and player1['coords'][0] < int(WIDTH / CELLSIZE) - 1:
			board[player1['coords'][0]][player1['coords'][1]]['player'] = None
			if board[player1['coords'][0]][player1['coords'][1]]['area'] != AREA1:
				board[player1['coords'][0]][player1['coords'][1]]['track'] = TRACK1
			player1['coords'][0] += 1
			board[player1['coords'][0]][player1['coords'][1]]['player'] = PLAYER1
		elif direction1 == UP and player1['coords'][1] > 0:
			board[player1['coords'][0]][player1['coords'][1]]['player'] = None
			if board[player1['coords'][0]][player1['coords'][1]]['area'] != AREA1:
				board[player1['coords'][0]][player1['coords'][1]]['track'] = TRACK1
			player1['coords'][1] -= 1
			board[player1['coords'][0]][player1['coords'][1]]['player'] = PLAYER1
		elif direction1 == DOWN and player1['coords'][1] < int(HEIGHT / CELLSIZE) - 1:
			board[player1['coords'][0]][player1['coords'][1]]['player'] = None
			if board[player1['coords'][0]][player1['coords'][1]]['area'] != AREA1:
				board[player1['coords'][0]][player1['coords'][1]]['track'] = TRACK1
			player1['coords'][1] += 1
			board[player1['coords'][0]][player1['coords'][1]]['player'] = PLAYER1

		# Move player 2 around and keep a track after him if he is not on his area.
		if direction2 == LEFT and player2['coords'][0] > 0:
			board[player2['coords'][0]][player2['coords'][1]]['player'] = None
			if board[player2['coords'][0]][player2['coords'][1]]['area'] != AREA2:
				board[player2['coords'][0]][player2['coords'][1]]['track'] = TRACK2
			player2['coords'][0] -= 1
			board[player2['coords'][0]][player2['coords'][1]]['player'] = PLAYER2
		elif direction2 == RIGHT and player2['coords'][0] < int(WIDTH / CELLSIZE) - 1:
			board[player2['coords'][0]][player2['coords'][1]]['player'] = None
			if board[player2['coords'][0]][player2['coords'][1]]['area'] != AREA2:
				board[player2['coords'][0]][player2['coords'][1]]['track'] = TRACK2
			player2['coords'][0] += 1
			board[player2['coords'][0]][player2['coords'][1]]['player'] = PLAYER2
		elif direction2 == UP and player2['coords'][1] > 0:
			board[player2['coords'][0]][player2['coords'][1]]['player'] = None
			if board[player2['coords'][0]][player2['coords'][1]]['area'] != AREA2:
				board[player2['coords'][0]][player2['coords'][1]]['track'] = TRACK2
			player2['coords'][1] -= 1
			board[player2['coords'][0]][player2['coords'][1]]['player'] = PLAYER2
		elif direction2 == DOWN and player2['coords'][1] < int(HEIGHT / CELLSIZE) - 1:
			board[player2['coords'][0]][player2['coords'][1]]['player'] = None
			if board[player2['coords'][0]][player2['coords'][1]]['area'] != AREA2:
				board[player2['coords'][0]][player2['coords'][1]]['track'] = TRACK2
			player2['coords'][1] += 1
			board[player2['coords'][0]][player2['coords'][1]]['player'] = PLAYER2
		
		# Set all TRACK CELLs as AREA, if player returned to his AREA.
		for x in range(int(WIDTH/CELLSIZE)):
			for y in range(int(HEIGHT/CELLSIZE)):

				# Check if PLAYER1 returned on AREA1.
				if board[x][y]['player'] == PLAYER1 and board[x][y]['area'] == AREA1:
					# Convert all CELLs which are TRACK1 to AREA1.
					for x in range(int(WIDTH/CELLSIZE)):
						for y in range(int(HEIGHT/CELLSIZE)):
							if board[x][y]['track'] == TRACK1:
								board[x][y]['track'] = None
								board[x][y]['area'] = AREA1
					# Find all empty inner CELLs inside AREA1 and make them AREA1 too.
					for x in range(1, int(WIDTH/CELLSIZE)-1):
						for y in range(1, int(HEIGHT/CELLSIZE)-1):
							if board[x][y]['area'] != AREA1:
								exitFlag = False
								counter = 0
								for xDirection, yDirection in [[1,0], [0,1], [-1,0], [0,-1]]:
									xNew, yNew = x, y
									while xNew != 0 and yNew != 0 and xNew != int(WIDTH/CELLSIZE)-1 and yNew != int(HEIGHT/CELLSIZE)-1:
										xNew += xDirection
										yNew += yDirection
										if board[xNew][yNew]['area'] == AREA1:
											counter += 1
											break
										if xNew == 0 or yNew == 0 or xNew == int(WIDTH/CELLSIZE)-1 or yNew == int(HEIGHT/CELLSIZE)-1:
											exitFlag = True
											break
									if exitFlag:
										break
								if counter == 4:
									board[x][y]['area'] = AREA1
								
				# Player 2
				if board[x][y]['player'] == PLAYER2 and board[x][y]['area'] == AREA2:
					# Convert all CELLs which are TRACK2 to AREA2.
					for x in range(int(WIDTH/CELLSIZE)):
						for y in range(int(HEIGHT/CELLSIZE)):
							if board[x][y]['track'] == TRACK2:
								board[x][y]['track'] = None
								board[x][y]['area'] = AREA2
					# Find all empty inner CELLs inside AREA2 and make them AREA2 too.
					for x in range(1, int(WIDTH/CELLSIZE)-1):
						for y in range(1, int(HEIGHT/CELLSIZE)-1):
							if board[x][y]['area'] != AREA2:
								exitFlag = False
								counter = 0
								for xDirection, yDirection in [[1,0], [0,1], [-1,0], [0,-1]]:
									xNew, yNew = x, y
									while xNew != 0 and yNew != 0 and xNew != int(WIDTH/CELLSIZE)-1 and yNew != int(HEIGHT/CELLSIZE)-1:
										xNew += xDirection
										yNew += yDirection
										if board[xNew][yNew]['area'] == AREA2:
											counter += 1
											break
										if xNew == 0 or yNew == 0 or xNew == int(WIDTH/CELLSIZE)-1 or yNew == int(HEIGHT/CELLSIZE)-1:
											exitFlag = True
											break
									if exitFlag:
										break
								if counter == 4:
									board[x][y]['area'] = AREA2


		# Count all CELLs with AREA1 and AREA2 area attribute.
		score1 = score2 = 0
		for x in range(int(WIDTH / CELLSIZE)):
			for y in range(int(HEIGHT / CELLSIZE)):
				if board[x][y]['area'] == AREA1:
					score1 += 1
				if board[x][y]['area'] == AREA2:
					score2 += 1

		# Check for collision between players and tracks.
		for x in range(int(WIDTH / CELLSIZE)):
			for y in range(int(HEIGHT / CELLSIZE)):
				if board[x][y]['player'] == PLAYER1 and board[x][y]['track'] == TRACK1:
					score1 = 0
					gameOver = True
					playGame = False
				if board[x][y]['player'] == PLAYER2 and board[x][y]['track'] == TRACK2:
					score2 = 0
					gameOver = True
					playGame = False
				if board[x][y]['player'] == PLAYER1 and board[x][y]['track'] == TRACK2:
					score2 = 0
					gameOver = True
					playGame = False
				if board[x][y]['player'] == PLAYER2 and board[x][y]['track'] == TRACK1:
					score1 = 0
					gameOver = True
					playGame = False

		windowSurface.fill(BACKGROUND)

		# Draw each CELL on the screen depending on what values its attributes have.
		for x in range(int(WIDTH / CELLSIZE)):
			for y in range(int(HEIGHT / CELLSIZE)):
				
				# Draw AREAs.
				if board[x][y]['area'] == AREA1:
					pygame.draw.rect(windowSurface, player1['color'], pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
				if board[x][y]['area'] == AREA2:
					pygame.draw.rect(windowSurface, player2['color'], pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
				
				# Draw TRACKs.
				if board[x][y]['track'] == TRACK1:
					cellSurface = pygame.Surface((CELLSIZE, CELLSIZE))
					cellSurface.set_alpha(100)
					cellSurface.fill(player1['color'])
					windowSurface.blit(cellSurface, pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
				if board[x][y]['track'] == TRACK2:
					cellSurface = pygame.Surface((CELLSIZE, CELLSIZE))
					cellSurface.set_alpha(100)
					cellSurface.fill(player2['color'])
					windowSurface.blit(cellSurface, pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
		
		# Draw PLAYERs.
		for x in range(int(WIDTH / CELLSIZE)):
			for y in range(int(HEIGHT / CELLSIZE)):
				if board[x][y]['player'] == PLAYER1:
					if direction1 == UP:
						windowSurface.blit(player1['bug']['up'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction1 == DOWN:
						windowSurface.blit(player1['bug']['down'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction1 == LEFT:
						windowSurface.blit(player1['bug']['left'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction1 == RIGHT:
						windowSurface.blit(player1['bug']['right'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
				if board[x][y]['player'] == PLAYER2:
					if direction2 == UP:
						windowSurface.blit(player2['bug']['up'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction2 == DOWN:
						windowSurface.blit(player2['bug']['down'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction2 == LEFT:
						windowSurface.blit(player2['bug']['left'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
					elif direction2 == RIGHT:
						windowSurface.blit(player2['bug']['right'], pygame.Rect(x * CELLSIZE - CELLSIZE / 2, y * CELLSIZE - CELLSIZE / 2, 0, 0))
		
		# Draw timer.
		drawText(str(round(timer/1000, 1)), mediumFont, WIDTH/2, HEIGHT/2)

		# Draw score.
		drawText(str(score1), smallFont, 50, HEIGHT - 50)
		drawText(str(score2), smallFont, WIDTH - 50, 50)

		pygame.display.update()
		mainClock.tick(FPS)

		timer += 1000 / FPS

		if gameOver:
			# Define the winner.
			if score1 > score2:
				winner = PLAYER1
				winscore = score1
			else:
				winner = PLAYER2
				winscore = score2

		while gameOver:
			for event in pygame.event.get():
				if event.type == QUIT:
					terminate()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						terminate()
					if event.key == K_RETURN:
						gameOver = False

			pygame.mixer.music.stop()
			windowSurface.fill(BACKGROUND)
			drawText('GAME OVER', bigFont, WIDTH/2, HEIGHT/4)
			drawText(f'{winner} wins with {winscore} points!', mediumFont, WIDTH/2, HEIGHT/2)
			drawText('Press ENTER to play again', smallFont, WIDTH/2, HEIGHT* 3/4)
			drawText('Press ESC to quit', smallFont, WIDTH/2, HEIGHT* 3/4 + 50)
			pygame.display.update()