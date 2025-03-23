# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Define game window settings
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My PyGame with Sprite')

# Define colors
color = (255, 255, 255)  #white
#color = (0,0,255)       #blue

# Sprite Class
class MySprite(pygame.sprite.Sprite):
   def __init__(self,x, y, width, height, color):            # constructor
      super().__init__()
      self.image = pygame.Surface((width, height))
      self.image.fill((color))  # filling sprite with green
      self.rect = self.image.get_rect(topleft=(x, y))

# Create sprite instance and sprite group
sprite1 = MySprite(10, 10, 50, 50, (255, 0, 0))  # Red sprite
sprite2 = MySprite(100, 75, 30, 30, (0, 0, 255))  # Blue sprite, different position and size
sprites = pygame.sprite.Group()
sprites.add(sprite1, sprite2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    # (Add code to update game objects' states)
    sprites.update()


    # Render game objects
    screen.fill(color)
    # (Add code to draw game objects on the screen)
    sprites.draw(screen)

    #pygame.display.flip()
    pygame.display.update()

# Clean up and quit
pygame.quit()
sys.exit()
