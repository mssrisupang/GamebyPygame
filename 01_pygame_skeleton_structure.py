# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Define game window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My PyGame')

# Define colors
#color = (255, 255, 255)  #white
color = (102,255,178)       #blue

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    # (Add code to update game objects' states)

    # Render game objects
    screen.fill(color)
    # (Add code to draw game objects on the screen)

    #pygame.display.flip()
    pygame.display.update()

# Clean up and quit
pygame.quit()
sys.exit()
