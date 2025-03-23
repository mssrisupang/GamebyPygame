# Import necessary libraries
import pygame
import sys

# Initialize PyGame
pygame.init()

# Define game window settings
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My PyGame with sprites')

# Define colors
color = (255, 255, 255)  #white
#color = (0,0,255)       #blue

# Sprite Class
class MySprite(pygame.sprite.Sprite):
   def __init__(self,x, y,imagepath):            # constructor
      super().__init__()
      original_image = pygame.image.load(imagepath).convert_alpha()
      new_width, new_height = 86, 86  # The new size you want for the image
      self.image = pygame.transform.scale(original_image, (new_width, new_height))
      self.rect = self.image.get_rect(topleft=(x, y))

# Create sprite instance and sprite group
sprite_elon = MySprite(10, 10,'musk.png')  # elon sprite
sprite_mas = MySprite(90, 90,'mas.png')  # mas sprite
sprites = pygame.sprite.Group()
sprites.add(sprite_elon,sprite_mas)

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
