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

# Update a rectangular sprite
class MySprite1(pygame.sprite.Sprite):
   def __init__(self,width_r, width_h,x,y,color):            # constructor
      super().__init__()
      self.image = pygame.Surface((width_r, width_h)) # size rantangle
      self.image.fill(color)  # filling sprite with green
      self.rect = self.image.get_rect(topleft=(x, y))
'''
class MySprite2(pygame.sprite.Sprite):
   def __init__(self):            # constructor
      super().__init__()
      self.image = pygame.Surface((50, 70)) # size rantangle
      self.image.fill((0,255,0))  # filling sprite with green
      self.rect = self.image.get_rect(topleft=(100, 100))
'''
# Create sprite instance and sprite group
my_sprite_1 = MySprite1(50, 70, 10,10, (0,255,0))
my_sprite_2 = MySprite1(50, 70, 100,100, (0,255,0))
sprites = pygame.sprite.Group()
sprites.add(my_sprite_1,my_sprite_2)

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
